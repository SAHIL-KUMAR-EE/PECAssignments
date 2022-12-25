print("Question1")

input_string = input("Enter string ")

#If string is a single word only

if " " not in input_string:

    #Remove duplicate letters

    unique = ""

    for i in input_string:

        if i not in unique:

            unique += i

    for j in unique:

        print(j,input_string.count(j))

else:

    unique_words = []

    for k in input_string.split():

        if k not in unique_words:

            unique_words.append(k)

    for x in unique_words:

        print(x,input_string.count(x))
    

print("\nQuestion2")

day = int(input("Day - "))

month = int(input("Month - "))

year = int(input("Year - "))

#Leap Year Check

if year % 400 == 0:

    leap = True

elif year % 100 == 0:

    leap = False

elif year % 4 == 0:

    leap = True

else:

    leap = False

#Finding days in a month

if month in (1,3,5,7,8,10,12):

    month_length = 31

elif month == 2:

    if leap == True:

        month_length = 29

    else:

        month_length = 28

else:

    month_length = 30

#Checking if day is less than month length

if day < month_length:

    day += 1

else:

    day = 1

    if month == 12:

        month = 1

        year += 1

    else:

        month += 1

#Final Output

print("Next Date is: %d/%d/%d"%(day,month,year))


print("\nQuestion3")

list1 = [3,9,10]

output_list = []

for i in list1:

    tmp = (i,i**2)

    output_list.append(tmp)

print(output_list)


print("\nQuestion4")

grade = int(input("Enter Grade "))

results = {10:("A+","Outstanding"),
           9:("A","Excellent"),
           8:("B+","Very Good"),
           7:("B","Good"),
           6:("C+","Average"),
           5:("C","Below Average"),
           4:("D","Poor")}
           
if 4 <= grade <= 10:

    print("Your Grade is %s and %s performance"%(results[grade][0],results[grade][1]))

else:

    print("Error")


print("\nQuestion5")

letters = [chr(i) for i in range(65,76)]

length = len(letters)

spaces = 0

for i in range(6):
	print((" "*spaces) + "".join(letters[0:length]))
	length -= 2
	spaces += 1


print("\nQuestion6")

student_details = {}

while True:

    choice = input("Do you want to enter SID and Name Y for YES / N for NO ")

    if (choice == "N") or (choice == "n"):

        break

    sid = int(input("Enter your SID "))

    name = input("Enter your name ")

    student_details[sid] = name

for i in student_details:

    print(i,student_details[i])

print("Original Dictionary",student_details)

dict_by_names = sorted(student_details.items(),key = lambda i:i[1])

dict_by_sid = sorted(student_details.items(),key = lambda i:i[0])

result_by_name = {key:value for key,value in dict_by_names}

result_by_sid = {key:value for key,value in dict_by_sid}

print("Dictionary sorted by name",result_by_name)

print("Dictionary sorted by SID",result_by_sid)

input_sid = int(input("Enter your SID "))

print("Your name is",student_details[input_sid])


print("\nQuestion7")

def fibo(n):

    if n == 0:

        return 0

    elif n == 1:

        return 1

    else:

        return (fibo(n-2) + fibo(n-1))

total_fibo = int(input("How many Fibonacci numbers do you want? "))

sum_of_fibo = 0

for i in range(total_fibo):

    x = fibo(i)

    print(x)

    sum_of_fibo += x

print("Average is",sum_of_fibo/total_fibo)


print("\nQuestion8")

s1 = {1, 2, 3, 4, 5}

s2 = {2, 4, 6, 8}

s3 = {1, 5, 9, 13, 17}

print('Set 1',s1)
print('Set 2',s2)
print('Set 3',s3)

set_a  = s1 ^ s2
print("Elements in Set1 and Set2 but not in both\n",set_a)

set_b = (s1 ^ s2 ^ s3) - (s1 & s2 & s3)
print("Elements that are in one of three sets only\n",set_b)

set_c = (s1 | s2 | s3) - (s1 ^ s2 ^ s3)
print("Elements that are in two of three sets only\n",set_c)

set_d = set(range(1,11)) - s1
print("Elements with numbers from 1 to 10 but not in Set1\n",set_d)

set_e = set(range(1,11)) - (s1 | s2 | s3)
print("Elements with numbers from 1 to 10 but not in Set1, Set2 and Set3\n",set_e)
