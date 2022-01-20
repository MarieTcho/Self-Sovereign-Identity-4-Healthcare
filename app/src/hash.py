
import hashlib

def SHA256(in_filename):
    with open(in_filename, 'rb') as in_file:
        in_file_bytes = in_file.read()
    sha256_hash = hashlib.sha256(in_file_bytes)
    #print("HASH : " + sha256_hash.hexdigest())
    return sha256_hash