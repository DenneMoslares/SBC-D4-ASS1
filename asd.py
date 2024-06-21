from random import randint

#kini ang function para maka kuhag valid input
def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

#get user input og e generate ang random numbers
nums = [get_integer_input(f"Enter number {i+1}: ") for i in range(3)]
gen_nums = [randint(0, 9) for _ in range(3)]

#print user input and generated numbers
print(f"user input: {''.join(map(str, nums))}")
print(f"generated numbers: {''.join(map(str, gen_nums))}")

#determine the result
result = "you win" if nums == gen_nums else "you partially win" if sorted(nums) == sorted(gen_nums) else "you lose"
print(result)
