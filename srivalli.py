x = int(input())
if (x%4 == 0):
	if(x%100 == 0):
		if(x%400 == 0):
			print("Yes")
		else:
			print("No")
	else:
		print("Yes")
else:
	print("No")	
		
	
