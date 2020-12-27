import string

word1 = input('MASUKKAN TEKS : ')
count = 2
word2 = ''
for i in range(len(word1)):
    char = word1[i]
    if(char.isupper()):
        word2 = word2 + chr((ord(char)+ count - 65)%26+65)
    else:
        word2 = word2 + chr((ord(char)+ count - 97)%26+97)

print("TEKS BARU:", word2)

word3 = ''
for i in range(len(word2)):
    char = word2[i]
    if(char.isupper()):
        word3 +=chr((ord(char) - count - 65)%26 + 65)
    else:
        word3 +=chr((ord(char) - count - 97)%26 + 97)

print("TEKS ASAL:", word3)
