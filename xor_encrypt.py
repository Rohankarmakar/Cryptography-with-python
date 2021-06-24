'''
Name : Rohan Karmakar; Dept.: ECE; ROLL No.: 34900319031; Year: 2nd
'''
import os

def xorCrypto(fileName, key):
    with open(fileName, 'rb') as f:
        data = f.read()
        f.close()
    
    data = bytearray(data)
    for i, val in enumerate(data):
        data[i] = val ^ key

    if fileName.find('enc_') == 0:
        new_fileName = fileName.replace('enc_', '')
        os.remove(fileName)
    else:
        new_fileName = 'enc_'+fileName
    
    with open(new_fileName, 'wb') as fw:
        fw.write(data)
        fw.close()
    print("Done.")

if __name__ == '__main__':
    key = int(input('Enter the byte key : '))
    fileName = input('Enter the file name : ')
    choice = input('''
    1. For encryption enter 1 
    2. For decryption enter 2
    3. For Quit enter 3 \n''')
    if choice == '1':
        xorCrypto(fileName, key)
    elif choice == '2':
        xorCrypto(fileName, key)
    else:
        exit()
