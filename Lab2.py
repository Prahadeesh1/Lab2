
#def calculate_bmi(height, weight):
 #   print("Height = " + str(height))
  #
   # bmi = int(weight/(height*height))
    #if (bmi<18.5):
#        print(bmi)
 #       print("Underweight")
#    elif (18.5<bmi>25.0,bmi == 18.5, bmi ==25.0):
#        print(bmi)
#        print("Normal weight")
#    else:
#        print(bmi)
#        print("Overweight")
#calculate_bmi(weight=57, height=1.73)


import statistics




def main():
    display_main_menu()
    temp = get_user_input()
    print(calc_average_temperature(temp))
    print( calc_min_max_temperature(temp))
    print(calc_median_temperature(temp))
    


def display_main_menu():
    print("Enter some numbers separated by commas(e.g. 5, 67, 32)")

def get_user_input():
    user = input()
    #split the string into a list
    user_input = user.split(",")
    for i in range(len(user_input)):
        user_input[i] = float(user_input[i])
    return user_input




def calc_average_temperature(tempraturelist):
    total = 0
    for x in tempraturelist:
        total += x
    return total / len(tempraturelist)

def calc_min_max_temperature(tempraturelist):
    sort_temperature(tempraturelist)
    min = tempraturelist[0]
    max = tempraturelist[-1]
    return [min, max]

def sort_temperature(list):
    list.sort()

def calc_median_temperature(list):
    median = statistics.median(list)

    return median


if __name__ == "__main__":
    main()





    




