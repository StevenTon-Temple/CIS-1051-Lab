
import random
roll = random.randint(1,6)
def pig():
    turn_total = 0
    while turn_total < 20:
        roll = random.randint(1,6)
        turn_total += roll
        if roll == 1:
            print("Roll:",roll)
            print("Turn total:","0")
            turn_total = 0
            break
        elif roll >= 2 and roll != 1:
            print("Roll:",roll)
    print("Turn total:",turn_total)
    return turn_total
    
#pig()

def pig2():
    prob= {}
    turn_total = 0
    score =[]
    how = int(input("How many simulations do you want? "))
    for _ in range(how):
        score.append(pig())
    for num in score:
        if num not in prob:
            s = score.count(num)
            Estimated_probablility = s/how
            prob[num] = Estimated_probablility


    lst = sorted(prob)
    print("Score", " ","Estimated Probability")
    for num in lst:
        print(str(num) + "\t" + str(prob[num]))   


#pig2()
x = int(input("How many point to hold at? "))
def holdatx():
    turn_total = 0
    while turn_total < x:
        roll = random.randint(1,6)
        turn_total += roll
        if roll == 1:
            print("Roll:",roll)
            print("Turn total:","0")
            turn_total = 0
            break
        elif roll >= 2 and roll != 1:
            print("Roll:",roll)
        elif roll == 1 or roll > x:
            break
    print("Turn total:",turn_total)
    return turn_total


def pig3():
    how = int(input("How many simulations do you want? "))
    prob= {}
    turn_total = 0
    score =[]
    for _ in range(how):
        score.append(holdatx())
    for num in score:      
        if num not in prob:
            s = score.count(num)
            Estimated_probablility = s/how
            prob[num] = Estimated_probablility


    lst = sorted(prob)
    print("Score", " ","Estimated Probability")
    for num in lst:
        print(str(num) + "\t" + str(prob[num]))   

pig3()

def pig4():
    score = int(input("What score are you tring to achive? "))
    while True:
        roll = random.randint(1,6)
        turn_total = pig()
        score = score + turn_total
        print('new score', score)
        if roll == 1 or turn_total >= 20:
            break
#pig4()
    
def pig5():
    score = 0
    turn_in_game= 0
    while True:
        roll = random.randint(1,6)
        turn_total = pig()
        score = score + turn_total
        turn_in_game +=1
        print('new score', score)
        if score>100:
            break
        return score
#pig5()

def pig6():
    turn_tot= 0
    how = int(input("How many games do you want? "))
    turns = 0
    avg_turn = 0
    for num in range(how):
        turn = pig5()
        turn_tot = turn
    avg_turn = turn_tot/how
    print(avg_turn)
#pig6()

def pig7():
    player1 = 0
    player2 = 0
    player_num = 1
    print("Player 1 score is: ",player1)
    print("Player 2 score is: ",player2)
    while True:
        if player_num == 1:
            print("It's player 1 turn")
            player1 += pig()
            print('New score for player 1 is:', player1)
            player_num=2
        if player_num == 2:
            print("It's player 2 turn")
            player2 += pig()
            print('New score for player 2 is:', player2)
        print(".....")
        if player1 >=100 or player2>=100:
            break
#pig7()
def rollorhold():
    turn_total = 0
    while turn_total < 20:
        roll = random.randint(1,6)
        turn_total += roll
        if roll == 1:
            print("Roll:",roll)
            print("Turn total:","0")
            turn_total = 0
            break
        elif roll >= 2 and roll != 1:
            roll_or_hold = input("Enter nothing to roll; enter anything to hold.")
            if roll_or_hold == "":
                print("Roll:",roll)
            elif roll_or_hold != "":
                break
    print("Turn total:",turn_total)
    return turn_total

def pig8():
    player1 = 0
    player2 = 0
    d = ["Player 1","Player 2"]
    r=random.choice(d)
    print("Player 1 score is: ",player1)
    print("Player 2 score is: ",player2)
    while True:
        if r == d[0]:
            print("You will be player 1")
            player1 += rollorhold()
            print('New score for player 1 is:', player1)
            print('New score for computer is:', player2)
        if r == d[1]:
            player1 += pig()
        if r == d[1]:
            print("You will be player 2")
            player2 += rollorhold()
            print('New score for computer is:', player1)
            print('New score for player 2 is:', player2)
        if r == d[0]:
            player2 += pig()
        if player1 >=100 or player2>=100:
            break
#pig8()
