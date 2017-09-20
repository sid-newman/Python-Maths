import random
from random import randint

maths=['+','-','*'] 
score = 0
name = raw_input ('What is your name?')
Class = raw_input ('What is your class: A, B Or C')
for i in range (10):
    num1=randint(0,20)
    num2=randint(1,20)
    op=random.choice(maths)

    answer=float(input('\n'+str(num1)+str(op)+str(num2)+'='))

    if op=='+':
        actualAns=num1+num2
    if op=='-':
        actualAns=num1-num2
    if op=='*':
        actualAns=num1*num2
    if answer == actualAns:
        print('Your answer was correct!')
        score += 1
    if answer != actualAns:
        print('Sorry, the correct answer was',str(actualAns))

print('Well done, you got '+str (score) + 'answer(s) out of 10 correct.')

if Class == 'A' or Class == 'a': #function temp opens txt files and saves user results
    print('Your score has been saved to Class A Results.txt')
    f = open('Class A Results.txt', "a")
    f.write('\n' +str(name)+': '+str(score))
    f.close() # 

if Class == 'B' or Class == 'b':
    print('Your score has been saved to Class B Results.txt')
    f = open('Class B Results.txt', "a")
    f.write('\n' +str(name)+': '+str(score))
    f.close()

if Class == 'C' or Class == 'c':
    print('Your score has been saved to Class C Results.txt')
    f = open('Class C Results.txt', "a")
    f.write('\n' +str(name)+': '+str(score))
    f.close()
    

