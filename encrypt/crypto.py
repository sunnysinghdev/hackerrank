
class Lock:

    def encrypt(self, public_key, msg):
        newMsg = ''
        for c in msg:
            newMsg += chr(ord(c) + public_key)
        return newMsg

    def decrypt(self, private_key, msg):
        newMsg = ''
        for c in msg:
            newMsg += chr(ord(c) - Lock.algo(private_key))
        return newMsg
    def get_public_key(self, private_key):
        return Lock.algo(private_key)

    @staticmethod
    def algo(private_key):
        return 5 * private_key

e = Lock()
private_key = 50
pub_key  = e.get_public_key(private_key)
print(str(pub_key))
eMsg = e.encrypt(pub_key,'HELLO')
print(eMsg)
dMsg = e.decrypt(private_key, eMsg)
print(dMsg)