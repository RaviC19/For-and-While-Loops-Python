times = int(input("How many times do I have to tell you to do something? "))

for i in range(times):
    print("CLEAN YOUR ROOM!")
    if i >= 4:
        print("Do you even listen to me? ")
        break
