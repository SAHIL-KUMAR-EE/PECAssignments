print('Question 1\n')

def perfect_chk(num1):

    sum1 = 0

    for i in range(1,num1):

        if num1 % i == 0:

            sum1 += i

    if sum1 == num1:

        print(num1,"is a perfect number.")

    else:

        print(num1,"is NOT a perfect number.")
    
    

num1 = int(input("Enter a number :: "))

perfect_chk(num1)



print('Question 2\n')

def palindrome_chk(str1):

    if str1[::-1] == str1:

        print(str1,"is a Palindrome.")

    else:

        print(str1,"is NOT a Palindrome.")

str1 = input("Enter a string :: ")

palindrome_chk(str1)
    
print('Question 3\n')

def pascal_triangle(n):
    
    for i in range(n):
        
        row = [1]
        
        for j in range(1, i + 1):
            row.append(row[j - 1] * (i - j + 1) // j)
            
        print(' '.join(str(x) for x in row))

n = int(input("Enter the number of rows: "))

pascal_triangle(n)



print('Question 4\n')

def panagram_chk(str2):

    str2 = str2.upper()

    alphabets = [chr(x) for x in range(65,91)]

    for letter in alphabets:

        if letter not in str2:

            break

    else:

        print("The given sentence is a panagram.")
        
str2 = input("Enter a sentence :: ")

panagram_chk(str2)



print('Question 5\n')

def sorted_hypen(x):

    words = x.split("-")

    words.sort()

    print("-".join(words))

sequence = input("Enter hyphen-separated sequence")

sorted_hypen(sequence)


print('Question 6\n')

def student_data(stud_id, stud_name=None, stud_class=None):
    
    print("Student ID:", stud_id)
    
    if stud_name != None:
        print("Student Name:", stud_name)
        
    if stud_class != None:
        print("Student Class:", stud_class)
        
student_data(stud_id = 22101001, stud_name = "ABC", stud_class = 12)

print('Question 7\n')

class Student:
    pass

class Marks:
    pass

#Checking if name is instance of Students class

stud_1 = Student()
stud_2 = Student()
mrks_1 = Marks()
mrks_2 = Marks()

print(isinstance(stud_1, Student))

print(isinstance(stud_2, Student))

print(isinstance(mrks_1, Marks))

print(isinstance(mrks_2, Marks))

print(issubclass(Student, object))

print(issubclass(Marks, object))


print('Question 8\n')

def find_triplets(arr):
    triplets = []
    arr.sort()
    n = len(arr)
    for i in range(n-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        l = i + 1
        r = n - 1
        while l < r:
            s = arr[i] + arr[l] + arr[r]
            if s == 0:
                triplets.append([arr[i], arr[l], arr[r]])
                l += 1
                r -= 1
                while l < r and arr[l] == arr[l-1]:
                    l += 1
                while l < r and arr[r] == arr[r+1]:
                    r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return triplets

input_arr = eval(input("Enter an array :: "))

print(find_triplets(input_arr))

print('Question 9\n')

def check_validity(s):
    
    stack = []
    
    for char in s:
        
        if char in "([{":
            
            stack.append(char)
            
        elif char in ")]}":
            
            if not stack:
                return False
            if char == ")" and stack[-1] != "(":
                return False
            if char == "]" and stack[-1] != "[":
                return False
            if char == "}" and stack[-1] != "{":
                return False
            stack.pop()
            
    return not stack

s = input("Enter a string of parentheses to check its validity: ")

print(check_validity(s))
