import random

def dataInput(args):
    args=args.split(',')
    return args

def shake(matchList):
    random.shuffle(matchList)
    return matchList



