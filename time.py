import time

t1 = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
min = int(time.strftime('%M'))

hour = int(input("Enter hour: "))
print(hour)
min = int(input("Enter minute: "))
print(min)

if 0 <= hour < 24 and 0 <= min < 60:
    if 0 <= hour < 12:
        print("Good Morning!")
        print("Have a wonderful start to your day!")
    elif 12 <= hour < 17:
        print("Good Afternoon!")
        print("Hope you're having a productive day!")
    elif 17 <= hour < 20:
        print("Good evening!")
        print("Take some time to relax and unwind!")
    else:
        print("Good night!")
        print("Wishing you a restful night's sleep!")
else:
    print("Invalid option!")
    print("Please enter a valid hour.")
