word=input("Enter your word: ")
n=len(word)
correct=[]
while True:
    Guess=input("enter your guess: ")
    for i in range(n):
        if (word[i] == Guess):
            correct.append(i)
    print(word[correct])
