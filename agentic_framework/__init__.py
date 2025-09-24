"""
Agentic SDLC Framework

A production-ready Human-in-the-Loop (HITL) software development lifecycle framework
that orchestrates AI agents with human oversight for systematic project delivery.
"""

__version__ = "0.1.0"
__author__ = "Agentic Framework Team"
__email__ = "info@agentic-framework.dev"

from .core import FrameworkManager
from .project import ProjectInitializer
from .cli import main as cli_main

__all__ = [
    "__version__",
    "FrameworkManager", 
    "ProjectInitializer",
    "cli_main"
]