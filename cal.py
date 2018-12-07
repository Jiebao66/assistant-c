diff  = ['simple_data.in','middle_data.in','hard_data.in']
wtff = ['out/simple_data.out','out/middle_data.out','out/hard_data.out']
for i in range(len(diff)):
    diff[i] = 'in/'+diff[i]    
num = int(input("input difficulty:"))
fr = open(diff[num],'r')
fw = open(wtff[num],'w')
for line in fr:
    try:
        ans = str(eval(line)) 
    except ZeroDivisionError:
        ans = 'error'
    fw.write(ans+'\n')


