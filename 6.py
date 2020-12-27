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

print("new teks is:", word2)

               
               
