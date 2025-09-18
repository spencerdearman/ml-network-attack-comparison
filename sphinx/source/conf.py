# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Detecting Brute Force, DDoS, and DoS Attacks: A Supervised Learning Comparison'
copyright = '2024, Kanchan Naik, Spencer Dearman'
author = 'Kanchan Naik, Spencer Dearman'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_nb",
]

# Enable or disable execution of notebooks
nb_execution_mode = "off"  # Disable execution for faster builds if no live outputs are needed

# Templates and exclude patterns
templates_path = ['_templates']
exclude_patterns = []

# Exclude cells with specific tags
nb_remove_cell_tags = ["remove-cell", "exclude-from-docs", "hide-input"]  # Ensure this matches your notebook's tags
nb_merge_streams = True  # Merge stdout and stderr for cleaner logs
nb_render_priority = {"html": ["text/html", "text/markdown", "text/plain"]}
nb_remove_empty_cells = True  # Remove cells with no content

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"  # Change to desired theme
html_static_path = ['_static']