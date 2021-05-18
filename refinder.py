

goalnumber = input('What number are you trying to find? ')
goalnumber = int(goalnumber)


sevenarray = []
fivearray = []

for x in range (0,200):
	sevenarray.append(7*x)
	fivearray.append(15*x)
	x += 1
	
for x in range (0,200):
    for y in range (0,200):
        if ((sevenarray[x] + fivearray[y]) == goalnumber):
            print('The Values you want are: ' + '7:' + str(x) + ' 15:' + str(y)) 
	
