x=input("Enter a word: ")
i=0
for i in range (10):
    print("")
    i+=1
lives = 6 
while True:
    y=input("Enter your letter: ")
    if y in x:
        print("Correct the word is: ", x)
        break
    elif lives == 0:
        print("YOur Dead")
        break
    else:
        print("Your letter is not in the word")
        print("your have ", lives,"lives")
        lives -= 1