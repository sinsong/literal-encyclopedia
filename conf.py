# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'literal-encyclopedia'
copyright = '2022, literal'
author = 'literal'
# release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_copybutton',
    'sphinxnotes.strike'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

html_title = "莉特雅百科全书"
html_theme_options = {
    "light_css_variables": {

    },
    "dark_css_variables": {
        "color-brand-primary": "#6495ed"
    },
    "source_repository": "https://github.com/sinsong/literal-encyclopedia",
    "source_branch": "master",
    # "source_directory": ""
}
