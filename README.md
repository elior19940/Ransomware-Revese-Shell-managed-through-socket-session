# Ransomware-Revese-Shell-managed-through-socket-session
Ransomware &amp; Revese Shell managed through socket session

This Program this program was developed only for education usage. 
Warning: The program have the capability to encrypt files and entire directories on the computer.
Be careful when you are using this program! Use it only for education and Do Not use it on your local computer.

The program is developted to implemenent a reverse shell and to give the attacker the ability to run all CMD and Unix commands and also I've added some external commands to encrypt file and directories (Recursively) on the victim computer.

All the comunication between the client and the server is complitly encrypted using RSA encryption to share symmeteric keys between the client and the server in the begging of the session which will be used to complitly encrypt the session using AES algorithm.

The Ransomware also uses AES algorithm to encrypt file and directories.
the folder encryption is done Recursively for each files and folders on the selected directory.
Type -help to get examples of how to use the external commands.
