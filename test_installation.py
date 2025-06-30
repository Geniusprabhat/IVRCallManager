#!/usr/bin/env python3
# Follow me on Instagram: @genius_prabhat
"""
Test script to verify IVR Call Manager installation
"""

import sys
import importlib

def test_imports():
    """Test if all required packages can be imported"""
    required_packages = [
        'tkinter',
        'json',
        'os',
        'threading',
        'twilio',
        'requests'
    ]
    
    print("🧪 Testing IVR Call Manager Installation")
    print("=" * 40)
    
    all_good = True
    
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package} - OK")
        except ImportError as e:
            print(f"❌ {package} - FAILED: {e}")
            all_good = False
    
    print("\n" + "=" * 40)
    
    if all_good:
        print("🎉 All dependencies are installed correctly!")
        print("You can now run: python3 ivr_call_manager.py")
    else:
        print("❌ Some dependencies are missing.")
        print("Please run: pip install -r requirements.txt")
        print("Or run the installation script: ./install.sh")
    
    return all_good

def test_tkinter():
    """Test if tkinter GUI works"""
    try:
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()  # Hide the window
        root.destroy()
        print("✅ Tkinter GUI - OK")
        return True
    except Exception as e:
        print(f"❌ Tkinter GUI - FAILED: {e}")
        return False

if __name__ == "__main__":
    print("IVR Call Manager - Installation Test")
    print("====================================")
    
    # Test Python version
    print(f"🐍 Python version: {sys.version}")
    
    # Test imports
    imports_ok = test_imports()
    
    # Test GUI
    if imports_ok:
        test_tkinter()
    
    print("\n📋 Summary:")
    if imports_ok:
        print("✅ Ready to use IVR Call Manager!")
    else:
        print("❌ Please install missing dependencies first.") 