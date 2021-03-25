
def isnum(num):
    try:
        if int(num)> 0 and int(num)<=8 :
            return True
    except ValueError:
            return False
            
            
def mario(num):
    for i in range(1,num+1):
        height= ("#"*i)
        num = num -1
        b = " " * (num)
        print(b + height + "  " + height)
    
    

num = int(input("Enter a number: "))
while not isnum(num):
    num = int(input("Invalid input, please use a valid number: "))
mario(num)

