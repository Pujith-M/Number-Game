print '                Hello \n                Welcome To Number Game!'
k=1
while k:
	dest=raw_input("Enter the destination :	\n\n	")
	try:
		dest=int(dest)
		k=0
	except:
		print "Enter proper input!!!!!!!!"
k=1
while k:
	num=raw_input("Enter the number limit that one can tell at a time\n\n 1  < num <  5\n\n")
	try:
		num=int(num)
		k=0
	except:
		print "Enter proper input!!!!!!!!!!!"
k=1
while k:
	print 'Enter 0 if you want System to start the game\nEnter 1 if you want to start the game\n\n'
	c=raw_input()

	try:
		c=int(c)
		k=0
	except:
		print "Enter proper input"
lis=list()
firstnum=dest%(num+1)
while firstnum<=dest:
		lis.append(firstnum)
		firstnum=firstnum+(num+1)
# print lis
firstnum=0
def printnos(firstnum,num,lis):
	temp=0
	firstnum=firstnum+1
	while temp<num:
		print firstnum
		if firstnum in lis:
			# print "break"
			return firstnum
		
		firstnum=firstnum+1
		temp=temp+1
	return firstnum-1
		
def getnos(firstnum,num):
	k=1
	while k:
		print "\nTill now Numbers : ",range(1,firstnum+1), "\n     "
		getno=raw_input("\nEnter next Numers  :\n               ")
		word=getno.split()
		if len(word) <= num:
			if len(word)>0:
				for temp in word:
					try:
						if (firstnum+1) is int(temp):
							k=0
							firstnum=firstnum+1
						else:
							print 'Enter proper input!!!!',
							k=1
							break
					except:
						print 'Enter proper input!!!!'
						k=1
						
						break
	return firstnum
						

						
						
key=1
if not c:
	print '\nSystem is starting the game:'
	firstnum=printnos(firstnum,num,lis)
	key=0
	if firstnum>=dest:
			print 'You lost the game!!!'
			exit()
else:
	firstnum=getnos(firstnum,num)
	if firstnum>=dest:
			print 'You wone the game!!!!!!!'
			exit()
k=1
while k:
	if key:
		key=1
		print '\nNext Numbers are:\n '
		if firstnum in lis:
			firstnum=firstnum+1
			key=1
			print firstnum
		else:
			firstnum=printnos(firstnum,num,lis)
			key=1
			if firstnum>=dest:
				print 'You lost the game!!!'
				break
	firstnum=getnos(firstnum,num)
	key=1
	if firstnum>=dest:
			print 'You wone the game!!!!!!!'
			exit()