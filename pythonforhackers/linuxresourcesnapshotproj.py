# Created 05/25/2025
# Author: https://github.com/codewarrior0007
# Script Name: linuxresourcesnapshotproj.py
# Script Version: 1.0
# Scripting Language: Python 3.12
# Library used: subprocess, json, os, time
# Inputs : configuration file (e.g., config.json)
# Output: Response from the server in bytes and decoded string
# # Scripting Tool: Visual Studio Code
# Purpose: This script uses above mentioned libraries to collect Linux System snapshot _
# for later analysis.  
# Disclaimer: This script was written for demonstation purposes only. Any misuse of this _
# script is not the responsibility of the author.  

import subprocess
import json
import os
import time

# Load configuration from JSON
config_file = "<location of the project>/config.json"

if not os.path.exists(config_file):
    print(f"Configuration file {config_file} not found!")
    exit(1)

with open(config_file, "r") as file:
    config = json.load(file)

# Configurations for various files
base_path = config["base_path"]
output_log_file = os.path.join(base_path, config["output_log_file"])
network_capture_file1 = os.path.join(base_path, config["network_capture_file1"])
network_capture_file2 = os.path.join(base_path, config["network_capture_file2"])

# Ensure base path exists
os.makedirs(base_path, exist_ok=True)

# Function to execute system commands and log output
def capture_command_output(command, filename):
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        with open(filename, "a") as file:
            file.write(f"\n### {command} ###\n")
            file.write(result.stdout + "\n")
    except Exception as e:
        print(f"Error running {command}: {e}")

# Capture user activity
capture_command_output("who", output_log_file)
capture_command_output("whoami", output_log_file)
capture_command_output("pwd", output_log_file)

# Capture Linux Kernel version
capture_command_output("uname -a", output_log_file)
capture_command_output("cat /proc/version", output_log_file)

# Capture file integrity check (e.g., system binaries)
capture_command_output("sha256sum /bin/bash /bin/ls /bin/ps", output_log_file)

# Capture networking details
capture_command_output("netstat -tulnp", output_log_file)
capture_command_output("ss -tulnp", output_log_file)
capture_command_output("ip addr show", output_log_file)
capture_command_output("ip link show", output_log_file)
capture_command_output("ip neigh show", output_log_file)
capture_command_output("iptables -L", output_log_file)
capture_command_output("ip tunnel show", output_log_file)
capture_command_output("cat /etc/hosts", output_log_file)
capture_command_output("ifconfig", output_log_file)

# Capture active connections
capture_command_output("lsof -i -P -n", output_log_file)

# Capture partition tables
capture_command_output("lsblk", output_log_file)
capture_command_output("df -h", output_log_file)

# Capture Accounts
capture_command_output("cat /etc/passwd | grep bash", output_log_file)
capture_command_output("cat /etc/passwd | grep sh", output_log_file)
capture_command_output("cat /etc/shadow", output_log_file)
capture_command_output("cat /etc/group", output_log_file)
capture_command_output("cat /etc/sudoers", output_log_file)

# Capture Login shells
capture_command_output("cat /etc/profile", output_log_file)
capture_command_output("cat /home/profile.d/*", output_log_file)
capture_command_output("cat /etc/bash.bashrc", output_log_file)
capture_command_output("cat /etc.bash_logout", output_log_file)
capture_command_output("cat /home/$USER/.bashrc", output_log_file)
capture_command_output("cat /home/$USER/.bashr_profile", output_log_file)

# Capture SSH Daemon
capture_command_output("cat /lib/systemd/system/ssh.service", output_log_file)
capture_command_output("cat /etc/ssh/sshd_config", output_log_file)
capture_command_output("ls ~/.ssh/rc", output_log_file)
capture_command_output("ls /etc/ssh/sshrc", output_log_file)

# Capture Services and systemd
capture_command_output("ls /etc/systemd/system/", output_log_file)

# Capture running processes
capture_command_output("ps aux", output_log_file)
capture_command_output("top -b -n 1 | head -20", output_log_file)
capture_command_output("uptime", output_log_file)

print(f"Evidence collected! Check {output_log_file} for details.")
