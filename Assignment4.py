print("Question 1")

marks = float(input("Enter your marks :: "))

if 0 <= marks < 25:
	
	grade = "F"
	
elif 25 <= marks < 45:
	
	grade = "E"
	
elif 45 <= marks < 50:
	
	grade = "D"
	
elif 50 <= marks < 60:
	
	grade = "C"
	
elif 60 <= marks < 80:
	
	grade = "B"
	
elif 80 <= marks <= 100:
	
	grade = "A"
	
else:
	
	grade = "Not Defined"
	
	print("Please enter marks between 1 to 100")
	
print("Grade ::",grade)



print("Question 2")

year = int(input("Enter year :: "))

if year % 4 == 0:

	if year % 100 != 0:
		
		leap = True
		
	elif year % 400 == 0:
		
		leap = True
		
	else:
		
		leap = False
			
else:
	
	leap = False
	
#Output

if leap == True:
	
	print("%d is a Leap Year" % year)
	
else:
	
	print("%d is NOT a Leap Year" % year)
	


print("Question 3")

import random

for i in range(1,11):
	
	a = random.randint(1,9)
	
	b = random.randint(1,9)
	
	c = a * b
	
	ans = int(input(("Question %d: %d x %d = ") % (i,a,b)))
	
	if ans == c:
		
		print("Right!")
		
	else:
		
		print("Wrong. The answer is %d" % c)
		
		

print("Question 4")

for i in range(200,0,-1):
	
	if (i % 5 == 2) and (i % 6 == 3) and (i % 7 == 2):
		
		print(i)
