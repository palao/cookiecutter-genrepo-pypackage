{% if cookiecutter.open_source_license == 'GNU General Public License v3' -%}
#######################################################################
#
# Copyright (C) {% now 'local', '%Y' %} {{ cookiecutter.full_name }}
#
# This file is part of {{ cookiecutter.project_name }}.
#
#  {{ cookiecutter.project_name }} is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  {{ cookiecutter.project_name }} is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with {{ cookiecutter.project_name }}.  If not, see <http://www.gnu.org/licenses/>.
#
#######################################################################
{%- endif %}
