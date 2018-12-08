gfr  = ['in/simple_data.in','in/middle_data.in','in/hard_data.in']
gfw = ['out/simple_data.out','out/middle_data.out','out/hard_data.out']

def cal(fr,fw):
    for line in fr:
        ans = str(eval(line)) 
        fw.write(ans+'\n')

def main():
    for i in range(3):
        fr = open(gfr[i],'r')
        fw = open(gfw[i],'w')
        cal(fr,fw)
        fr.close()
        fw.close()


if __name__ == '__main__':
    main()