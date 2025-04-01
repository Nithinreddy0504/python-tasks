# LOOPS---EASY QUESTIONS
# 1) Print all numbers from 1 to 100 using a  for  loop.
for i in range(1,101):
    print(i);

#2) write a program to display the multiplication table of a given number. First 20 
number=int(input('enter a number'));
for j in range(1,number):
 for i in range(1,21):
    print(j,'*',i,'=',j*i)

# 3) print all even numbers between 1 and 50 using a  while loop.
i=1;
while(i<50):
    if(i%2==0):
        print(i);
    i+=1;

# 4) write a program to print the sum of the first  n  natural numbers. (n*n+1/ 2) 
naturalnumbers=0;
for i in range(1,101):
    naturalnumbers+=i;
print(naturalnumbers);


# 5) reverse a number using a  while  loop. 1.  Also can we get the sum of all the digits. 
number=54321;
rev_num=0;
count=0;
sum=0;
while(number>0):
    rem=number%10;
    sum+=rem;
    if(rem%3==0):
        print(rem,'is divisible by 3');
    rev_num=rev_num*10+rem;
    number=number//10;
    count=count+1;
print('reverse of given',rev_num);
print('digits are in given number',count);
print('sum of given number',sum)

# 6) write a program to count the number of digits in a given number using a  while  loop. 
digit=input('enter a number');
i=1;
while(i==1):
 print(len(digit));
 i+=1;

# 7) write a program that keeps asking the user to enter numbers until they enter a negative number. Use a  while  loop. 
while(True):
    user=int(input('enter a number'));
    if(user<0):
        break;
# ---------------------------------------------------------------------------------------------------------------
# LOOPS---MEDIUM QUESTIONS

# 1) print the first 10 terms of the Fibonacci series using a  for loop.
number1=0;
number2=1;
number3=int(input('enter the number'));
for i in range(1,number3-1):
    number4=number1+number2;
    if(number1==0 and number2==1):
      print(number1);
      print(number2);
    print(number4);
    number1=number2;
    number2=number4;
    
    
# 2) check if a given number is a prime number using a  for loop. 
user_input_number=int(input('enter a number'));
if(user_input_number>1):
 for i in range(2,user_input_number):
    if(user_input_number%i!=0):
        if(i==user_input_number-1):
         print('prime');
         break;
    else:
        print('not prime');
        break;
else:
    print('please enter a valid number');
# 3) find the factorial of given number using while loop
number=int(input('enter a number'));
number1=1;
if(number==0):
    print(number1);
else:
 while(number>0):
    
    number1*=number;
    number-=1;
    if(number==0):
        break;
 print(number1)  

# 4) Print all numbers from 1 to 100 that are divisible by 3 and 5 using a  for  loop
for i in range(1,101):
    if(i%5==0 and i%7==0):
        print(i); 

# 5) Implement a menu-driven program where the user can choose to: 1.  Find the square of a number. 2.  Find the cube of a number. 3.  Exit.

    
for i in range(1,4):    
    print('1.square of the number');
    print('2.cube of the number');
    print('3.exit');
    user_input=int(input('please enter above  any one option numbers here'));
    if(user_input==1):
        user_input2=int(input('enter the number'));
        print(user_input2*user_input2);
        
    elif(user_input==2):
        user_input3=int(input('enter the number'));
        print(user_input3*user_input3*user_input3);
    else:
        break;
    # 6) Implement a basic login system where the user has three attempts to enter the correct password using a loop.
password='king123';
for i in range(1,4):
    user_input=input('enter your correct password');
    if(password==user_input):
        print('you are entered correct password');
        break;
    else:
        print('you are entered wrong password');