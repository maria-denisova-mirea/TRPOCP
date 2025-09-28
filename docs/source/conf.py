import os
import sys
sys.path.insert(0, os.path.abspath('../'))

project = 'Калькулятор'
copyright = '2025, Denisova M'
author = 'Мария Денисова'
release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']