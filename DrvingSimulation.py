# u=Initial Velocity
# a=Acceleration=input
# t=Time Spent=input
# T=Time
# d=Distance=input
# sl=speedlimit
while (True):
    u = 0
    T =0
    sl = 60
    d = int(input("Distance is"))
    a = int(input("Acceleration is"))
    t = int(input("Time spent is"))
    while (T < t):
        Destination =(T * a) + (a * T * T / 2)
        finalvel = u + (a * T)
        if (T<=t):
            print("Duration:", T, "Distance:", "*"*finalvel)
            T = T + 1
    while (T==t):
        finalvel = u + (a * T)
        Destination =(T / 2) * (finalvel + u)
        if finalvel > sl:
            print("Max Speed was",finalvel,"m/s, congratz you went over the speed limit")
        if finalvel <= sl:
            print("Max speed was",finalvel," m/s")
        if Destination >= d:
            print("Reached at",Destination,"m")
        if Destination < d:
            print("did not reach destination",Destination,"m")
        if (T==t):
            quit()



