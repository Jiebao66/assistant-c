gfr  = ['data/in/simple_data.in','data/in/middle_data.in','data/in/hard_data.in']
gfw1 = ['data/out/int/simple_data.out','data/out/int/middle_data.out','data/out/int/hard_data.out']
gfw2 = ['data/out/float/simple_data.out','data/out/float/middle_data.out','data/out/float/hard_data.out']

def cal(fr,fw):
    for line in fr:
        ans = str(eval(line))+' = '+line
        fw.write(ans)

def main():
    for i in range(3):
        fr = open(gfr[i],'r')
        fw = open(gfw2[i],'w')
        cal(fr,fw)
        fr.close()
        fw.close()


if __name__ == '__main__':
    main()