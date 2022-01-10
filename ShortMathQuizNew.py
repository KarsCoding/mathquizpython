
#Variables
wrongAnswers = 0
difficulty1 = False
difficulty2 = False
difficulty3 = False

#Loop for choosing Difficulty
run = True
while run:
    print('Quick Math Quiz')
    print('Choose your difficulty (1 = Easy ; 2 = Medium ; 3 = Hard')
    difficulty = input()
    if difficulty == '1':
        difficulty1 = True
        break
    elif difficulty == '2':
        difficulty2 = True
        break
    elif difficulty == '3':
        difficulty3 = True
        break
    else:
        run = True


#Easy Difficulty Code
if difficulty1 == True:
    print('You have chosen Easy Difficulty')
    print()
    print('First Question : What is 35 + 90')
    answerEasy1 = input()
    if answerEasy1 == '125':
        print('Correct')
        print()
    else:
        print('Incorrect')
        print()
        wrongAnswers += 2
    print()
    print('Second Question : What is 149 - 44')
    answerEasy2 = input()
    if answerEasy2 == '105':
        print('Correct')
        print()
    else:
        print('Incorrect')
        print()
        wrongAnswers += 2
    print()
    print('Third Question : What is 93 + 29')
    answerEasy3 = input()
    if answerEasy3 == '122':
        print('Correct')
        print()
    else:
        print('Incorrect')
        print()
        wrongAnswers += 2
    print()
    print('Fourth Question : What is 103 - 57')
    answerEasy4 = input()
    if answerEasy4 == '46':
        print('Correct')
        print()
    else:
        print('Incorrect')
        print()
        wrongAnswers += 2
    print()
    print('Last Question : What is 987 - 33')
    answerEasy5 = input()
    if answerEasy5 == '954':
        print('Correct')
        print()
    else:
        print('Incorrect')
        print()
        wrongAnswers += 2

    #Outro
    grade = 10 - wrongAnswers
    print()
    print("That's it for the Math Quiz, I hope you enjoyed it! Press ENTER for Results")
    input()
    if grade == 10:
        print('You got a 10! Great job but again this is easy mode after all. Try a Harder difficulty next time')
        print('You got 0/5 questions incorrect')
    elif grade == 8:
        print('You got an 8, This is decent! Definitely look into trying Medium difficulty next')
        print('You got 1/5 question incorrect')
    elif grade == 6:
        print('You got a 6, Definitely could be better but its not the worst')
        print('You got 2/5 questions incorrect')
    elif grade == 4:
        print('You got a 4, You need some practice')
        print('You got 3/5 questions incorrect')
    elif grade == 2:
        print('You got a 2, This is bad')
        print('You got 4/5 questions incorrect')
    elif grade == 0:
        print('You got a 0, You definitely just spammed through the questions and didnt even try')
        print('You got all questions incorrect')
    print()
    print('--------------------------------')
    print('Thanks for playing! - Karscoding')
    print('--------------------------------')



#Medium Difficulty Code
if difficulty2 == True:
    print('You have chosen Medium Difficulty')
    print()
    print('First Question : What is 66 / 3')
    answerMedium1 = input()
    if answerMedium1 == '22':
        print('Correct')
        print()
    else:
        print('Incorrect')
        print()
        wrongAnswers += 2
    print()
    print('Second Question : What is 28 * 6')
    answerMedium2 = input()
    if answerMedium2 == '168':
        print('Correct')
        print()
    else:
        print('Incorrect')
        print()
        wrongAnswers += 2
    print()
    print('Third Question : What is 819 / 9')
    answerMedium3 = input()
    if answerMedium3 == '91':
        print('Correct')
        print()
    else:
        print('Incorrect')
        print()
        wrongAnswers += 2
    print()
    print('Fourth Question : What is 667 * 2')
    answerMedium4 = input()
    if answerMedium4 == '1334':
        print('Correct')
        print()
    else:
        print('Incorrect')
        print()
        wrongAnswers += 2
    print()
    print('Last Question : What is 29 * 34')
    answerMedium5 = input()
    if answerMedium5 == '986':
        print('Correct')
        print()
    else:
        print('Incorrect')
        print()
        wrongAnswers += 2

    #Outro
    grade = 10 - wrongAnswers
    print()
    print("That's it for the Math Quiz, I hope you enjoyed it! Press ENTER for Results")
    input()
    if grade == 10:
        print('You got a 10! Great job! Try a Harder difficulty next time')
        print('You got 0/5 questions incorrect')
    elif grade == 8:
        print('You got an 8, This is really good!')
        print('You got 1/5 question incorrect')
    elif grade == 6:
        print('You got a 6, Still really good but not the best')
        print('You got 2/5 questions incorrect')
    elif grade == 4:
        print('You got a 4, You need some practice')
        print('You got 3/5 questions incorrect')
    elif grade == 2:
        print('You got a 2, This is bad')
        print('You got 4/5 questions incorrect')
    elif grade == 0:
        print('You got a 0, You definitely just spammed through the questions and didnt even try')
        print('You got all questions incorrect')
    print()
    print('--------------------------------')
    print('Thanks for playing! - Karscoding')
    print('--------------------------------')



#Hard Difficulty Code
if difficulty3 == True:
    print('You have chosen the Hard Difficulty')
    print()
    print('First Question : What is 33 ^ 3')
    answerHard1 = input()
    if answerHard1 == '35937':
        print('Correct')
        print()
    else:
        print('Incorrect')
        print()
        wrongAnswers += 2
    print()
    print('Second Question : What is 38 + 49 * 3^2')
    answerHard2 = input()
    if answerHard2 == '479':
        print('Correct')
        print()
    else:
        print('Incorrect')
        print()
        wrongAnswers += 2
    print()
    print('Third Question : What is 289^2 + 284 * 3')
    answerHard3 = input()
    if answerHard3 == '84373':
        print('Correct')
        print()
    else:
        print('Incorrect')
        print()
        wrongAnswers += 2
    print()
    print('Fourth Question : What is 290 * 39 + 13(42 + 3)')
    answerHard4 = input()
    if answerHard4 == '11895':
        print('Correct')
        print()
    else:
        print('Incorrect')
        print()
        wrongAnswers += 2
    print()
    print('Last Question : What is 28498 + 32 * 3(489 + 2) /2')
    answerMedium5 = input()
    if answerMedium5 == '49366':
        print('Correct')
        print()
    else:
        print('Incorrect')
        print()
        wrongAnswers += 2

    #Outro
    grade = 10 - wrongAnswers
    print()
    print("That's it for the Math Quiz, I hope you enjoyed it! Press ENTER for Results")
    input()
    if grade == 10:
        print('You got a 10! Youre insane! But you probably used a calculator but I never told you not to :)')
        print('You got 0/5 questions incorrect')
    elif grade == 8:
        print('You got an 8, This is insanely good, not a 10 though :(')
        print('You got 1/5 question incorrect')
    elif grade == 6:
        print('You got a 6, This is really good!')
        print('You got 2/5 questions incorrect')
    elif grade == 4:
        print('You got a 4, This is decent!')
        print('You got 3/5 questions incorrect')
    elif grade == 2:
        print('You got a 2, You kinda suck, try again')
        print('You got 4/5 questions incorrect')
    elif grade == 0:
        print('You got a 0, You definitely just spammed through the questions and didnt even try')
        print('You got all questions incorrect')
    print()
    print('--------------------------------')
    print('Thanks for playing! - Karscoding')
    print('--------------------------------')

    

