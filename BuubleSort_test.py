import unittest
from src.BubbleSort import BubbleSortArray


class BubbleSortTest(unittest.TestCase):

    def test_bubbleSort(self):

        arr1 = [0,1,2,3,4]
        arr2 = [50,40,30,1]
        arr3 = []
        arr4 = "dsds"
        arr5 = 222
        arr6 = [20,21,22,40,2,3,4,7,41,42]
        arr7 = [1]
        arr8 = [1,2]
        arr9 = [6,6]
        arr10 = [6,1,6]

        excepted1 = [0,1,2,3,4]
        excepted2 = [1,30,40,50]
        excepted3 = "The array is empty!"
        excepted4 = "Error"
        excepted5 = "Error"
        excepted6 = [2,3,4,7,20,21,22,40,41,42]
        excepted7 = 5
        excepted8 = 4
        excepted9 = 10
        excepted10 = 1
        excepted11 = 2
        excepted12 = [1]
        excepted13 = [1,2]
        excepted14 = [6,6]
        excepted15 = [1,6,6]

        result1 = BubbleSortArray.soringByBubbleSort(arr1)
        result2 = BubbleSortArray.soringByBubbleSort(arr2)
        result3 = BubbleSortArray.soringByBubbleSort(arr3)
        result4 = BubbleSortArray.soringByBubbleSort(arr4)
        result5 = BubbleSortArray.soringByBubbleSort(arr5)
        result6 = BubbleSortArray.soringByBubbleSort(arr6)
        result7 = len(BubbleSortArray.soringByBubbleSort(arr1))
        result8 = len(BubbleSortArray.soringByBubbleSort(arr2))
        result9 = len(BubbleSortArray.soringByBubbleSort(arr6))
        result10 = len(BubbleSortArray.soringByBubbleSort(arr7))
        result11 = len(BubbleSortArray.soringByBubbleSort(arr8))
        result12 = BubbleSortArray.soringByBubbleSort(arr7)
        result13 = BubbleSortArray.soringByBubbleSort(arr8)
        result14 = BubbleSortArray.soringByBubbleSort(arr9)
        result15 = BubbleSortArray.soringByBubbleSort(arr10)

        self.assertEqual(result1, excepted1)
        self.assertEqual(result2, excepted2)
        self.assertEqual(result3, excepted3)
        self.assertEqual(result4, excepted4)
        self.assertEqual(result5, excepted5)
        self.assertEqual(result6, excepted6)
        self.assertEqual(result7, excepted7)
        self.assertEqual(result8, excepted8)
        self.assertEqual(result9, excepted9)
        self.assertEqual(result10, excepted10)
        self.assertEqual(result11, excepted11)
        self.assertEqual(result12, excepted12)
        self.assertEqual(result13, excepted13)
        self.assertEqual(result14, excepted14)
        self.assertEqual(result15, excepted15)


if __name__ == '__main__':
    unittest.main()
