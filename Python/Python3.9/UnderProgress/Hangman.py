word=input("Enter your word: ")
n=len(word)
wor=[]
counter = 0
while True:
    Guess=input("enter your guess: ")
    for i in range (n):
        cor=word.find(Guess,i)
        wor.append(i)
        wor[i]='_'
        wor.pop(cor)
        wor[cor]=Guess
        print(cor)