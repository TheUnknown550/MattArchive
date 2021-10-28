word=input("Enter your word: ")
n=len(word)
wor=[]
counter = 0
while True:
    guess=input("Enter your Guess: ")
    for i in range(n):
        wor[i]='_'
        find=word.find(guess)