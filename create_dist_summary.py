#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:copyright: (c) 2024 Devon (scarletcafe) R
:copyright: (c) 2025 CrystalAlpha358
:license: MIT, see LICENSE for more details.
"""

import hashlib
import importlib.metadata
import os
import pathlib
import subprocess
import typing

from jinja2 import Environment
from jinja2.environment import Template
from jinja2.loaders import BaseLoader


class File(typing.NamedTuple):
    """
    Artifact file descriptor
    """
    name: str
    md5: str
    sha1: str
    sha256: str


ENVIRONMENT = Environment(loader=BaseLoader())
FILES: typing.List[File] = []

for file in pathlib.Path('dist').iterdir():
    if file.is_file() and file.name.lower().endswith(('.whl', '.egg', '.tar.gz')):
        with open(file, 'rb') as fp:
            data = fp.read()

        FILES.append(File(
            name=file.name,
            md5=hashlib.md5(data).hexdigest(),
            sha1=hashlib.sha1(data).hexdigest(),
            sha256=hashlib.sha256(data).hexdigest()
        ))

process = subprocess.Popen(
    ['git', 'tag', '-l', '--sort=version:refname'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

tags, err = process.communicate()
tags = tags.decode('utf-8').strip().split('\n')

while tags[-1].lower().strip() == (os.getenv('tag_name') or '').lower().strip():
    tags.pop(-1)

last_version = tags[-1]

process = subprocess.Popen(
    ['git', 'rev-parse', '--short', 'HEAD'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

commit_hash, err = process.communicate()
commit_hash = commit_hash.decode('utf-8').strip()

with open('dist_summary.jinja2', 'r', encoding='utf-8') as fp:
    template: Template = ENVIRONMENT.from_string(fp.read())

with open('dist/DIST_SUMMARY.md', 'w', encoding='utf-8') as fp:
    output = template.render(
        env=os.getenv,
        package=importlib.metadata.distribution('jishaku'),
        files=FILES,
        last_version=last_version,
        commit_hash=commit_hash,
    )

    # Jinja loves obliterating trailing newlines
    if not output.endswith('\n'):
        output += '\n'

    fp.write(output)
