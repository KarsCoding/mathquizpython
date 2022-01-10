wrongAnswers = 0

print('Quick and Easy math quiz')
print('Ready? (Press ENTER)')
input ()


print('What is 58 - 13?')
answer1 = input()
if answer1 == '45':
    print('Correct')
else:
    print('Incorrect')
    wrongAnswers += 1


print('What is 490 + 559?')
answer2 = input()
if answer2 == '1049':
    print('Correct')
else:
    print('Incorrect')
    wrongAnswers += 1


print ('What is 189 Divided by 3?')
answer3 = input()
if answer3 == '63':
    print('Correct')
else:
    print('Incorrect')
    wrongAnswers += 1


print ('And Finally, What is 3989 times 3?')
answer4 = input()
if answer4 == '11967':
    print('Correct! That was a Hard one :)')
else:
    print('Incorrect, That was a Hard one to be fair :)')
    wrongAnswers += 1


print('End of Quiz, Press Enter to see Results')
input()


Grade = 8 - wrongAnswers
if Grade > 6.5:
    print('Great Job! You got an', Grade)
if Grade < 6.5:
    print("You got a", Grade," Definitely improvable but good try :D")
input()

    

