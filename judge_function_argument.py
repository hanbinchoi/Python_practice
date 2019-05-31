korean,english,mathematics,science=map(int,input().split())

def get_min_max_score(*args):
    return min(args),max(args);

def get_average(korean=0,english=0,mathematics=0,science=0):
    scoreList=[korean,english,mathematics,science]
    count=0
    for i in scoreList:
        if i!=0:
            count+=1
    return sum(scoreList)/count

min_score,max_score=get_min_max_score(korean,english,mathematics,science)
average_score=get_average(korean=korean,english=english,
                          mathematics=mathematics,science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.
      format(min_score,max_score,average_score))

min_score,max_score=get_min_max_score(english,science)
average_score=get_average(english=english,
                          science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.
      format(min_score,max_score,average_score))
