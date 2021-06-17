import random

big_numbers = [100,75,50,25]
small_numbers = [10,9,8,7,6,5,4,3,2,1]
min_size = 100
max_size = 999

def request_amount_of_big():
    amount_of_big = int(input("How many big numbers would you like (0-4): "))
    if amount_of_big > 4:
        amount_of_big = 4
    elif amount_of_big < 0:
        amount_of_big = 0
    return amount_of_big

def calc_amount_of_small(big):
    amount_of_small = 6 - big
    return amount_of_small

def gen_rand_numbers(amnt_big, big_numbers, amnt_small, small_numbers):
    rand_numbers = []
    for i in range(amnt_big):
        number = big_numbers[random.randint(0,len(big_numbers)-1)]
        rand_numbers.append(number)
    for i in range(amnt_small):
        number = small_numbers[random.randint(0,len(small_numbers)-1)]
        rand_numbers.append(number)
    return rand_numbers

def gen_target_num(min_size, max_size):
    target = random.randint(min_size,max_size)
    return target


print("Welcome to countdown, the numbers game!")
amount_of_big = request_amount_of_big()
amount_of_small = calc_amount_of_small(amount_of_big)
rand_numbers = gen_rand_numbers(amount_of_big, big_numbers, amount_of_small, small_numbers)
rand_numbers.sort(reverse=True)
print("Here are your numbers: " + str(rand_numbers))
target = gen_target_num(min_size, max_size)
print("Your target number is: " + str(target))
print("yeet")