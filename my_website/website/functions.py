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

def input_ans():
    ans = input()
    while not (ans.isdigit() and int(ans) in [0,1,2,3,4]):
        print("Please enter a valid value:")
        ans = input()
    return int(ans)