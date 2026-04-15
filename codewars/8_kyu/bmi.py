def bmi(weight, height):
    calc = weight / (height ** 2)

    if calc <= 18.5:
        return "Underweight"
    elif calc <= 25.0:
        return "Normal"
    elif calc <= 30.0:
        return "Overweight"
    else:
        return "Obese"