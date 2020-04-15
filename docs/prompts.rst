Prompts
=======

When you create a package, you are prompted to enter these values.

Templated Values
----------------

The following appear in various parts of your generated project.

full_name
    Your full name.

email
    Your email address.

repo_username
    Your username on the repo host (ie GitHub or GitLab).

project_name
    The name of your new Python package project. This is used in documentation, so spaces and any characters are fine here.

project_dir_name
    Camel case version of project_name without spaces.
    
project_slug
    The namespace of your Python package. This should be Python import-friendly. Typically, it is the slugified version of project_name.

project_short_description
    A 1-sentence description of what your Python package does.

pypi_username
    Your Python Package Index account username.

version
    The starting version number of the package.

repo_base_url
    The base url of the repo hosting

path_on_repo_host
    The part after base url on the repo host. Useful if the project belongs to a GitLab
    project, or sub-project, for instance.
    
Options
-------

The following package configuration options set up different features for your project.

use_pypi_deployment_with_travis
    Whether to use PyPI deployment with Travis.

command_line_interface
    Whether to create a console script using Click. Console script entry point will match the project_slug. Options: ['Click', "No command-line interface"]
