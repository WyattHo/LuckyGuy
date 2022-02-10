import random

def Draw(totalNum, usedIdxList):  
    if len(usedIdxList) == totalNum:
        raise Exception('All been drawn.')

    pick = True
    while pick:
        idx = random.randint(0, totalNum-1)

        if idx not in usedIdxList:
            pick = False
        else:
            pick = True

    usedIdxList.append(idx)


if __name__ == '__main__':
    usedIdxList = []
    
    Draw(10, usedIdxList)
    print(usedIdxList)
    
    Draw(10, usedIdxList)
    print(usedIdxList)
    
    Draw(10, usedIdxList)
    print(usedIdxList)
    
    Draw(10, usedIdxList)
    print(usedIdxList)
    
    Draw(10, usedIdxList)
    print(usedIdxList)