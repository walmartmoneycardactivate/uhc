# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'UCard Help Documentation'
copyright = '2025, UCard Help'
author = 'UCard Support Team'
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

html_title = "UCard Help Center – Activate, Shop, and Check Balance"
html_short_title = "UCard Help"
html_favicon = 'favicon.ico'  # Place in root or _static

# html_theme = 'sphinx_rtd_theme'  # Uncomment if using RTD theme

html_show_sourcelink = False
html_allow_unsafe = True
raw_enabled = True

# Optional: Add custom templates or static files
templates_path = ['_templates']
# html_static_path = ['_static']

# -- Theme Options (optional) ------------------------------------------------

html_theme_options = {
    'show_powered_by': False,
}
