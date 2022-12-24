# Ransomware Reverse Shell Socket Session Manager
#### Warning: This program was developed for educational purposes only. It has the capability to encrypt files and entire directories on a computer. Use caution #### when using this program and do not use it on your own computer.

This program is designed to implement a reverse shell and give the attacker the ability to run all CMD and Unix commands, as well as encrypt files and directories using AES encryption. The communication between the client and the server is completely encrypted using RSA encryption to exchange symmetric keys, which are then used to establish an AES-encrypted session.

## Features
- Reverse shell functionality allows the attacker to run commands on the victim's computer
- AES encryption for secure communication between client and server
- RSA encryption for exchanging symmetric keys
- Ransomware functionality using AES encryption to encrypt files and directories
- Folder encryption is done recursively, meaning all files and subfolders within the selected directory will be encrypted
Usage
- To use the ransomware functionality, you can use the -help command to see examples of how to encrypt files and directories.

### Detection and evasion
This program is designed to not be detected or blocked by any antivirus or endpoint detection and response (EDR) software. However, as with any potentially malicious software, use caution when deploying and using this program.

## Disclaimer
This program was developed for educational purposes only. The authors do not endorse or condone the use of this program for any illegal or malicious activities. Use at your own risk.
