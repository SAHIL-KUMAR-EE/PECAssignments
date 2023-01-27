print("Question 1")

string1 = input("Enter a string :: ")

print(string1[::-1])



print("Question 2")

start = int(input("Enter range starting :: "))

end = int(input("Enter range ending :: "))

numb = int(input("By which number do you want to check divisibility :: "))

for i in range(start,end):
	
	if i % numb == 0:
		
		print(i)
		


print("Question 3")

a = float(input("Enter length of first side :: "))

b = float(input("Enter length of second side :: "))

c = float(input("Enter length of third side :: "))

if ((a + b) <= c) or ((b + c) <= a) or ((c + a) <= b):
	
	print("Triangle is not possible as sum of two sides is lesser than the third side.")

else:
	
	s = (a + b + c)/2
	
	area = (s*(s - a)*(s - b)*(s - c)) ** (0.5)
	
	print("Area is %.2f" % area)
	
	
	
print("Question 4")

n = int(input("Enter width of triangle :: "))

for i in range(1,n+1):
	
	print("*"*i)
	
for i in range(n+1,2*n):
	
	print("*"*((2*n)-i))



print("Question 5")

row = int(input("Enter number of rows :: "))

start = 65

for i in range(row):
	
	for j in range(0,i+1):
		
		print(chr(start),end="")
		if start < 90:
			start += 1
		else:
			start = 65
		
	print("")
	
	
print("Question 6")

start = int(input("Enter start of range :: "))

end = int(input("Enter end of range :: "))

for i in range(start,end+1):
	
	for j in range(2,i):
		
		if i % j == 0:
			
			break
	
	else:
			
		print(i)
		

print("Question 7")

for i in range(1,501):
			
	if (i % 7 == 0) and (i % 11 == 0):
			
			print(i)
			

print("Question 8")

print("Input 10 integers")

lis = []

for i in range(10):
			
	x = int(input())
	
	lis.append(x)
		
print("Positive Numbers")
for i in lis:
	if i > 0:
		print(i)
		
print("Negative Numbers")
for i in lis:
	if i < 0:
		print(i)

print("Odd Numbers")
for i in lis:
	if (i % 2) != 0:
		print(i)

print("Even Numbers")
for i in lis:
	if (i % 2) == 0:
		print(i)
		
#To remove duplicates		
set1 = set(lis)

print("Number : Occurences")
for i in set1:
	print(lis.count(i))				
print("Question 9")

print("Enter a list of words")

lis2 = eval(input("Enter list with square brackets"))

set2 = set(lis2)

print("Word : Occurence")

for i in set2:
	print(i,lis2.count(i))					
						
