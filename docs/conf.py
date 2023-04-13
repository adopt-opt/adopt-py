# Project information
project = "ADOPT: AI-Driven Design and Optimization"
copyright = "2023, Technical University of Munich"
author = "ADOPT Authors"

# General configuration
extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]
intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]
templates_path = ["_templates"]

# Options for EPUB output
epub_show_urls = "footnote"

# Ignore patterns
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Setting the theme
html_theme = "alabaster"
