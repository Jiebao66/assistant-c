gfr  = ['in/simple_data.in','in/middle_data.in','in/hard_data.in']
gfw1 = ['out/int/simple_data.out','out/int/middle_data.out','out/int/hard_data.out']
gfw2 = ['out/float/simple_data.out','out/float/middle_data.out','out/float/hard_data.out']

def cal(fr,fw):
    for line in fr:
        ans = str(eval(line)) 
        fw.write(ans+'\n')

def main():
    for i in range(3):
        fr = open(gfr[i],'r')
        fw = open(gfw2[i],'w')
        cal(fr,fw)
        fr.close()
        fw.close()


if __name__ == '__main__':
    main()