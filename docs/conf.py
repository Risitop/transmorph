# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.append(os.path.abspath("../src/"))

project = "transmorph"
copyright = "2022, Aziz Fouché, Loïc Chadoutaud, Andrei Zinovyev"
author = "Aziz Fouché, Loïc Chadoutaud, Andrei Zinovyev"
release = "0.2.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx_math_dollar",
    "sphinx.ext.napoleon",
    "nbsphinx",
    "sphinxcontrib.bibtex",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]
bibtex_bibfiles = ["biblio.bib"]

autodoc_mock_imports = [
    "anndata",
    "igraph",
    "leidenalg",
    "pre-commit",
    "pot",
    "pymde",
    "pynndescent",
    "scanpy",
    "scipy",
    "stabilized-ica",
    "umap-learn",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "bizstyle"
html_static_path = ["_static"]
html_logo = "../img/logo_v2.png"
html_favicon = "../img/favicon.ico"
