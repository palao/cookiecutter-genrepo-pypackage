.. highlight:: shell

============
Installation
============


Stable release
--------------

To install {{ cookiecutter.project_name }}, run this command in your terminal:

.. code-block:: console

    $ pip install {{ cookiecutter.project_slug }}

This is the preferred method to install {{ cookiecutter.project_name }}, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for {{ cookiecutter.project_name }} can be downloaded from the `{{ cookiecutter.repo_host}} repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://{{ cookiecutter.repo_host.lower() }}.com/{{ cookiecutter.path_on_repo_host }}

Or download the {% if cookiecutter.repo_host == 'GitLab' -%}tarball{% elif cookiecutter.repo_host == 'GitHub' %}`tarball`_{% endif -%}:

.. code-block:: console

    $ curl -OJL {{ cookiecutter.repo_base_url }}/{{ cookiecutter.path_on_repo_host }}/{% if cookiecutter.repo_host == 'GitLab' -%}-/archive/master/{{ cookiecutter.project_slug }}-{% elif cookiecutter == 'GitHub' %}archive/{%- endif %}master.zip

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _{{ cookiecutter.repo_host}} repo: {{ cookiecutter.repo_base_url }}/{{ cookiecutter.path_on_repo_host }}
{% if cookiecutter.repo_host == 'GitHub' -%}.. _tarball: {{ cookiecutter.repo_base_url }}/{{ cookiecutter.path_on_repo_host }}/tarball/master{%- endif %}
