file=open('words.txt','r')
line=file.read()
words=line.split()
j=0
for i in words:
    words[j]=i.strip(',.')
    if 'c' in words[j]:
        print(words[j])
    j+=1

file.close()

