word=input("Enter your word: ")
n=len(word)
wor=[n]
counter = 0
def find_w(n,guess,word):
    for i in range(n):
        find=word.index(i)
        if i==find:
            print(guess,end='')
        else:
            print('_',end='')
            
for i in range (n):
    guess=input("Enter your guess: ")
    if guess in word:
        find_w(n,guess,word)
    else:
        print("your letter is not in the word.") 