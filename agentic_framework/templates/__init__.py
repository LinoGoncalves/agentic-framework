"""
Framework Templates Module

Contains essential framework templates and documentation files 
that are used during project initialization.
"""

from pathlib import Path

# Get the templates directory path
TEMPLATES_DIR = Path(__file__).parent

def get_template_path(template_name):
    """Get the full path to a template file."""
    return TEMPLATES_DIR / template_name

def list_templates():
    """List all available template files."""
    return [f.name for f in TEMPLATES_DIR.glob("*.md")]
