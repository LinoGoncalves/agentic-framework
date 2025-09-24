#!/usr/bin/env python3
"""
CLI Entry Point for Agentic Framework
"""

import sys
import os
import argparse
import subprocess
from pathlib import Path
from .core import FrameworkManager, get_version
from .project import ProjectInitializer


def check_cli_installation():
    """Check if CLI commands are properly accessible and provide guidance if not."""
    try:
        # Try to find the CLI scripts
        result = subprocess.run(['which', 'agentic-framework'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ CLI commands are properly installed and accessible!")
            return True
    except FileNotFoundError:
        # 'which' command not found (Windows)
        try:
            result = subprocess.run(['where', 'agentic-framework'], capture_output=True, text=True, shell=True)
            if result.returncode == 0:
                print("✅ CLI commands are properly installed and accessible!")
                return True
        except Exception:
            pass
    
    print("⚠️  CLI commands are not accessible from PATH")
    print("\n🔧 Solutions:")
    print("1. Use module execution: python -m agentic_framework")
    print("2. Add Scripts directory to PATH:")
    
    if os.name == 'nt':  # Windows
        import site
        user_scripts = Path(site.getusersitepackages()).parent / "Scripts"
        print(f"   Add this to your PATH: {user_scripts}")
        print("   Or run: setx PATH \"%PATH%;" + str(user_scripts) + "\"")
    else:  # Unix/Linux/macOS
        user_base = subprocess.run([sys.executable, '-m', 'site', '--user-base'], 
                                 capture_output=True, text=True).stdout.strip()
        user_scripts = Path(user_base) / "bin"
        print(f"   Add this to your PATH: {user_scripts}")
        print(f"   Or add to ~/.bashrc: export PATH=\"{user_scripts}:$PATH\"")
    
    print("3. Use virtual environment (recommended for development)")
    return False


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
    
    # Doctor command (diagnose installation)
    subparsers.add_parser("doctor", help="Diagnose CLI installation and provide setup guidance")
    
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
            
        elif args.command == "doctor":
            print("🔍 Agentic Framework Installation Diagnostics")
            print("=" * 50)
            check_cli_installation()
            print("\n📚 For more help, visit: https://github.com/LinoGoncalves/agentic-framework#installation")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()