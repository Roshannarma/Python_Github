import time
def create_pascal(depth):
    my_pascal_triangle = [[1]]
    x = 1
    while x < depth:
        my_current_line = my_pascal_triangle[-1]
        my_temp = (len(my_current_line)+1)*[0]
        for location in range(0,len(my_current_line)):
            my_temp[location] += my_current_line[location]
            my_temp[location+1] += my_current_line[location]
        my_pascal_triangle.append(my_temp)
        x += 1
    return my_pascal_triangle
mytime = time.time()
f = open("D:\Python_Github\Squarefree_Binomial_Coefficients\Prime_numbers.txt","r")
my_prime_numbers = eval(f.readline())
print(time.time()-mytime)
def check_divisible_prime(n):
    location = 0
    while True:
        temp = (my_prime_numbers[location])**2
        if n < temp:
            return True
        else:
            if n%temp == 0:
                return False
        location += 1
def add_total(pascal):
    total = 0
    memo = []
    for x in pascal:
        for number in x:
            if number in memo:
                continue
            elif check_divisible_prime(number):
                total += number
                memo.append(number)
    return total
print(add_total(create_pascal(51)))
print(time.time()-mytime)
