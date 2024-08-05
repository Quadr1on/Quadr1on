import time
Curtime = time.strftime("%H:%M:%S")
print("Time is: ",Curtime)
if Curtime >= "00:00:00" and Curtime < "12:00:00":
    print("Good Morning")

elif Curtime >= "12:00:00" and Curtime < "16:00:00":
    print("Good AfterNoon")

if Curtime >= "16:00:00" and Curtime < "23:59:59":
    print("good evening")



    