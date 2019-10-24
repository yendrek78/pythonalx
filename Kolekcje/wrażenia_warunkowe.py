x = int(input("Podaj pierwszą współrzędną:"))
y = int(input("Podaj drugą współrzędną:"))

if x > 100 or y > 100 or x < 0 or y < 0:
    print("jesteś poza planszą")
elif x > 90 and y > 90:
    print("jesteś w Pgr")
elif x > 90 and y < 10:
    print("jesteś w Pdr")
elif x < 10 and y > 90:
    print("jesteś w Lgr")
elif x < 10 and y < 10:
    print("jesteś w Ldr")
elif x > 90:
    print("jesteś w pk")
elif x < 10:
    print("jesteś w lk")
elif y > 90:
    print("jesteś w gk")
elif y < 10:
    print("jesteś w dk")
else:
    print("jesteś w centrum")
