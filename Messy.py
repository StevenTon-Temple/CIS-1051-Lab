

print("It’s time to go on a scavenger hunt!")
print("You'd be amazed how many things can go wrong!")
print("Please enter how long you want to travel for:")
initialPos = 7.0
time  = float(input('enter how long to travel for: '))
velocity = 5.0
acceleration = 1.0
position =  initialPos + velocity * time + (1 / 2) *acceleration*time*time
print("our position is", position)

