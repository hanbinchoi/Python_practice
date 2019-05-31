key=input().split()
value=map(float,input().split()) #리스트 값들을 float값으로 맵핑함
dictA=dict(zip(key,value)) #리스트 2개를 키 와 밸류의 형태로 딕셔너리 저장
print(dictA)
