#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if 'GNU General Public License v3' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')
    else:
        remove_file('COPYING')
        remove_file("devel/template.py")

    if "{{ cookiecutter.repo_host }}" != 'GitLab':
        remove_file('.gitlab-ci.yml')
    if "{{ cookiecutter.repo_host }}" != 'GitHub':
        remove_file('.travis.yml')
