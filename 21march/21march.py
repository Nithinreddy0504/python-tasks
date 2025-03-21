# A. EASY QUESTIONS

# 1) write a program to check if a given number is positive, negative or zero
integer = int(input("Enter a number: "))
if integer >0:
    print("positive")
else :
    if integer == 0:
        print("0")
    else:
        if integer == -1:
            print("minus one")
        else:
          print("negative")


# -------------------------------------------------------------------------------------------------------------------------------------------

# 2) determine if a number is odd or even.
i = int(input('Enter a number: '))
if i%2 == 0:
    print('even')
else:
    print('odd')

# ------------------------------------------------------------------------------------------------------------------------------

# 3)  write a program to find a greatest of two numbers
a=int(input("enter a number1:"))
b=int(input("enter a number2:"))
if a>=b:
    print(a,"is larger")
else:
    print(b,"is larger")

# ------------------------------------------------------------------------------------------------------------------------------------------



# 4) Write a program to find the greater number between two numbers.

num1 = input("Enter a number1: ")
num2 = input("Enter a number2: ")
if  num1 > num2:
    print("Number1 is greater",num1)
else:
    print("Number2 is greater",num2)

# -------------------------------------------------------------------------------------------------
# 5) print pass if student scores more than 40 marks, otherwisw print fail.
marks = int(input("Enter your marks: "))
if marks > 40:
    print("pass")
else:
    print("fail")

# ------------------------------------------------------------------------------------------------- 
# 6)  write a programme  to display the day of the week based on a number input (1 for monday, 2 for tuesday, etc)
day =int(input("enter a number: "))
if day==1:
    print("monday")
elif day==2:
    print("tuesday")
elif day==3:    
    print("wednesday")
elif day==4:
    print("thursday")
elif day==5:
    print("friday")
elif day==6:
    print("saturday")
elif day==7:
    print("sunday")
else:
    print("invalid input")
# -------------------------------------------------------------------------------------------------
# 7) implement a simple calculator to perform addition, substraction, multiplication, and division

num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
op = input("enter operator").lower()
if op in ['add', '+']:
   print(num1+num2)
elif op in ['sub', '-']:
   print("num1-num2")
elif op in ['mul','*']:
   print("num1*num2")
elif op in ['div', '/']:
    if num2 != 0 :
        print("num1/num2")
    else:
        print("division by zero is not possible")
else:
    print("invalid input")
        


        
 

# ------------------------------------------------------------------------------------------------------------
# 8) write a programme to display the name of the month based on a number input (1 for january, 2 for february, etc)
day = int(input("enter a number:"))
if day==1:
    print("january")
elif day==2:
    print("february")
elif day==3:    
    print("march")
elif day==4:
    print("april")
elif day==5:
    print("may")
elif day==6:
    print("june")
elif day==7:
    print("july")
elif day==8:
    print("august")
elif day==9:
    print("september")
elif day==10:
    print("october")
elif day==11:
    print("november")
elif day==12:
    print("december")


# -------------------------------------------------------------------------------------------------------------------------------
# B. MEDIUM QUESTIONS
# ---------------------


# 1) write a program to find the greatest of three numbers
a=int(input("enter a number1:"))
b=int(input("enter a number2:"))
c=int(input("enter a number3:"))
if a>=b and a>=c:
    print(a,"is larger")
elif b>=a and b>=c:
    print(b,"is larger")
else:
    print(c,"is larger")


# -----------------------------------------------------------------------------------------------------------------------------------------

# 2) check if a year is a leap year
a=int(input("enter a year:"))
if a%4==0 or a%100==0 and a%400==0:
    print (a," is a leap year")
else:
    print(a,"is not a leap year")

# -----------------------------------------------------------------------------------------------------------------------------
# 3) write a program to classify  a character entered by the user as a vowel, consonant, or neither
letters = input("enter a letter:").lower()
if len(letters)>1 and len(letters) ==0:
    print("invalid")
elif letters in ["a", "e", "i", "o", "u"]:
    print("it contain vowel")
else:
    print("it contain consonant")

# ----------------------------------------------------------------------------------------------------------------------------------------------------
# 4) calculate thr grade of a student based on the marks they score:

marks = int(input("enter a number:"))
if marks < 100 and marks > 90:
    print("Grade A")
elif marks < 89 and marks > 80:
    print("Grade B")
elif marks < 79 and marks > 70:
    print("Grade C")
elif marks < 70:
    print("fail")

# --------------------------------------------------------------------------------------------------------------------------------

num = int(input("enter a number:"))
if num%15==0:
 print("fizzbuzz")
elif num%3==0:
 print("fizz")
elif num%5==0:
 print("buzz")
else:
    print("invalid")

# ------------------------------------------------------------------------------------------------------------
#  5) write a program to check if three sides length form a valid triangle
a=int(input("enter a value:"))
b=int(input("enter a value:"))
c=int(input("enter a value:"))
if a==b==c:
    print("equilateral triangle")
elif a==b or a==c or b==c:
    print("isoceless triangle")
else:
    print("scalene triangle")    