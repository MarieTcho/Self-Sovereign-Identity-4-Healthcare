import ipfshttpclient

class IPFS:
    def __init__(self, ip=None, port=None):
        self.ip = ip
        self.port = port
        self.api = self.connect(ip, port)
        
    def connect(self, ip=None, port=None):
        api = ipfshttpclient.connect('/ip4/'+ip+'/tcp/'+port+'/http')
        return api

    def addDoc(self, doc):
        res = self.api.add(doc)    
        return res['Hash']

    def printDoc(self, hash):
        res = self.api.cat(hash)
        print(res)
        return res