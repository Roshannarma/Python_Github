import numpy as np
def print_nicely(array):
    for x in array:
        temp = ""
        for z in x:
            y = len(z)
            temp += z + " "*(9-y)
        print("[" + temp + "]")
    print("")
def basic_check(full_list):
    single,multiple = [],[]
    for y in full_list:
        if len(y)==1:
            single.append(y)
        else:
            multiple.append(y)
    for i,number in enumerate(full_list):
        if number not in single:
            for check in single:
                if check in number:
                    location = number.index(check)
                    number = number[0:location] + number[location+1:]
                    full_list[i] = number
    return full_list


def multiple_of_same_solver(full_list):
    double = []
    for i,y in enumerate(full_list):
        if len(y) == 2 and y in full_list[i+1:]:
            double.append(y)
    if double != []:
        for x in double:
            for check in x:
                for i,number in enumerate(full_list):
                    if check in number and number not in double:
                        location = number.index(check)
                        number = number[0:location] + number[location+1:]
                        full_list[i] = number
    return full_list
def only_one(full_list):
    for x in range(1,10):
        temp = []
        x = str(x)
        for i,y in enumerate(full_list):
            if x in y:
                temp.append(i)
        if len(temp) == 0:
            print("error in code or problem")
        if len(temp) == 1:
            full_list[temp[0]] = x
        # print(temp)
    return full_list

def solve_starting(my_array):
    for x in range(0,9):
        for y in range(0,9):
            if my_array[x][y] == " ":
                my_array[x][y] = "123456789"
    print(my_array)
    return my_array

def solvers(my_array,loop=0):
    if loop == 0:
        my_array = solve_starting(my_array)
    elif loop >= 15:
        print("took too long")
        return my_array
    done = True
    for x in range(0,9):
        for y in range(0,9):
            if len(my_array[x][y]) != 1:
                done = False
    if done:
        print("DONE")
        print(loop)
        return my_array
    else:
        for x in range(0,9):
            basic_check(my_array[x])
            multiple_of_same_solver(my_array[x])
            only_one(my_array[x])
        for y in range(0,9):
            temp = []
            for z in my_array:
                temp.append(z[y])
            first = basic_check(temp)
            first = multiple_of_same_solver(first)
            first = only_one(first)
            for i,z in enumerate(my_array):
                z[y] = first[i]
            temp = []
        for a in range(1,4):
            s1 = slice((3*a)-3,3*a)
            for b in range(1,4):
                temp = []
                for loc,c in enumerate(my_array[s1]):
                    s2 = slice((3*b)-3,3*b)
                    temp.extend(c[s2])
                basic_check(temp)
                multiple_of_same_solver(temp)
                only_one(temp)
                for d in range(0,3):
                    for e in range(0,3):
                        my_array[3*a + d - 3][3*b + e - 3] = temp[3*d + e]

    # print_nicely(my_array)
    return solvers(my_array,loop+1)
if __name__ == "__main__":
    array = [['8', ' ', ' ', '7', '1', '5', ' ', ' ', '4'],
    [' ', ' ', '5', '3', ' ', '6', '7', ' ', ' '],
    ['3', ' ', '6', '4', ' ', '8', '9', ' ', '1'],
    [' ', '6', ' ', ' ', '5', ' ', ' ', '4', ' '],
    [' ', ' ', ' ', '8', ' ', '7', ' ', ' ', ' '],
    [' ', '5', ' ', ' ', '4', ' ', ' ', '9', ' '],
    ['6', ' ', '9', '5', ' ', '3', '4', ' ', '2'],
    [' ', ' ', '4', '9', ' ', '2', '5', ' ', ' '],
    ['5', ' ', ' ', '1', '6', '4', ' ', ' ', '9']]
    mine = solvers(array)
    print_nicely(mine)
