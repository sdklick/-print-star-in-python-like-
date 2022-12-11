# print star in python like
'''
*
**
***
****
*****
'''
userinput=int(input('please input number : '))
for x in range(userinput):
    for y in range(x):
        print("*",end='')
    print("\r")    
