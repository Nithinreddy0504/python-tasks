# perfect number
k=0;
num=int(input("enter the number"));
for i in range(1,num):
    if(num%i==0):
        k+=i;
if(k==num):
    print("perfect number");
else:
    print("not perfect ");
    
# LCM
num1=int(input("enter the number "));
num2=int(input("enter the second number"));
spy=True
for i in range(1,num2+1):
    i*num1;
    if(spy==False):
        break;
    for j in range(1,num1+1):
        j*num2;
        if(i*num1==j*num2):
            print(i*num1);
            spy=False;
            break;
        
# sum of even digits
count=0
number=int(input("enter a number"));
while(number>0):
    rev=number%10;
    if(rev%2==0):
        count+=rev;
    number=number//10;
print(count)

# Team numbers
number=int(input("enter how many team numbers are there"));
total=0;
for i in range(1,number+1):
    if(i%2==0):
        team_number=i*100;
        print(team_number);
        total+=team_number
print(total)


# n prime numbers
number=int(input("enter a number"));

for j in range(2,number+1):
 print("j",j)
 spy=False
 for i in range(2, j):
    print("i",i)
    if(j%i==0):
        spy=True;
       
        break;
 if spy==False:
    print(j);