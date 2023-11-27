def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    height2 = height * height
    bmi = weight / height2
    if bmi < 18.5:
        print("underweight")
    elif 18.5 <= bmi <= 25:
        print("normal")
    else:
        print("overweight")
    print("BMI = " + str(bmi))


calculate_bmi(weight=57, height=1.73)
