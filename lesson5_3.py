n = int(input("Enter upper limit: "))
num_counter = 0

for n in range(2, n + 1):
    if n % 2 == 0:
        if num_counter % 5 == 0:
            print("\n")
        print(str(n) + " ", end="")
        num_counter += 1
