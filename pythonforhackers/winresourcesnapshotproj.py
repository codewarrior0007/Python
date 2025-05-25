# Created 05/24/2025
# Author: https://github.com/codewarrior0007
# Script Name: winresourcesnapshotproj.py
# Script Version: 1.0
# Scripting Language: Python 3.12
# Library used: psutil, socket, getpass, datetime
# Scripting Tool: Visual Studio Code
# Purpose: This script uses above mentioned libraries to collect Windows System snapshot _
# for later analysis
# Disclaimer: This script was written for demonstation purposes only. Any miss use of this _
# script is not the responsibility of the author.  

import psutil 
import socket
import getpass 
import pySMART
import scapy.all as scapy
import pyshark
import os
import mss
import winreg
import win32com.client
import browser_history
import shutil
import pytsk3
import dfvfs 
import plaso
import usbrip
import hachoir
import yara
import pyclamd
from datetime import datetime
from reportlab.pdfgen import canvas

# # Function to capture user account details
def get_user_info():
    user_info = {
        "username" : getpass.getuser(),
        "hostname" : socket.gethostname(),
        "users" : psutil.users() 
     }
    return user_info

# # Function to capture memory usage
def get_memory_snapshot():
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    return {"virtual_memory": memory._asdict(), "swap_memory": swap._asdict()}

# # Function to capture running processes
def get_process_snapshot():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        processes.append(proc.info)
    return processes

# # Function to capture network details
def get_network_snapshot():
    net_info = {
        "interfaces": psutil.net_if_addrs(),
        "connections": psutil.net_connections(kind='inet')
    }
    return net_info

# # Function to capture hard drive SMART data
def get_disk_snapshot():
    drives = {}
    for disk in psutil.disk_partitions():
        drive_name = disk.device
        try:
            smart = pySMART.Device(drive_name)
            drives[drive_name] = smart.attributes
        except:
            drives[drive_name] = "SMART data unavailable"
    return drives
    
# # Function to capture disk partitions
def get_partition_snapshot():
    partitions = psutil.disk_partitions()
    # usage = {p.device: psutil.disk_usage(p.mountpoint)._asdict() for p in partitions}
    # return {"partitions": partitions, "usage": usage}
    usage = {}
    for p in partitions:
           try:
            # Attempt to get disk usage; if the device is not ready, it will raise an exception
                usage[p.device] = psutil.disk_usage(p.mountpoint)._asdict()
           except PermissionError:
                print(f"Skipping {p.device}: Permission denied")
           except FileNotFoundError:
                print(f"Skipping {p.device}: Mount point not found")
           except OSError as e:
                print(f"Skipping {p.device}: {e}")
    return {"partitions": partitions, "usage": usage}
    
# # Function to capture network packets (optional)
def capture_network_packets():
    packets = []
    try:
        cap = pyshark.LiveCapture(interface="Wi-Fi")
        cap.sniff(timeout=5)  # Capture for 5 seconds
        for packet in cap.sniff_continuously(packet_count=10):
            packets.append(str(packet))
    except Exception as e:
        return {"error": str(e)}
    return packets

# # Function to take screen capture for forensic evidence
def take_screenshot():
    with mss.mss() as sct:
        screenshot_file = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        sct.shot(output=screenshot_file)
        return {"screenshot_path": screenshot_file}

# # Function to extract Outlook email metadata
def get_outlook_emails():
    try:
        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        inbox = outlook.GetDefaultFolder(6)  # 6 = Inbox
        emails = []
        
        for message in inbox.Items[:5]:  # Extract last 5 emails
            emails.append({
                "subject": message.Subject,
                "sender": message.SenderName,
                "timestamp": message.SentOn.strftime("%Y-%m-%d %H:%M:%S")
            })
        return emails
    except Exception as e:
        return {"error": str(e)}

# # Function to extract registry keys
def get_registry_keys():
    keys = ["SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", "SYSTEM\\CurrentControlSet\\Services"]
    registry_data = {}

    try:
        for key in keys:
            reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key, 0, winreg.KEY_READ)
            registry_data[key] = {}
            
            i = 0
            while True:
                try:
                    name, value, _ = winreg.EnumValue(reg, i)
                    registry_data[key][name] = value
                    i += 1
                except OSError:
                    break
    except Exception as e:
        return {"error": str(e)}

    return registry_data

 # Function to extract browser history
def get_browser_history():
    try:
        outputs = browser_history.get_history()
        history = [{"timestamp": str(entry[0]), "url": entry[1]} for entry in outputs.histories]
        return history
    except Exception as e:
        return {"error": str(e)}

# # Aggregate all forensic snapshots
def collect_forensic_snapshot():
     forensic_data = {
        "user_info": get_user_info(),
        "memory_snapshot": get_memory_snapshot(),
        "process_snapshot": get_process_snapshot(), 
        "network_snapshot": get_network_snapshot(),    
        "disk_snapshot": get_disk_snapshot(), 
        "partition_snapshot": get_partition_snapshot(),  
        "network_packets": capture_network_packets(),  
        "screenshot": take_screenshot(), 
        "outlook_emails": get_outlook_emails(),
        "registry_keys": get_registry_keys(),  
        "browser_history": get_browser_history(),         
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     }
    
     return forensic_data

## Main to print forensics snapshot
if __name__ == "__main__":
     print(collect_forensic_snapshot())
