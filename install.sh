#!/bin/bash

# IVR Call Manager - Installation Script for Kali Linux
# This script installs the required dependencies and sets up the IVR Call Manager

# Follow me on Instagram: @genius_prabhat

echo "🚀 IVR Call Manager - Installation Script for Kali Linux"
echo "========================================================"

# Check if running as root
if [ "$EUID" -eq 0 ]; then
    echo "❌ Please don't run this script as root. Run as normal user."
    exit 1
fi

# Update package list
echo "📦 Updating package list..."
sudo apt update

# Install Python3 and pip if not already installed
echo "🐍 Installing Python3 and pip..."
sudo apt install -y python3 python3-pip python3-tk

# Install required Python packages
echo "📚 Installing Python dependencies..."
pip3 install -r requirements.txt

# Make the Python script executable
echo "🔧 Making script executable..."
chmod +x ivr_call_manager.py

# Create desktop shortcut (optional)
echo "🖥️ Creating desktop shortcut..."
cat > ~/Desktop/IVR-Call-Manager.desktop << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=IVR Call Manager
Comment=Interactive Voice Response Call Manager
Exec=$(pwd)/ivr_call_manager.py
Icon=phone
Terminal=false
Categories=Network;Telephony;
EOF

chmod +x ~/Desktop/IVR-Call-Manager.desktop

echo ""
echo "✅ Installation completed successfully!"
echo ""
echo "📋 Next steps:"
echo "1. Run the application: python3 ivr_call_manager.py"
echo "2. Or double-click the desktop shortcut"
echo "3. Configure your Twilio credentials in the System Configuration tab"
echo ""
echo "🔗 Get Twilio credentials from: https://www.twilio.com/console"
echo ""
echo "📖 For more information, see README.md" 