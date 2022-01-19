import os
import hash
import encryption
import ipfs
import ldap

if __name__ == "__main__":
    in_filename = input("Enter the input file name: ")
    iv = b'TestMeInitVector'

    filesize = os.path.getsize(in_filename)
    
    AES_key = hash.SHA256(in_filename)
        
    encryption.encrypt_aes(AES_key, iv, in_filename, filesize)

    ipfs = ipfs.IPFS("127.0.0.1", "5001")

    #mettre dans ipfs le doc chiffré + calculer hash du doc chiffré

    ipfs.addDoc(in_filename.split(".")[-2]+".crypt")

    hash_doc_encrypted = hash.SHA256(in_filename.split(".")[-2]+".crypt")

    encryption.decrypt_aes(AES_key, iv, in_filename)

    l = ldap.initialize('ldap://localhost:1390')

    ldap.add("ou=documents, dc=nodomain")



