number = input("Test the number? ")
for n in range(10):
    wrong = True
    while wrong:
        question = f"{n} x {number} = " 
        answer = input(question)
        if answer == "q": 
            print('Thank you')
            exit()
            
        if int(answer) == (n * int(number)):
            print("Well done")
            wrong = False
        else:
            print("Try again")
