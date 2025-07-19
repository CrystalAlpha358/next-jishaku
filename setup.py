#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:copyright: (c) 2024 Devon (scarletcafe) R
:copyright: (c) 2025 CrystalAlpha358
:license: MIT, see LICENSE for more details.
"""

import os
import pathlib
import re
import subprocess
import typing

from setuptools import setup

ROOT = pathlib.Path(__file__).parent

with open(ROOT / 'jishaku' / 'meta.py', 'r', encoding='utf-8') as f:
    VERSION_MATCH = re.search(r'VersionInfo\(major=(\d+), minor=(\d+), micro=(\d+), .+\)', f.read(), re.MULTILINE)

    if not VERSION_MATCH:
        raise RuntimeError('version is not set or could not be located')

    version = '.'.join([VERSION_MATCH.group(1), VERSION_MATCH.group(2), VERSION_MATCH.group(3)])

EXTRA_REQUIRES: typing.Dict[str, typing.List[str]] = {}

for feature in (ROOT / 'requirements').glob('*.txt'):
    with open(feature, 'r', encoding='utf-8') as f:
        EXTRA_REQUIRES[feature.with_suffix('').name] = f.read().splitlines()

REQUIREMENTS = EXTRA_REQUIRES.pop('_')

if not version:
    raise RuntimeError('version is not set')


try:
    process = subprocess.Popen(
        ['git', 'rev-list', '--count', 'HEAD'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    COMMIT_COUNT, err = process.communicate()

    if COMMIT_COUNT:
        process = subprocess.Popen(
            ['git', 'rev-parse', '--short', 'HEAD'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        COMMIT_HASH, err = process.communicate()

        if COMMIT_HASH:
            match = re.match(r'(\d).(\d).(\d)(a|b|rc)?', os.getenv('tag_name') or "")

            if (match and match[4]) or not match:
                version += ('' if match else 'a') + COMMIT_COUNT.decode('utf-8').strip() + '+g' + COMMIT_HASH.decode('utf-8').strip()

                # Also attempt to retrieve a branch, when applicable
                process = subprocess.Popen(
                    ['git', 'symbolic-ref', '-q', '--short', 'HEAD'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )

                COMMIT_BRANCH, err = process.communicate()

                if COMMIT_BRANCH:
                    version += "." + re.sub('[^a-zA-Z0-9.]', '.', COMMIT_BRANCH.decode('utf-8').strip())

except FileNotFoundError:
    pass


with open(ROOT / 'README.md', 'r', encoding='utf-8') as f:
    README = f.read()


setup(
    name='next-jishaku',
    author='CrystalAlpha358',
    url='https://github.com/CrystalAlpha358/next-jishaku',

    license='MIT',
    description='A discord.py extension including useful tools for bot development and debugging.',
    long_description=README,
    long_description_content_type='text/markdown',
    project_urls={
        'Code': 'https://github.com/CrystalAlpha358/next-jishaku',
        # 'Issue tracker': 'https://github.com/scarletcafe/jishaku/issues'
    },

    version=version,
    packages=['jishaku', 'jishaku.features', 'jishaku.repl'],
    include_package_data=True,
    install_requires=REQUIREMENTS,
    python_requires='>=3.8.0',

    extras_require=EXTRA_REQUIRES,
    entry_points={
        'console_scripts': [
            'jishaku = jishaku.__main__:entrypoint',
        ],
    },

    # download_url=f'https://github.com/scarletcafe/jishaku/archive/{version}.tar.gz',

    keywords='jishaku discord.py discord cog repl extension',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities'
    ]
)
