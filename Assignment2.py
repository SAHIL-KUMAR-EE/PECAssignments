print("Question 1")
#(a)
x = "Python is a case sensitive language"
 
print("Length",len(x))
 
#(b)
print(x[::-1])
 
#(c)
s = slice(10,26)
 
print(x[s])
 
#(d)
x1 = x.replace("a case sensitive","object oriented")
 
print(x1)
 
#(e)
print(x.index("a"))
 
#(f)
x2 = x.replace(" ","")
 
print(x2)
 
print("\nQuestion 2")
 
name = input("Enter Name ")
sid = int(input("Enter SID "))
dept = input("Enter Department Name ")
cgpa = float(input("Enter CGPA "))
 
print("Hey, %s Here !" % name)
 
print("My SID is %d" % sid)
 
print("I am from %s department and my CGPA is %2.1f" % (dept,cgpa))
 
print("\nQuestion 3")
 
a = 56
b = 10
 
print(a & b)
print(a | b)
print(a ^ b)
print(a << 2, b << 2)
print(a >> 2, b >> 4)
 
print("\nQuestion 4")
 
num1 = int(input("Enter First Number "))
 
num2 = int(input("Enter Second Number "))
 
num3 = int(input("Enter Third Number "))
 
print("Greatest Number",max(num1,num2,num3))
 
print("\nQuestion 5")
 
if "name" in x:
 
	print("YES")
 
else:
 
	print("NO")
 
print("\nQuestion 6")
 
s1 = int(input("Enter First Side "))
 
s2 = int(input("Enter Second Side "))
 
s3 = int(input("Enter Third Side "))
 
if (s1 + s2 >= s3) and (s2 + s3 >= s1) and (s1 + s3 >= s2):
 
	print("YES")
 
else:
 
	print("NO")
