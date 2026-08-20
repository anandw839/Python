'''condition = 1

while condition <10:
    print(condition)

'''
    #multiline comment
'''
    # condition= condition+1
    condition +=1

condition=5

#while True:
    #print("infinite")



exampleList=[1,2,4,6,8,9,0]

for things in exampleList:
    print(things)

for x in range(1,11):
    print(x)



x=2
y=7
z=10

if x>y:
    print(x,'is greater than',y)

if x<y:
    print(x,'is less than',y)



x = 13
y=6

if x<y:
    print(x,'is less than',y)
if x>y:
    print(x,'is greater than',y)
else:
    print(x,'is not less than',y)


def addition(num1,num2,num3,num4):
    answer=num1+num2+num3+num4
    return answer
x= addition(5,6,7,5)
print(x)

def website(font='TNR',background_color='white',font_size='11',font_color='black'):
    print('font:',font)
    print('bg:',background_color)
    print('Font size:', font_size)
    print('Font color:',font_color)

#website('TNR','white','11','black')

website(font_color='grey',font='TNR',background_color='white',font_size='11'

x=6
def example3():
    global x
    x += 1
    print(x)

def example():
    z=5
    print(z)


#cannot do this
#print(z)

def example2():
    z=7
    print(z)
    y= x+1
    print(y)
    return y

x= example2()
print(x)

variable = 55
print(varaiable)
#wirte into file
writeMe='Example text'
saveFile = open('exampleWrite.txt','w')
saveFile.write(writeMe)
saveFile.close()
#append text into file
writeMe='some text'
saveFile = open('exampleWrite.txt','a')
saveFile.write('\n')
saveFile.write(writeMe)
saveFile.close()
# reading from file
readMe = open('exampleWrite.txt','r').read()
print(readMe)

splitMe= readMe.split('\n')
print(splitMe)

readMe2= open('exampleWrite.txt','r').readlines()
print(readMe2)

class calc:

    def add(x,y):
        answer=x+y
        print(answer)
    def sub(x,y):
        answer=x-y
        print(answer)
    def mult(x,y):
        answer=x*y
        print(answer)
    def div(x,y):
        answer=x/y
        print(answer)

calc.add(5,6)


name= input('what is your name: ')
print('Hello',name)

import statistics

exList=[5,3,2,9,9,7,4,3,1,8,9]

x= statistics.mean(exList)
print(x)


x= statistics.median(exList)
print(x)


x= statistics.mode(exList)
print(x)


x= statistics.stdev(exList)
print(x)


from statistics import mean as m , stdev as s
#import statistics as s

from statistics import *
exList = [5,6,2,7,5,2,4,6,8]

#print(s.mean(exList))

print(m(exList))
print(m(exList))





def example():
    return 15,19

a,b= example()

print(a)
print(b)

x=[3,4,5,6,7,5,3]
print(x)

print(x[5])

x.append(12)

print(x)

x.insert(5,7)
print(x)

x.remove(7)
print(x)

print(x.index(12))

print(x.count(3))

x.sort

print(x)

x=['spot','Cam','Jan','Dave']

print(x)
x.sort()

x.reverse()
print(x)'''



gradeDict={'kelly':89, 'David':65}

print(gradeDict)

print(gradeDict['David'])

gradeDict['David']= 56

print(gradeDict)

gradeDict['Jessy']=92
print(gradeDict)

del gradeDict['David']
print(gradeDict)


gradeDict = {'Kelly':[88,89],
             'Kack':[95,87],
             'Jessy':[92,99]}
print(gradeDict)

print(gradeDict['Jessy'])
print(gradeDict['Jessy'][0])