import unittest
from src.BMI import BMI

class BMITesing(unittest.TestCase):

    def test_BMIcalc(self):

        stub1_height = "ass"
        stub2_height = -1
        stub3_height = 1.6

        stub4_weight = "ss"
        stub5_weight = -1
        stub6_weight = 80

        excepted1 = -1
        excepted2 = -1
        excepted3 = -1
        excepted4 = -1
        excepted5 = -1
        excepted6 = -1
        excepted7 = -1
        excepted8 = -1
        excepted9 = stub6_weight / (stub3_height**2)

        #action
        result1 = BMI.calcBMI(stub1_height, stub4_weight)
        result2 = BMI.calcBMI(stub1_height, stub5_weight)
        result3 = BMI.calcBMI(stub1_height, stub6_weight)
        result4 = BMI.calcBMI(stub2_height, stub4_weight)
        result5 = BMI.calcBMI(stub2_height, stub5_weight)
        result6 = BMI.calcBMI(stub2_height, stub6_weight)
        result7 = BMI.calcBMI(stub3_height, stub4_weight)
        result8 = BMI.calcBMI(stub3_height, stub5_weight)
        result9 = BMI.calcBMI(stub3_height, stub6_weight)

        self.assertEqual(result1, excepted1)
        self.assertEqual(result2, excepted2)
        self.assertEqual(result3, excepted3)
        self.assertEqual(result4, excepted4)
        self.assertEqual(result5, excepted5)
        self.assertEqual(result6, excepted6)
        self.assertEqual(result7, excepted7)
        self.assertEqual(result8, excepted8)
        self.assertEqual(result9, excepted9)

    def test_BMI_answer(self):

        stub1 = -2
        stub2 = 'dsdsds'

        stub3 = 0
        stub4 = 18.5
        stub5 = 17

        stub6 = 19
        stub7 = 20
        stub8 = 24.9

        stub9 = 25
        stub10 = 28
        stub11 = 29.9

        stub12 = 30
        stub13 = 32
        stub14 = 34.9

        stub15 = 35
        stub16 = 37
        stub17 = 39.9

        stub18 = 40
        stub19 = 43

        excepted1 = "Error"
        excepted2 = "Error"
        excepted3 = "Underweight"
        excepted4 = "Ok weight"
        excepted5 = "Underweight"
        excepted6 = "Ok weight"
        excepted7 = "Ok weight"
        excepted8 = "Ok weight"
        excepted9 = "Overweight"
        excepted10 = "Overweight"
        excepted11 = "Overweight"
        excepted12 = "Obese Class 1"
        excepted13 = "Obese Class 1"
        excepted14 = "Obese Class 1"
        excepted15 = "Obese Class 2"
        excepted16 = "Obese Class 2"
        excepted17 = "Obese Class 2"
        excepted18 = "Obese Class 3"
        excepted19 = "Obese Class 3"

        result1 = BMI.answerBMI(stub1)
        result2 = BMI.answerBMI(stub2)
        result3 = BMI.answerBMI(stub3)
        result4 = BMI.answerBMI(stub4)
        result5 = BMI.answerBMI(stub5)
        result6 = BMI.answerBMI(stub6)
        result7 = BMI.answerBMI(stub7)
        result8 = BMI.answerBMI(stub8)
        result9 = BMI.answerBMI(stub9)
        result10 = BMI.answerBMI(stub10)
        result11 = BMI.answerBMI(stub11)
        result12 = BMI.answerBMI(stub12)
        result13 = BMI.answerBMI(stub13)
        result14 = BMI.answerBMI(stub14)
        result15 = BMI.answerBMI(stub15)
        result16 = BMI.answerBMI(stub16)
        result17 = BMI.answerBMI(stub17)
        result18 = BMI.answerBMI(stub18)
        result19 = BMI.answerBMI(stub19)

        self.assertEqual(result1,excepted1)
        self.assertEqual(result2,excepted2)
        self.assertEqual(result3,excepted3)
        self.assertEqual(result4,excepted4)
        self.assertEqual(result5,excepted5)
        self.assertEqual(result6,excepted6)
        self.assertEqual(result7,excepted7)
        self.assertEqual(result8,excepted8)
        self.assertEqual(result9,excepted9)
        self.assertEqual(result10,excepted10)
        self.assertEqual(result11,excepted11)
        self.assertEqual(result12,excepted12)
        self.assertEqual(result13,excepted13)
        self.assertEqual(result14,excepted14)
        self.assertEqual(result15,excepted15)
        self.assertEqual(result16,excepted16)
        self.assertEqual(result17,excepted17)
        self.assertEqual(result18,excepted18)
        self.assertEqual(result19,excepted19)


if __name__ == '__main__':
    unittest.main()
