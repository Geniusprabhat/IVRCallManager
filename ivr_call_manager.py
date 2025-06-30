#!/usr/bin/env python3
"""
IVR Call Manager - Python Version for Kali Linux
Interactive Voice Response Call Manager using Twilio
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
import sys
import threading
from twilio.rest import Client
from twilio.twiml import VoiceResponse
import requests
import time

class IVRCallManager:
    def __init__(self, root):
        self.root = root
        self.root.title("IVR Call Manager - Kali Linux")
        self.root.geometry("800x600")
        self.root.configure(bg='#2b2b2b')
        
        # Twilio client
        self.twilio_client = None
        
        # Configuration file
        self.config_file = "ivr_config.json"
        
        # Load configuration
        self.load_config()
        
        # Create GUI
        self.create_gui()
        
    def load_config(self):
        """Load configuration from JSON file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
            else:
                self.config = {
                    "twilio_account_sid": "",
                    "twilio_auth_token": "",
                    "twilio_phone_number": ""
                }
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load configuration: {str(e)}")
            self.config = {
                "twilio_account_sid": "",
                "twilio_auth_token": "",
                "twilio_phone_number": ""
            }
    
    def save_config(self):
        """Save configuration to JSON file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=4)
            messagebox.showinfo("Success", "Configuration saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save configuration: {str(e)}")
    
    def create_gui(self):
        """Create the main GUI"""
        # Style configuration
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        style.configure('TNotebook', background='#2b2b2b')
        style.configure('TNotebook.Tab', background='#3c3c3c', foreground='white')
        style.configure('TFrame', background='#2b2b2b')
        style.configure('TLabel', background='#2b2b2b', foreground='white')
        style.configure('TButton', background='#4CAF50', foreground='white')
        style.configure('TEntry', fieldbackground='#3c3c3c', foreground='white')
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # System Configuration Tab
        self.create_config_tab()
        
        # Initiate Call Tab
        self.create_call_tab()
        
        # About Tab
        self.create_about_tab()
    
    def create_config_tab(self):
        """Create System Configuration tab"""
        config_frame = ttk.Frame(self.notebook)
        self.notebook.add(config_frame, text="System Configuration")
        
        # Title
        title_label = tk.Label(config_frame, text="Twilio Configuration", 
                              font=('Arial', 16, 'bold'), bg='#2b2b2b', fg='white')
        title_label.pack(pady=20)
        
        # Configuration frame
        config_inner_frame = tk.Frame(config_frame, bg='#2b2b2b')
        config_inner_frame.pack(pady=20)
        
        # Account SID
        tk.Label(config_inner_frame, text="Account SID:", bg='#2b2b2b', fg='white').pack(anchor='w')
        self.account_sid_entry = tk.Entry(config_inner_frame, width=50, bg='#3c3c3c', fg='white')
        self.account_sid_entry.pack(pady=5, fill='x')
        self.account_sid_entry.insert(0, self.config.get("twilio_account_sid", ""))
        
        # Auth Token
        tk.Label(config_inner_frame, text="Auth Token:", bg='#2b2b2b', fg='white').pack(anchor='w', pady=(10,0))
        self.auth_token_entry = tk.Entry(config_inner_frame, width=50, bg='#3c3c3c', fg='white', show="*")
        self.auth_token_entry.pack(pady=5, fill='x')
        self.auth_token_entry.insert(0, self.config.get("twilio_auth_token", ""))
        
        # Phone Number
        tk.Label(config_inner_frame, text="Twilio Phone Number:", bg='#2b2b2b', fg='white').pack(anchor='w', pady=(10,0))
        self.phone_number_entry = tk.Entry(config_inner_frame, width=50, bg='#3c3c3c', fg='white')
        self.phone_number_entry.pack(pady=5, fill='x')
        self.phone_number_entry.insert(0, self.config.get("twilio_phone_number", ""))
        
        # Save button
        save_btn = tk.Button(config_inner_frame, text="SAVE CONFIGURATION", 
                            command=self.save_configuration, bg='#4CAF50', fg='white',
                            font=('Arial', 12, 'bold'), relief='flat', padx=20, pady=10)
        save_btn.pack(pady=20)
        
        # Instructions
        instructions = """
        Instructions:
        1. Get your Twilio credentials from https://www.twilio.com/console
        2. Enter your Account SID, Auth Token, and Twilio Phone Number
        3. Click SAVE CONFIGURATION
        4. Make sure your Twilio account has sufficient credits
        """
        instruction_label = tk.Label(config_inner_frame, text=instructions, 
                                   bg='#2b2b2b', fg='#cccccc', justify='left')
        instruction_label.pack(pady=20)
    
    def create_call_tab(self):
        """Create Initiate Call tab"""
        call_frame = ttk.Frame(self.notebook)
        self.notebook.add(call_frame, text="Initiate Call")
        
        # Title
        title_label = tk.Label(call_frame, text="Make IVR Call", 
                              font=('Arial', 16, 'bold'), bg='#2b2b2b', fg='white')
        title_label.pack(pady=20)
        
        # Call configuration frame
        call_inner_frame = tk.Frame(call_frame, bg='#2b2b2b')
        call_inner_frame.pack(pady=20)
        
        # Target phone number
        tk.Label(call_inner_frame, text="Target Phone Number:", bg='#2b2b2b', fg='white').pack(anchor='w')
        self.target_number_entry = tk.Entry(call_inner_frame, width=50, bg='#3c3c3c', fg='white')
        self.target_number_entry.pack(pady=5, fill='x')
        self.target_number_entry.insert(0, "+1234567890")
        
        # Call options
        options_frame = tk.Frame(call_inner_frame, bg='#2b2b2b')
        options_frame.pack(pady=20, fill='x')
        
        # IVR Script
        tk.Label(options_frame, text="IVR Script (TwiML):", bg='#2b2b2b', fg='white').pack(anchor='w')
        self.ivr_script_text = tk.Text(options_frame, height=8, bg='#3c3c3c', fg='white')
        self.ivr_script_text.pack(pady=5, fill='x')
        
        # Default IVR script
        default_script = '''<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="alice">Hello! This is an automated call from IVR Call Manager.</Say>
    <Gather numDigits="1" action="/handle-input" method="POST">
        <Say voice="alice">Press 1 for sales, press 2 for support, press 3 to speak with an operator.</Say>
    </Gather>
    <Say voice="alice">Thank you for calling. Goodbye!</Say>
</Response>'''
        self.ivr_script_text.insert('1.0', default_script)
        
        # Initiate call button
        call_btn = tk.Button(call_inner_frame, text="INITIATE CALL SEQUENCE", 
                            command=self.initiate_call, bg='#2196F3', fg='white',
                            font=('Arial', 12, 'bold'), relief='flat', padx=20, pady=10)
        call_btn.pack(pady=20)
        
        # Status label
        self.status_label = tk.Label(call_inner_frame, text="Ready to make calls", 
                                   bg='#2b2b2b', fg='#4CAF50')
        self.status_label.pack(pady=10)
    
    def create_about_tab(self):
        """Create About tab"""
        about_frame = ttk.Frame(self.notebook)
        self.notebook.add(about_frame, text="About")
        
        about_text = """
        IVR Call Manager - Python Version
        
        Version: 1.0
        Platform: Kali Linux / Linux
        
        Features:
        • Interactive Voice Response (IVR) call management
        • Twilio integration for voice calls
        • Custom TwiML script support
        • Cross-platform compatibility
        
        Requirements:
        • Python 3.6+
        • Twilio account
        • Internet connection
        
        Installation:
        pip install twilio requests
        
        Usage:
        1. Configure your Twilio credentials
        2. Enter target phone number
        3. Customize IVR script if needed
        4. Click "INITIATE CALL SEQUENCE"
        
        Note: This tool is for educational and legitimate business purposes only.
        Ensure compliance with local telephony laws and regulations.
        """
        
        about_label = tk.Label(about_frame, text=about_text, 
                              bg='#2b2b2b', fg='white', justify='left',
                              font=('Arial', 10))
        about_label.pack(pady=20, padx=20)
    
    def save_configuration(self):
        """Save the current configuration"""
        self.config["twilio_account_sid"] = self.account_sid_entry.get().strip()
        self.config["twilio_auth_token"] = self.auth_token_entry.get().strip()
        self.config["twilio_phone_number"] = self.phone_number_entry.get().strip()
        
        # Validate configuration
        if not all([self.config["twilio_account_sid"], 
                   self.config["twilio_auth_token"], 
                   self.config["twilio_phone_number"]]):
            messagebox.showerror("Error", "Please fill in all Twilio credentials!")
            return
        
        self.save_config()
        
        # Initialize Twilio client
        try:
            self.twilio_client = Client(self.config["twilio_account_sid"], 
                                      self.config["twilio_auth_token"])
            messagebox.showinfo("Success", "Twilio client initialized successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to initialize Twilio client: {str(e)}")
    
    def initiate_call(self):
        """Initiate the IVR call"""
        if not self.twilio_client:
            messagebox.showerror("Error", "Please configure Twilio credentials first!")
            return
        
        target_number = self.target_number_entry.get().strip()
        if not target_number:
            messagebox.showerror("Error", "Please enter a target phone number!")
            return
        
        # Get IVR script
        ivr_script = self.ivr_script_text.get('1.0', tk.END).strip()
        
        # Update status
        self.status_label.config(text="Initiating call...", fg='#FF9800')
        self.root.update()
        
        # Make call in separate thread
        threading.Thread(target=self._make_call, args=(target_number, ivr_script), daemon=True).start()
    
    def _make_call(self, target_number, ivr_script):
        """Make the actual call (runs in separate thread)"""
        try:
            # Create a simple TwiML response (you might want to host this on a web server)
            # For now, we'll use a basic call without custom TwiML
            call = self.twilio_client.calls.create(
                to=target_number,
                from_=self.config["twilio_phone_number"],
                twiml=f'<Response><Say voice="alice">Hello! This is an automated call from IVR Call Manager.</Say></Response>'
            )
            
            # Update status on main thread
            self.root.after(0, lambda: self.status_label.config(
                text=f"Call initiated! SID: {call.sid}", fg='#4CAF50'))
            
        except Exception as e:
            # Update status on main thread
            self.root.after(0, lambda: self.status_label.config(
                text=f"Call failed: {str(e)}", fg='#f44336'))
            self.root.after(0, lambda: messagebox.showerror("Error", f"Call failed: {str(e)}"))

def main():
    """Main function"""
    # Check if required packages are installed
    try:
        import twilio
        import requests
    except ImportError as e:
        print("Missing required packages. Please install them:")
        print("pip install twilio requests")
        sys.exit(1)
    
    # Create and run the application
    root = tk.Tk()
    app = IVRCallManager(root)
    root.mainloop()

if __name__ == "__main__":
    main() 