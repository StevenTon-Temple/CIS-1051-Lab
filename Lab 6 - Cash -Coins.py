def isfloat(n):
    try:
        if float(n) > 0:
            return True
    except ValueError:
            return False

quarter = 25
dime = 10
nickel = 5
penny = 1
nums = [quarter, dime, nickel, penny]

def cash (change):
    coins = 0
    while change >= nums[0] and change > nums[1]:
        change = change - nums[0]
        coins = coins + 1
    while change < nums[0] and change >= nums[1]:
        change = change - nums[1]
        coins = coins + 1
    while change < nums[1] and change >= nums[2]:
        change =change - nums[2]
        coins = coins + 1
    while change < nums[2] and change >= nums[3]:
        change = change - nums[3]
        coins = coins + 1
    return coins
    
num = input("Enter a number: ")
if isfloat(num) == True:
    change = float(num)
    change = round(change*100)
while not isfloat(num):
    num = input("Invalid input, please use a valid number: ")   
    if isfloat(num) == True:
        change = float(num)
        change = round(change*100)

print("Your cash is",num,"so your change is", cash(change), "coins.")





