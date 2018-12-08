esp  =  0.001
f_stu = open('./student_out/t.out')
f_ans = open('../out/hard_data.out')
f_exp = open('../in/hard_data.in')

ok = True

lines_stu = f_stu.readlines()
lines_ans = f_ans.readlines()
lines_exp = f_exp.readlines()
f_stu.close()
f_ans.close()
f_exp.close()


lcnt = min(len(lines_stu),len(lines_ans))

er = []

for i in range(lcnt):

    data1 = float(lines_stu[i][:len(lines_stu[i])-1])
    data2 = float(lines_ans[i][:len(lines_ans[i])-1])
    
    if abs(data2-data1) > esp:
        ok = False
        er.append(i)

if ok == False:
    for i in er:
        print('error%d @ %s'%(i,lines_exp[i]))
else:
    print 'Correct!'


