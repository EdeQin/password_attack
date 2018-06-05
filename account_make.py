#f=open('IDToken1.txt','w')
start=[1512480,1511410,1611410]         #调查获得的几种学号开头
start_group=0
for i in range(101,640):
    if int(i/10)%10>3:                  #假设6个班，每班39人
        i=int(i/100+1)*100
    else:
        #f.write(str(start0)+str(i)+'\n')
        print(str(start[0])+str(i))     #生成计算机系几个班的学号
#f.close()