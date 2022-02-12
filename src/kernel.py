import random

def Draw(totalNum, usedIdxList):  
    if len(usedIdxList) == totalNum:
        raise Exception('All been drawn.')

    availableIdxList = [idx for idx in range(totalNum) if idx not in usedIdxList]
    idx = random.choice(availableIdxList)
    usedIdxList.append(idx)


if __name__ == '__main__':
    usedIdxList = []
    
    itr = 0
    while itr < 5:
        Draw(10, usedIdxList)
        print(usedIdxList)
        itr += 1