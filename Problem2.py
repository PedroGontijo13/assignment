#Write a function which lets the user enter English words. 
# The user can keep entering English words as long as the user
# has not entered the word “exit”. Once the user enters “exit” 
# the function will return and print the list of all distinct 
# words starts with English alphabets. Like:

def organizeList(list):
    myList = sorted(list)
    print(myList)
    return myList

def inputList():
    word = str
    words = []
    while word != "exit":
        word = str(input("word:"))
        if word != "exit":
            words.append(word)
    organizeList(words)

inputList()