import random

#generate list of potential answers
def gen_choices():
    choices = []
    for i in range(1,10):
        for j in range(1,10):
            if i != j:
                for k in range(1,10):
                    if k not in [i,j]:
                        for l in range(1,10):
                            if l not in [i,j,k]:
                                guess = str(i)+str(j)+str(k)+str(l)
                                choices.append(guess)
    return choices

#check if proper input
def input_ans():
    ans = input()
    while not (ans.isdigit() and int(ans) in [0,1,2,3,4]):
        print("Please enter a valid value:")
        ans = input()
    return int(ans)

#shorten list of possible answers from cow & bull values
def narrowing(cows,bulls, guess):
    choices_temp = []
    for choice in choices:
        toll = 0
        for i in range(0,4):
            if choice[i] == guess[i]:
                toll = toll + 1
        if toll != cows:
            continue
        choices_temp.append(choice)
    choices_temp1 = []
    for choice in choices_temp:
        toll = 0
        for i in range(0,4):
            for j in range(0,4):
                if i !=j:
                    if choice[i] == guess[j]:
                        toll = toll + 1
        if toll != bulls:
            continue
        choices_temp1.append(choice)
    return(choices_temp1)

#begin or reset the game
def start():
    global choices, guess, count, cows
    choices = gen_choices()
    guess = random.choice(choices)
    count = 1
    cows = 0

#play the game
start()
print(len(choices))
while int(cows) != 4: 
    print("Guess #", count, ":",guess)
    print("Cows:")
    cows = input_ans()
    if cows == 4:
        continue
    print("Bulls:")
    bulls = input_ans()
    choices = narrowing(cows, bulls, guess)
    if (len(choices) == 0 or (cows + bulls > 4) or (cows == 3 and bulls == 1)):
        print("You have entered the wrong number of bulls or cows somewhere. Start again.")
        start()
        continue
    guess = random.choice(choices)
    count = count + 1
else:
    print("CORRECT!")