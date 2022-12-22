print("Question1")
a = int(input("Enter First Number "))
b = int(input("Enter Second Number "))
c = int(input("Enter Third Number "))
d = (a+b+c)/3
print(round(d,5))
 
print("\nQuestion2")
gross = round(float(input("Enter Gross Income ")),2)
 
dependents = int(input("Enter no. of dependents "))
 
standard = 10000
taxable = gross - standard - (3000 * dependents)
tax = taxable * 0.2
print("Your tax is ",tax) 
 
print("\nQuestion3")
number = int(input("Enter Seconds "))
 
minutes = number // 60
 
seconds = number % 60
 
print("No. of minutes ",minutes)
 
print("No. of seconds ",seconds)
 
print("\nQuestion4")
answer = 25 + int('25') + int(25.0)
 
print(answer)
 
print("\nQuestion5")
import math
 
for i in range(0,350,15):
	angle = math.radians(i)
 
	sin_answer = math.sin(angle)
 
	cos_answer = math.cos(angle)
 
	print("%d --- %.4f %.4f" % (i,sin_answer,cos_answer))
