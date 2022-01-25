import os
import hash
import encryption
import sys
import ipfs
from flask import Flask, request
from ldap3 import Server, Connection, ALL, SAFE_SYNC, ALL_ATTRIBUTES

app = Flask(__name__)
@app.route("/encryptstore", methods=['GET', 'POST'])

def encryptstore():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./temp.bin') # DANGER !!!!!

    uid = request.form['uid']
    in_filename = os.path.realpath('./temp.bin')
    iv = b'TestMeInitVector'

    filesize = os.path.getsize(in_filename)
    
    AES_key = hash.SHA256(in_filename)
        
    encryption.encrypt_aes(AES_key.digest(), iv, in_filename, filesize)

    ipfsapi = ipfs.IPFS("127.0.0.1", "5001")

    CID = ipfsapi.addDoc(in_filename.split(".")[-2]+".crypt")

    hash_doc_encrypted = hash.SHA256(in_filename.split(".")[-2]+".crypt").hexdigest()

    encryption.decrypt_aes(AES_key.digest(), iv, in_filename)

    server = Server('ldap://localhost:389', get_info=ALL)

    print("*" * 100)
    print("Patient DID : "+ uid + "\nEncrypted document : " + in_filename.split(".")[-2] + ".crypt \nHASH : " + hash_doc_encrypted + "\nCID : " + CID)

    #connect to the LDAP local server

    conn = Connection(server,'cn=admin,dc=nodomain','ldap',auto_bind=True,client_strategy=SAFE_SYNC)
    conn.add('ou=documents,dc=nodomain', 'document', {'documentIdentifier': hash_doc_encrypted, 'documentAuthor': uid})


    #conn.add('ou=documents,dc=nodomain',[("documentIdentifier","5bdce32e97b7ab121dbe39244825d9482a4664d258678bc5166d413ac4b1058f"),("documentAuthor",b"uid=0x9EdF6CCAFE620a14fB83531f5a6Fd3673F7BC39a,ou=patients,dc=nodomain")])
    #initially it was conn.add_s for synchronous
    #conn.add(f"documentIdentifier={hash_doc_encrypted},ou=documents,dc=nodomain", "document", {"documentAuthor": "uid="+uid+",ou=patients,dc=nodomain"})

    # print(conn.search('ou=patients,dc=nodomain', '(sn=Marie)', attributes=ALL_ATTRIBUTES))
    # print(conn.search('ou=documents,dc=nodomain', '(documentAuthor=uid=0x9EdF6CCAFE620a14fB83531f5a6Fd3673F7BC39a,ou=patients,dc=nodomain)', attributes=ALL_ATTRIBUTES))

    return "<html><head></head><body><p>Medical data well uploaded</p></body>"