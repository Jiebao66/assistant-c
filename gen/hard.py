import random
maxInt = 30
minInt = -20
op = ['+','-','*','/']

def getOp():
    return op[random.randint(0,3)]

def getNum():
    x = random.randint(minInt,maxInt)
    if x<0:
        x = '('+str(x)+')'
    elif x==0:
        x = str(x+1)
    else:
        x = str(x)
    return x

def numExp(x):
    maxCnt = 3
    ac = ''
    cnt = random.randint(1,maxCnt)
    for i in range(cnt):
        ac += getNum()+ getOp()
    if x == 0:
        ac = getOp()+ac
    elif x == 1:
        ac = ac[0:len(ac)-1]        
    elif x ==3:
        ac = getOp()+ac[0:len(ac)-1]
    return ac

def bracket():
    maxB = 3
    ac = '('
    maxInt = 3
    lf = 1
    rt = 0
    while lf>=rt:
        if lf>rt:
            bno = random.randint(0,1)
            if bno==0:
                ac += '('
                lf += 1
            else:
                ac += ')'
                rt += 1
        else:
            ac += '('
            lf += 1
        if len(ac)>maxB:
            ac += ')'*(lf-rt)
            return ac

def exp():
    ac = '&'
    bk = '&'+bracket()+'&'
    bk_len = len(bk)
    for i in range(bk_len-1):
        tag = bk[i:i+2]
        if tag == ')(':
            ac += numExp(0)+'('
        elif tag == '()':
            ac += numExp(1)+')'
        elif tag == '((' or tag == '&(':
            ac += numExp(2) + '('
        elif tag == ')&':
            ac += numExp(3)+'&'
        elif tag == '))':
            ac += numExp(3) + ')'
    return ac[1:len(ac)-1]
            

        
def main():
    f = open('../in/hard_data.in','w')
    for i in range(20):
        f.write(exp()+'\n')


if __name__ == '__main__':
    main()