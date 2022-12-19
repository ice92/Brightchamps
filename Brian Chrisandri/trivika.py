import time
import getpass
import random

questions = [
    ["What object is used in JavaScript to evaluate math?","Math"],
    ["How to throw an exception (error) in JavaScript?","throw new Error"],
    ["What method prints something to the JavaScript console?","console.log"],
    ["How to create an array with 3 empty items using the Array() method, using JavaScript?","Array(3)"],
    ["What command specifies a constant so that it can't be changed again?","const"],
    ["What stands for \"Not a Number\" in JavaScript?","NaN"],
    ["What is the symbol to check equality (not strict equality) in JavaScript?","=="],
    ["What is the symbol to return the remainder of numbers in JavaScript?","%"]
]
score = 0

print("Hello, welcome to JavaScript Trivika!")
print("In JavaScript Trivika, you're going to answer mild-to-moderate difficulty questions about JavaScript.")
getpass.getpass("Are you ready? Press enter to continue... ")
print("")

print("Ready?")
time.sleep(1)
print("Set...")
time.sleep(1)
print("Go!")
print("")

for i in range(5):
    questionindex = random.randint(0,len(questions)-1)
    print(questions[questionindex][0])
    answer = input("Your answer: ")
    if (answer == questions[questionindex][1]):
        print("Correct!")
        score += 1
    else:
        print("Wrong answer. The answer is \"" + questions[questionindex][1] + "\"")
    print("")

print("Game over!")
print("You got " + str(score) + " out of 5 correct.")
print("This means you've answered " + str(round((score / 5) * 100)) + "% of questions correctly.")
print("")
print("Want to improve your score? Learn JavaScript:")
print("- https://developer.mozilla.org/en-US/docs/Learn/JavaScript")
print("- https://developer.mozilla.org/en-US/docs/Web/JavaScript")
print("")

getpass.getpass("Press enter to exit... ")
