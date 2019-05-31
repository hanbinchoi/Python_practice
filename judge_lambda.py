files=input().split()
print(list(map(lambda x: '00'+x[0:x.find('.')]+x[x.find('.'):]
               if len(x[0:x.find('.')])==1
               else '0'+x[0:x.find('.')]+x[x.find('.'):] if len(x[0:x.find('.')])==2
               else x,files)))
