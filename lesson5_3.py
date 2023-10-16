n = int(input("Enter upper limit: "))
num_counter = 0

for i in range(2, n + 1, 2):
    if num_counter == 5:
        num_counter = 0
        print("")
    print(n, end=" ")
    num_counter += 1
