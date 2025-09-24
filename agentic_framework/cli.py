#!/usr/bin/env python3
"""
CLI Entry Point for Agentic Framework
"""

import sys
import argparse
from .core import FrameworkManager, get_version
from .project import ProjectInitializer


def create_parser():
    """Create the argument parser."""
    parser = argparse.ArgumentParser(
        prog="agentic-framework",
        description="Agentic SDLC Framework - AI-assisted software development"
    )
    
    parser.add_argument(
        "--version", 
        action="version", 
        version=f"agentic-framework {get_version()}"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Init command
    init_parser = subparsers.add_parser("init", help="Initialize a new project")
    init_parser.add_argument("name", help="Project name")
    init_parser.add_argument("--type", default="web-app", help="Project type")
    init_parser.add_argument("--output", help="Output directory")
    
    # New command (interactive wizard)
    subparsers.add_parser("new", help="Start interactive project wizard")
    
    return parser


def main():
    """Main CLI entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        if args.command == "init":
            framework_manager = FrameworkManager()
            framework_manager.init_project(
                project_name=args.name,
                project_type=args.type,
                output_dir=args.output
            )
        
        elif args.command == "new":
            initializer = ProjectInitializer()
            initializer.start_wizard()
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()