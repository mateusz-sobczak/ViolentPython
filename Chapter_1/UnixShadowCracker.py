import crypt

shadowFile = '/home/brains/shadow'
dictFile = '/home/brains/dictionary.txt'


def testPass(cryptPass):
    salt = cryptPass.split('$')[1:3]
    with open(dictFile, 'r') as file:
        for line in file:
            word = line.strip('\n')
            try:
                cryptWord = crypt.crypt(word, '$' + salt[0] + '$' + salt[1] + '$')
            except:
                break
            if (cryptPass == cryptWord):
                print('[+] Found Password: {}'.format(word))
                return
        print('[-] Password Not Found')


def main():
    with open(shadowFile, 'r') as file:
        for line in file:
            if ':' in line:
                user, cryptPass = line.split(':')[0], line.split(':')[1]
                print('[*] Cracking Password For: {}'.format(user))
                testPass(cryptPass.strip('\n'))
            else:
                print('Not A shadow file')


if __name__ == '__main__':
    main()