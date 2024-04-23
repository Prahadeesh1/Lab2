def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = int(weight/(height*height))
    if (bmi<18.5):
        print(bmi)
        print("Underweight")
    elif (18.5<bmi>25.0,bmi == 18.5, bmi ==25.0):
        print(bmi)
        print("Normal weight")
    else:
        print(bmi)
        print("Overweight")
    

    

   



calculate_bmi(weight=57, height=1.73)






    




