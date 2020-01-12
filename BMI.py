class BMI:

    @staticmethod
    def calcBMI(height, weight):

        if type(height) == str or type(weight) == str:
            return -1
        elif height < 0 or weight < 0:
            return -1
        else:
            return weight / (height**2)

    @staticmethod
    def answerBMI(bmiValue):

        if type(bmiValue) == str:
            return "Error"
        elif bmiValue < 0:
            return "Error"
        elif 0 <= bmiValue < 18.5:
            return "Underweight"
        elif 18.5 <= bmiValue < 25:
            return "Ok weight"
        elif 25 <= bmiValue <= 29.9:
            return "Overweight"
        elif 30 <= bmiValue <= 34.9:
            return "Obese Class 1"
        elif 35 <= bmiValue <= 39.9:
            return "Obese Class 2"
        else:
            return "Obese Class 3"
