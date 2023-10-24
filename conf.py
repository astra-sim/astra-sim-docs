# Version of documentation
version = '2.0'
release = version

import datetime
from git import Repo

# Retrive info
repo = Repo()
current_year = datetime.date.today().year

# Project Setup
project = 'ASTRA-sim'
copyright = f'2020-{current_year}, Synergy Lab, Georgia Institute of Technology'
author = 'ASTRA-sim'
repo_name = 'astra-sim-docs'

# Sphinx Setup: Initialization
html_context = dict()

# Sphinx Setup: Extension and theme
extensions = ['myst_parser',
              'sphinx_rtd_theme']
myst_enable_extensions = ['colon_fence']
html_theme = 'sphinx_rtd_theme'

# Sphinx Setup: Paths
templates_path = ['_templates']
exclude_patterns = ['_build', '_scripts', '.DS_Store', 'README.md']
html_static_path = ['_static']

# Get all Versions
versions = [tag.name for tag in repo.tags]
versions.append('latest')

# Compile All Versions
html_context['versions'] = list()
for version in versions:
    if version == 'latest':
        link = f'/{repo_name}/index.html'
    else:
        link = f'/{repo_name}/{version}/index.html'
        
    version_value = (version, link)
    html_context['versions'].append(version_value)
