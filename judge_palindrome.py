file=open('words.txt','r')
words=file.readlines()
j=0
for i in words:
    words[j]=i.strip('\n')
    
    if words[j]==words[j][::-1]:
        print(words[j])
    j+=1
file.close()
