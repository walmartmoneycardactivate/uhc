import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project Information -----------------------------------------------------

project = 'UCard Help Documentation'
copyright = '2025, UCard Help'
author = 'UCard Help Team'
release = '1.0.0'

# -- General Configuration ---------------------------------------------------

extensions = [
    'myst_parser',  # Optional, for .md support if needed
]

templates_path = ['_templates']
exclude_patterns = []

# -- HTML Output -------------------------------------------------------------

html_theme = 'sphinx_book_theme'

html_title = "UCard Help Center"
html_short_title = "UCard Help"
html_favicon = 'favicon.ico'  # Optional: place favicon.ico in root or _static

html_theme_options = {
    "repository_url": "https://github.com/your-org/ucard-docs",  # optional
    "use_repository_button": False,
    "use_edit_page_button": False,
    "home_page_in_toc": True,
    "show_navbar_depth": 1,
    "navigation_with_keys": True,
}

html_context = {
    "display_github": False,
    "default_mode": "auto",
}

html_static_path = ['_static']  # Optional

html_show_sourcelink = False
html_show_sphinx = False

# -- Options for reStructuredText -------------------------------------------

source_suffix = {
    '.rst': 'restructuredtext',
    # '.md': 'markdown',  # Uncomment if you want Markdown support
}
