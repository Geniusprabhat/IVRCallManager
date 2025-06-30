# Quick Start Guide

Get IVR Call Manager running in 5 minutes!

## 🚀 For Windows Users

1. **Download & Run**
   ```bash
   # Just double-click IVRCallManager.exe
   ```

2. **Configure Twilio**
   - Go to "System Configuration" tab
   - Enter your Twilio credentials
   - Click "SAVE CONFIGURATION"

3. **Make Your First Call**
   - Go to "Initiate Call" tab
   - Enter target phone number (+1234567890)
   - Click "INITIATE CALL SEQUENCE"

## 🐧 For Kali Linux Users

1. **Install Dependencies**
   ```bash
   # Option 1: Use installation script
   chmod +x install.sh
   ./install.sh
   
   # Option 2: Manual installation
   sudo apt install python3 python3-pip python3-tk
   pip3 install -r requirements.txt
   ```

2. **Test Installation**
   ```bash
   python3 test_installation.py
   ```

3. **Run Application**
   ```bash
   python3 ivr_call_manager.py
   ```

4. **Configure & Use** (same as Windows)

## 🔑 Get Twilio Credentials

1. Sign up at [Twilio Console](https://www.twilio.com/console)
2. Get your Account SID and Auth Token
3. Purchase a phone number ($1/month)
4. Add credits to your account

## 📞 Example IVR Script

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="alice">Hello! Welcome to our automated system.</Say>
    <Gather numDigits="1" action="/handle-input" method="POST">
        <Say voice="alice">Press 1 for sales, press 2 for support.</Say>
    </Gather>
    <Say voice="alice">Thank you for calling!</Say>
</Response>
```

## ⚡ Troubleshooting

- **"Failed to initialize Twilio client"** → Check your credentials
- **"Call failed"** → Verify phone number format (+1234567890)
- **Import errors** → Run `pip install -r requirements.txt`

## 📚 Need Help?

- Check the full [README.md](README.md)
- Review [Troubleshooting section](README.md#-troubleshooting)
- Create an issue on GitHub

---

**Ready to make calls?** 🎯 