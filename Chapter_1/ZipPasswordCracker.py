import zipfile
from threading import Thread

zipFile = '/home/brains/evil.zip'
dictFile = '/home/brains/dictionary.txt'


def extract(password):
    try:
        zFile = zipfile.ZipFile(zipFile)
        zFile.extractall(pwd=password.encode(), path='')
        print("[+] Password Found {}".format(password))
    except:
        return False


def main():
    with open(dictFile, 'r') as file:
        for word in file:
            word = word.strip('\n')
            t = Thread(target=extract, args=(word,))
            t.start()

if __name__ == '__main__':
    main()