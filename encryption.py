from ctypes import sizeof
from genericpath import isfile
import hashlib
import os, struct
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


bs = AES.block_size

def hashSHA256(in_filename):
    with open(in_filename, 'rb') as in_file:
        in_file_bytes = in_file.read()
    sha256_hash = hashlib.sha256(in_file_bytes)
    print("HASH : " + sha256_hash.hexdigest())
    return sha256_hash.digest()[:bs]


def encrypt_aes(key, iv, in_filename, filesize):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    with open(in_filename, 'rb') as in_file, open(in_filename.split(".")[-2]+'.crypt', 'wb') as out_file:
        out_file.write(struct.pack('<Q', filesize))
        out_file.write(iv)
        while True:
            chunk = in_file.read(1024 * 64)
            if len(chunk) == 0:
                break
            elif len(chunk) % bs != 0: #final block/chunk is padded before encryption
                padding_length = (bs - len(chunk) % bs) or bs
                chunk += str.encode(padding_length * chr(padding_length))
            out_file.write(cipher.encrypt(chunk))
    print(in_filename + " has been encrypted. See " + in_filename.split(".")[-2] + '.crypt')


def decrypt_aes(key, iv, in_filename):
    with open(in_filename.split(".")[-2]+'.crypt', 'rb') as in_file, open(in_filename.split(".")[-2]+'decrypted.'+in_filename.split(".")[-1], 'wb') as out_file:
        origsize = struct.unpack('<Q', in_file.read(struct.calcsize('Q')))[0]
        iv = in_file.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)
        while True:
            chunk = in_file.read(1024 * 24)
            if len(chunk) == 0:
                break
            out_file.write(decryptor.decrypt(chunk))
            out_file.truncate(origsize)
    print(in_filename.split(".")[-2]+'.crypt' + " has been decrypted. See " + in_filename.split(".")[-2]+'decrypted.'+in_filename.split(".")[-1])



if __name__ == '__main__' : 
    in_filename = input("Enter the input file name: ")
    #in_filename = "AOPC_Presentation_Tcholakian.pdf"
    iv = b'TestMeInitVector'
    filesize = os.path.getsize(in_filename)
        
    AES_key = hashSHA256(in_filename)
        
    encrypt_aes(AES_key, iv, in_filename, filesize)
    
    decrypt_aes(AES_key, iv, in_filename)

    
