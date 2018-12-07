
import random
f = open('../in/middle_data.in','w')
test_group = 10
maxint = 30
minInt = -10
test_len = 20
op = ['+','-','*','/']
while test_group>0:
    data = ''
    for i in range(random.randint(3,test_len)):
        num = random.randint(minInt,maxint)
        if num <0:
            num = '('+str(num)+')'
        elif num ==0:
            num = str(num+1)
        else:
            num = str(num)
        data += num+op[random.randint(0,3)]
    data += str(random.randint(1,maxint))
    f.write(data+'\n')
    test_group -= 1