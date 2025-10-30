import random
def get_rolls():


    while True:
        answer = input("How many pairs of dice would you like to roll?")
        if answer.isdigit():
            num = int(answer)
            if num > 0:
                return num
            else:
                print("Please enter a number bigger than 0.")
        else:
            print("That's not a whole number. Try again.")








def main():

    num_rolls = get_rolls()
    print(f"\nRolling {num_rolls} pair(s) of dice...\n")


    counts = [0]  * 13

    for i in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2

        counts[total] += 1



    print(counts)


    for total in range(2, 13):
        stars = "*" * counts[total]
        print(f"Sum of {total:2}  {stars}")

main()