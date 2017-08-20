import hashlib


def gen_hash(string):
    if type(string) is str:
        return hashlib.md5(str.encode(string))
    else:
        raise Exception("Not a string")

string = 'ECSC'
while True:
    hash = gen_hash(string)
    # print(hash.hexdigest())
    if hash.hexdigest() == 'c89aa2ffb9edcc6604005196b5f0e0e4':
        print('Found original {} hashes to {}'.format(string, hash.hexdigest()))
        exit(0)
    else:
        string = hash.hexdigest()

# 6c6453c96fb1e472ba6cc14f5c24ce9c