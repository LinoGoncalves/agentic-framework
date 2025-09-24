"""
Agentic Framework Templates

This module contains template files and documentation that are included
with the framework installation for project initialization.
"""

from pathlib import Path

# Get the directory where templates are stored
TEMPLATES_DIR = Path(__file__).parent

def get_template_path(template_name):
    """Get the full path to a template file."""
    return TEMPLATES_DIR / template_name

def list_templates():
    """List all available template files."""
    return [f.name for f in TEMPLATES_DIR.glob('*.md')]