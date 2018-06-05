f=open('IDToken2.txt','w')
year=['95','96','97']                 #生成生日弱口令
month=['01','02','03','04','05','06','07','08','09','10','11','12']
for y in year:
    for m in month:
        for d in range(1,32):
            if d<10:
                #print(y+m+'0'+str(d))   
                f.write(y+m+'0'+str(d)+'\n')
            else:
                #print(y+m+str(d))
                f.write(y+m+str(d)+'\n')
f.close()