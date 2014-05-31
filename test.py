print	'{0}{1}{2}{3}{4}'.format('0)Dromos?\n','1)podhlato?\n','2)Droseros aeras?\n','3)paralia\n','4)THalassa??? \n')
sum=0
r='dwse treis epiloges !!! Me prosoxh'
print r
w=1
for t in range(0,3):
	print' epilogh %d'%(w)
	w=w+1
	x=raw_input('dwse epilogh:')
	x=int(x)
	if x==0:
		s='kalh h pathsiwn'
		print s
		y=1;
	elif  x==1:
		s='2 rodes!!!'
		print s
		y=2
	elif x==2:
		s='thes to diaforetiko'
		print s
		y=3
	elif x==3:
		s='eisai etoimos gia to nhsi'
		print s
		y=4
	elif x==4:
		s='eishthria/ploio'
		print s
		y=5;
	else:
		s='eisai tharaleos'
		print s
		y=0
	sum=sum+y
if sum>12:
	p='PETYXES thes diakopes\n'
	print p
else:
	p='DYSTYXWS antexeis akoma\n'
	print p
	


print "change to change"

