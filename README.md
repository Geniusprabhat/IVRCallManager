<!-- Follow me on Instagram: @genius_prabhat -->
# IVR Call Manager

Interactive Voice Response (IVR) Call Manager with Twilio integration for Windows and Kali Linux.

## 🚀 Features

- **Cross-Platform Support**: Windows (.exe) and Kali Linux (Python)
- **Twilio Integration**: Seamless integration with Twilio's voice services
- **Custom IVR Scripts**: Support for custom TwiML scripts
- **User-Friendly GUI**: Intuitive interface for easy configuration and call management
- **Real-time Status**: Live call status updates
- **Secure Configuration**: Encrypted storage of Twilio credentials

## 📋 Requirements

### For Windows:
- Windows 10/11
- No additional installation required (standalone .exe)

### For Kali Linux/Linux:
- Python 3.6+
- tkinter (usually pre-installed)
- Internet connection
- Twilio account

## 🛠️ Installation

### Windows Installation:
1. Download the `IVRCallManager.exe` file
2. Extract to any folder
3. Run `IVRCallManager.exe`

### Kali Linux Installation:
```bash
# Clone the repository
git clone https://github.com/yourusername/ivr-call-manager.git
cd ivr-call-manager

# Install Python dependencies
pip install -r requirements.txt

# Make the script executable
chmod +x ivr_call_manager.py

# Run the application
python3 ivr_call_manager.py
```

## 🔧 Setup

### 1. Get Twilio Credentials
1. Sign up at [Twilio Console](https://www.twilio.com/console)
2. Get your Account SID and Auth Token
3. Purchase a Twilio phone number

### 2. Configure the Application
1. Run the application
2. Go to "System Configuration" tab
3. Enter your Twilio credentials:
   - Account SID
   - Auth Token
   - Twilio Phone Number
4. Click "SAVE CONFIGURATION"

## 📞 Usage

### Making Calls:
1. Go to "Initiate Call" tab
2. Enter the target phone number (with country code)
3. Customize the IVR script if needed
4. Click "INITIATE CALL SEQUENCE"

### Custom IVR Scripts:
The application supports custom TwiML scripts. Example:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="alice">Hello! This is an automated call.</Say>
    <Gather numDigits="1" action="/handle-input" method="POST">
        <Say voice="alice">Press 1 for sales, press 2 for support.</Say>
    </Gather>
    <Say voice="alice">Thank you for calling. Goodbye!</Say>
</Response>
```

## 📁 File Structure

```
IVRCallManager/
├── IVRCallManager.exe          # Windows executable
├── ivr_call_manager.py         # Python version for Linux
├── requirements.txt            # Python dependencies
├── ivr_config.json            # Configuration file
├── README.md                  # This file
└── README.txt                 # Original Windows instructions
```

## 🔒 Security Notes

- Twilio credentials are stored locally in `ivr_config.json`
- Never share your Twilio credentials
- Use this tool responsibly and in compliance with local laws
- Ensure you have permission to call the target numbers

## ⚠️ Legal Disclaimer

This tool is intended for educational and legitimate business purposes only. Users are responsible for:

- Complying with local telephony laws and regulations
- Obtaining proper consent for automated calls
- Following Do Not Call (DNC) lists and regulations
- Respecting privacy and communication preferences

## 🐛 Troubleshooting

### Common Issues:

1. **"Failed to initialize Twilio client"**
   - Check your Account SID and Auth Token
   - Ensure your Twilio account is active

2. **"Call failed"**
   - Verify the target phone number format (+1234567890)
   - Check your Twilio account balance
   - Ensure the target number is valid

3. **Python import errors**
   - Install required packages: `pip install -r requirements.txt`
   - Ensure Python 3.6+ is installed

### Kali Linux Specific:
```bash
# If tkinter is not installed
sudo apt-get install python3-tk

# If pip is not available
sudo apt-get install python3-pip
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review Twilio documentation

## 🔄 Version History

- **v1.0**: Initial release with Windows and Linux support
- Basic IVR functionality
- Twilio integration
- GUI interface

---

**Note**: This tool requires a valid Twilio account with sufficient credits to make calls. 