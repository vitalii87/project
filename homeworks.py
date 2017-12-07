'''                                                           # 1 task

H='1234 9u ytreee' 

#print(H.isspace()) - not working
print(len(H.split(' '))-1)                    #1.2  print(a1.isspace()) 
print(len(H.split('.'))-1)                    #1.3
a1='Homework'
a2='homework'
print(a1.center(100,' '))                     #1.4
print(a2.capitalize())                        #1.5

                                                               #task 2

summa=print(int(179*2+971*2)/2)               #2.1

n = int(input())
print(n // 10 % 10)                           #2.2

a=123
print(sum([int(i) for i in str(a)]))          #2.3




                                                               #task 3

import calendar
a=print(calendar.isleap(2020))
if a==True:
  print('yes')
else: print('no')  

import calendar
input('enter year')
if input(calendar.isleap())=True:
 print('leap year') 

                                                               #task4
print("enter width:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a + b > c and a + c > b and b + c > a:
	print("exist")
else:
	print("doesnt exist")                          

                                                               #task6
print("enter num:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a==b==c:
  print('all same')
elif a==b or a==c or b==c:
 print("two same") 
else :
  print('no same')
'''