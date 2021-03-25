seconds = input('Enter seconds here please: ')
seconds = int(seconds)
hours = seconds//3600
seconds_remaining = seconds % 3600
minutes = seconds_remaining // 60
seconds_remaining_minutes = seconds % 60


print( seconds,"sec =" , hours,"hours", minutes,"minutes", seconds_remaining_minutes,"seconds")
