#!/usr/bin/python3

from Crypto.Cipher import AES
from optparse import OptionParser
import sys
import os


def encrypt(plainte_text):
    a='C'*32
    en=AES.new(key=a)
    if len(plainte_text)>=32:
        plainte_text+=int(32-int(len(plainte_text)%32))*'A'
        return en.encrypt(plainte_text)
    elif len(plainte_text)<32:
        plainte_text+=int(32-len(plainte_text))*'A'
        return en.encrypt(plainte_text)

def decode(ciphertext_text):
    a='C'*32
    de=AES.new(key=a)
    plainte_text=de.decrypt(ciphertext_text)
    return plainte_text.decode().strip('A')

def main():
    parser=OptionParser()
    parser.add_option('-e','--encrypt',action='store',type='string',dest='encrypt')
    parser.add_option('-d', '--decode', action='store', type='string', dest='decode')
    (options,args)=parser.parse_args()
    if options.encrypt:
        for path in os.walk('./'):
            if not path[0].endswith('/'):
                dir_path=path[0]+'/'
            else:
                dir_path=path[0]
            for i in path[2]:
                if i.endswith('.py') and 'encrypt_and_decode.py' != i:
                    ciphertext=encrypt(open(str(dir_path + i), 'r+').read())
                    f = open(str(dir_path + i),'wb+')
                    f.write(ciphertext)
                    f.close()
        sys.exit()
    if options.decode:
        for path in os.walk('./'):
            if not path[0].endswith('/'):
                dir_path = path[0] + '/'
            else:
                dir_path = path[0]
            for i in path[2]:
                if i.endswith('.py') and  'encrypt_and_decode.py' != i:
                    plainte=decode(open(str(dir_path + i), 'rb+').read())
                    f = open(str(dir_path + i), 'w+')
                    f.write(plainte)
                    f.close()
        sys.exit()

if __name__ == '__main__':
    main()