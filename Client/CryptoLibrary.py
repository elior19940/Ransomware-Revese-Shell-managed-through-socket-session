import Cryptodome
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from cryptography.fernet import Fernet
import base64
import hashlib
import os
import pathlib

class AES_encryption(object):

    def __init__(self,key):
        self.key=key
        iv = hashlib.md5(key).digest()
        self.cipher=AES.new(key, AES.MODE_CBC, iv)

    def pad_data(self,data):
        return data + bytes(len(data)%16) + bytes([len(data)%16])

    def encrypt_data_aes(self,data):
        return base64.b64encode(self.cipher.encrypt(pad(data,AES.block_size)))

    def decrypt_data_aes(self,data):
        return unpad(self.cipher.decrypt(base64.b64decode(data)),AES.block_size)
    

    def encryptFile(self,path):
        assert(os.path.getsize(path)) < 25000000
        try:
            data = self.encrypt_data_aes(open(path,'rb').read())
            open(path,'wb').write(data)
            return True
        except:
            return False

        
    def decryptFile(self,path):
        try:
            data = self.decrypt_data_aes(open(path,'rb').read())
            open(path,'wb').write(data)
            return True
        except:
            return False
            pass
        
    def encryptDir(self,path):
        files = [i for i in pathlib.Path(path).rglob("*") if os.path.isfile(i)]
        e = False
        for i in files:
            try:
                self.encryptFile(i)
                e = True
            except:
                pass
        if e:
            return True
        return False
            
    def decryptDir(self,path):
        files = [i for i in pathlib.Path(path).rglob("*") if os.path.isfile(i)]
        e = False
        for i in files:
            try:
                self.decryptFile(i)
                e = True
            except:
                pass
        if e:
            return True
        return False
      
      
      
class RSA_encryption(object):
        
    def generet_rsa_keys(self,bytes_length):
        key=RSA.generate(bytes_length)
        public=key.public_key()
        return [key.export_key('PEM'),public.export_key('PEM')]

    def import_rsa_private_key(self,private_pem):
        return RSA.import_key(private_pem)

    def import_rsa_public_key(self,public_pem):
        return RSA.import_key(public_pem).public_key()

    def rsa_encryt(self,public,data):
        if type(public)!=Cryptodome.PublicKey.RSA.RsaKey:
            public=self.import_rsa_private_key(public)
        cipher=PKCS1_OAEP.new(public)
        return cipher.encrypt(data)

    def rsa_decrypt(self,private,data):
        if type(private)!=Cryptodome.PublicKey.RSA.RsaKey:
            private=self.import_rsa_private_key(private)
        cipher=PKCS1_OAEP.new(private)
        return cipher.decrypt(data)

    
class Encryption():
    
    def __init__(self,key=False):
        if key != False:
            self.fer = Fernet(key)
            
    def encrypt(self,message):
        return self.fer.encrypt(message)
    
    def decrypt(self,data):
        return self.fer.decrypt(data)
    
    def genKey(self):
        return base64.b64encode(os.urandom(32))
      
      
      
