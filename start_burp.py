from functions import TryLogin
import datetime
def main():
	starttime = datetime.datetime.now()
	f1=open('IDToken1.txt')
	count=0
	for line1 in f1.readlines():
		account = line1.strip('\n')  # 调用strip()删除行尾空格
		f2 = open('IDToken2.txt')
		for line2 in f2.readlines():
			password=line2.strip('\n')
			TryLogin.delay(account,password)
			count+=1
			if count%100==0:
				print(count)
			"""if count==1000:
				endtime = datetime.datetime.now()
				print("用"+str((endtime-starttime).seconds)+"秒尝试了"+str(count)+"次")"""
		f2.close()
	f1.close()
main()