import ipfshttpclient

#http://localhost:8080/ipfs

class IPFS:
    def __init__(self, ip, port) -> None:
        self.api = self.connect(ip, port)
        
    def connect(self, ip=None, port=None):
        """if not ip:
            ip = "127.0.0.1"
        if not port:
            port = "5001"""
        api = ipfshttpclient.connect('/ip4/'+ip+'/tcp/'+port+'/http')
        return api

    def addDoc(self, doc):
        res = self.api.add(doc)
        print(res)
        return res

    def printDoc(self, hash):
        res = self.api.cat(hash)
        print(res)
        return res

"""
if __name__ == '__main__':
    ipfs = IPFS("127.0.0.1", "5001")
    print(ipfs.api)
    ipfs.addDoc("encryption.py")
    print(ipfs.api.id())
    print(ipfs.api.pin.ls(type='all'))
    print(ipfs.api.cat('QmWNidJdGn9cF3xNFC93QmhuJGfG7eEFnF4P31H4Mp5sV8'))
    """
