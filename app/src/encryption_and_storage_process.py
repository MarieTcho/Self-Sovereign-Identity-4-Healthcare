import os
import hash
import encryption
import ipfs
from ldap3 import Server, Connection, ALL, SAFE_SYNC, ALL_ATTRIBUTES

def encryptstore(x,y):
    uid = x
    in_filename = y

    iv = b'TestMeInitVector'

    filesize = os.path.getsize(in_filename)
    
    AES_key = hash.SHA256(in_filename)
        
    encryption.encrypt_aes(AES_key, iv, in_filename, filesize)

    ipfs = ipfs.IPFS("127.0.0.1", "5001")

    #mettre dans ipfs le doc chiffré + calculer hash du doc chiffré

    ipfs.addDoc(in_filename.split(".")[-2]+".crypt")

    hash_doc_encrypted = hash.HSHA256(in_filename.split(".")[-2]+".crypt")

    encryption.decrypt_aes(AES_key, iv, in_filename)

    server = Server('ldap://localhost:389', get_info=ALL)

    print("*" * 100)
    print(hash_doc_encrypted)

    conn = Connection(server, 'cn=admin,dc=nodomain', 'ldap', auto_bind=True, client_strategy=SAFE_SYNC)
    # print(conn.search('ou=patients,dc=nodomain', '(sn=Marie)', attributes=ALL_ATTRIBUTES))
    # print(conn.search('ou=documents,dc=nodomain', '(documentAuthor=uid=0x9EdF6CCAFE620a14fB83531f5a6Fd3673F7BC39a,ou=patients,dc=nodomain)', attributes=ALL_ATTRIBUTES))

    # conn.add(f"documentIdentifier={hash_doc_encrypted},ou=documents,dc=nodomain", "document", {"documentAuthor": "uid="+uid+",ou=patients,dc=nodomain"}))
    # l.add_s("ou=documents, dc=nodomain", [("documentIdentifier", hash_doc_encrypted), ("documentAuthor", b"uid=0x9EdF6CCAFE620a14fB83531f5a6Fd3673F7BC39a,ou=patients,dc=nodomain")])

	

