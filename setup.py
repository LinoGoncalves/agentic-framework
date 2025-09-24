#!/usr/bin/env python3
"""
Setup script for backward compatibility with older pip versions
"""

from setuptools import setup, find_packages

# Read the contents of README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="agentic-framework",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description="A production-ready Human-in-the-Loop (HITL) software development lifecycle framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Agentic Framework Team",
    author_email="info@agentic-framework.dev",
    url="https://github.com/agentic-framework/agentic-framework",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "click>=8.0.0",
        "pathlib",
        "typing-extensions>=3.7.4",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
            "pre-commit",
        ],
        "docs": [
            "sphinx",
            "sphinx-rtd-theme", 
            "myst-parser",
        ],
    },
    entry_points={
        "console_scripts": [
            "agentic-framework=agentic_framework.cli:main",
            "agentic-new=agentic_framework.project:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "ai", "agents", "sdlc", "framework", "automation", "hitl", "development",
        "project-management", "workflow", "orchestration"
    ],
    project_urls={
        "Documentation": "https://agentic-framework.readthedocs.io",
        "Source": "https://github.com/agentic-framework/agentic-framework",
        "Tracker": "https://github.com/agentic-framework/agentic-framework/issues",
    },
)