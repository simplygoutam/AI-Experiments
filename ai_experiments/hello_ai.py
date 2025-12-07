#!/usr/bin/env python3
"""
Hello AI - A simple runnable AI experimentation script
This demonstrates a basic setup for AI coding experiments
"""

import sys

def main():
    """
    Main function to demonstrate a working Python setup.
    """
    print("=" * 50)
    print("AI Python Code Experimentation Setup")
    print("=" * 50)
    print()
    print("✓ Python environment is working correctly!")
    print(f"✓ Python version: {sys.version}")
    print()
    print("Setup Instructions:")
    print("1. Create a virtual environment: python -m venv venv")
    print("2. Activate it: source venv/bin/activate (Mac/Linux)")
    print("   or: venv\\Scripts\\activate (Windows)")
    print("3. Install dependencies: pip install -r requirements.txt")
    print("4. Run this script: python ai_experiments/hello_ai.py")
    print()
    print("Next Steps:")
    print("- Add your AI experiments in the ai_experiments/ folder")
    print("- Use utils/ folder for shared helper functions")
    print("- Update requirements.txt with new dependencies")
    print()
    print("Ready for AI Event! 🚀")
    print("=" * 50)

if __name__ == "__main__":
    main()
