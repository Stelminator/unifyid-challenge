from Crypto.PublicKey import RSA

import bits


random_org = bits.RandomOrg()

#I thought about doing a generator or a global,
#but, a callable class seemed simpler
class ByteGen(object):
    #misspelled to not conflict with builtin 'bytes'
    bites = random_org.get_bytes_from_local()

    def __init__(self):
        self.i = 0

    def __call__(self, N):
        retval = self.bites[self.i:self.i+N]
        self.i += N
        #print self.i, N
        return retval

byte_gen = ByteGen()

key = RSA.generate(1024, byte_gen)
pubkey = key.publickey()

with open('key.priv', 'wb') as f:
    f.write(key.exportKey(passphrase='unifyid'))

with open('key.pub', 'wb') as f:
    f.write(pubkey.exportKey())
