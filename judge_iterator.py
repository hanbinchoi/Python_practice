class TimeIterator:

    timeList=[]
    def __init__(self,start,stop):
        self.start=start
        
        self.k=0
        self.stop=stop
        self.hour=self.start//3600
        if self.hour>=24:
            self.hour-=24
        self.minute=self.start%3600//60
        self.second=self.start%3600%60
        self.time=str(self.hour).zfill(2)+':'+str(self.minute).zfill(2)+':'+str(self.second).zfill(2)
        

    def __iter__(self):
        return self

    def __next__(self):
        if self.start<self.stop:
               
            self.hour=self.start//3600
            self.minute=self.start%3600//60
            self.second=self.start%3600%60
            if self.hour>=24:
                self.hour-=24
            self.start+=1
            self.time=str(self.hour).zfill(2)+':'+str(self.minute).zfill(2)+':'+str(self.second).zfill(2)
            self.timeList.append(self.time)
            
            return self.time 
        else:
            raise StopIteration

    def __getitem__(self,index):
        if index<self.stop-self.start:
            print(TimeIterator.timeList)
            return self.timeList[index]
        else:
            raise IndexError

start,stop,index=map(int,input().split())

for i in TimeIterator(start,stop):
    print(i)

print('\n',TimeIterator(start,stop)[index],sep='')

