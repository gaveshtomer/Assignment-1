sec=int(input("Enter number of seconds"))
if sec < 60:
    print("Please enter seconds more than 60.")
else:
    Min = sec//60
    secs = sec%60
    print(sec,"seconds corresponds to",Min,"minutes and",secs,"seconds")
