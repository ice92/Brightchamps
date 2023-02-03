import random
import math
import time

def RandomItem(items):
    return items[random.randint(0,items.__len__()-1)]

print("Hello there!")
print("")
print("In this game, you're going to answer simple")
print("arithmetic questions and become a math")
print("proffesional! Try to answer as many questions")
print("correctly as possible!")
print("")

diff = int(input("Level (1 - 10): "))
maxnum = [5,10,15,20,30,50,100,200,500,1000][diff - 1]
size = input("Questions to answer: ")
highstreak = 0

print("")
print("Ready...")
time.sleep(1.5)
print("Set...")
time.sleep(1.5)
print("Go!")
print("")

score = 0
streak = 0
starttime = time.time()

for i in range(int(size)):
    operators = ["+", "-", "*", "/"]
    operator = RandomItem(operators)
    num1 = random.randint(1,maxnum)
    if operator == "-":
        num2 = random.randint(1,maxnum)
        num1 = num2 + random.randint(1,maxnum)
    elif operator == "/":
        num2 = random.randint(1,maxnum)
        num1 = num2 * random.randint(1,maxnum)
    else:
        num2 = random.randint(1,maxnum)
    qstring = 'What is ' + str(num1) + ' ' + operator + ' ' + str(num2) + '? Your answer: '
    if operator == '+':
        ans = num1 + num2
    elif operator == '-':
        ans = num1 - num2
    elif operator == '*':
        ans = num1 * num2
    elif operator == '/':
        ans = num1 / num2
    else:
        ans = 0
    ans = round(ans)
    print('Question ' + str(i+1) + ':')
    inp = input(qstring)
    if str(inp) == str(ans):
        score += 1
        streak += 1
        if streak > highstreak:
            highstreak = streak
        print(["Okay.","Yes.","Right!","Correct!","Nice!","Good!","Good job!","Very nice!","Very good!","Great!","Very great!","Great job!","Fantastic!","Excellent!","Amazing!","Awesome!","Outstanding!","Unbelievable!"][min(streak-1, 17)] + " x" + str(streak) + " Streak!")
    else:
        streak = 0
        print(RandomItem(["Keep thinking.","You can do it better.","Sorry, incorrect.","Wrong answer.","Whoops!","Keep trying."]) + " The answer is " + str(ans) + ".")
    print("")

totaltime = time.time() - starttime
finalscore = score * maxnum
finalscore -= (int(size)-score) * (maxnum * 1.25)
finalscore -= totaltime * 1.5
finalscore *= highstreak
finalscore = max(round(finalscore), 0)

print('')
print('Game over!')
print('')
print('You got ' + str(score) + ' out of ' + str(int(size)) + ' correct.')
print("This means you've answered " + str(math.ceil((score / int(size)) * 100 * 100) / 100) + "% of questions correctly.")
print('')
print('It took you about ' + str(math.ceil(totaltime / 60)) + ' minutes to answer all ' + str(int(size)) + ' questions.')
print('So this took you about ' + str(math.ceil(totaltime / int(size) * 10) / 10) + ' seconds to answer 1 question.')
print('')
print('Your highest streak is ' + str(highstreak) + '.')
print('Based on your answers, your final score is ' + str(finalscore) + '.')
print('')
input('Thanks for playing! Press enter to exit. ')
