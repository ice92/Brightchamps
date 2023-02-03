import time

def leadingzero(int: int):
    if (int < 10):
        return "0" + str(int)
    else:
        return str(int)

def assistanttalk(string: str):
    print("Assistant: " + string)

def talk(string: str):
    print("You: " + string)

def linebreak():
    print("")

assistanttalk("Hello there! What do you want to do?")
linebreak()
for i in range(1000000):
    answer = input("> ")
    linebreak()
    keyword = answer.lower()
    talk(answer)
    if (keyword.__contains__("hello")):
        assistanttalk("Oh, hi there!")
    elif (keyword.__contains__("hi")):
        assistanttalk("Oh, hello there!")
    elif (keyword.__contains__("who are you")):
        assistanttalk("I\'m your assistant.")
    elif (keyword.__contains__("what time") or (keyword.__contains__("what") and keyword.__contains__("time")) or keyword == "time" or keyword == "current time"):
        assistanttalk("The time is " + leadingzero(time.localtime().tm_hour) + ":" + leadingzero(time.localtime().tm_min) + ":" + leadingzero(time.localtime().tm_sec) + ".")
    elif (keyword.__contains__("what date") or (keyword.__contains__("what") and keyword.__contains__("date")) or keyword == "date" or keyword == "current date"):
        assistanttalk("Today it\'s " + ["January","February","March","April","May","June","July","August","September","October","November","December"][time.localtime().tm_mon - 1] + " " + str(time.localtime().tm_mday) + ", " + str(time.localtime().tm_year) + ".")
    elif (keyword.startswith("goodbye") or keyword.startswith("bye") or keyword.startswith("thank you") or keyword.startswith("thanks") or keyword == "exit" or keyword == "quit"):
        assistanttalk("Okay, thanks for visiting us! See you later!")
        time.sleep(2)
        exit()
    else:
        assistanttalk("I don\'t understand your question.")
    linebreak()
