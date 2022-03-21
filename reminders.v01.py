now = float(input("Please enter the current hour in military time (0 - 23): "))

if(0 <= now <= 5):
    print("It's early! You should be sleeping!")
elif(5 < now <= 7):
    print("Wake up, brew that coffee, get that mile run in, and get that breakfast...")
elif(7 < now <= 9):
    print("Time to go to work.")
elif(9 < now <= 12):
    print("You should be working!")
elif(12 < now <= 13):
    print("Take your lunch break!")
elif(13 < now <= 17):
    print("Do you feel that afternoon lull?")
elif(17 < now <= 19):
    print("Time to hit the gym.")
elif(19 < now <= 21):
    print("Got to eat that dinner.")
elif(21 < now <= 23):
    print("Get that SLEEP. And REPEAT!")
else:
    print("You didn't type in an acceptable value!")