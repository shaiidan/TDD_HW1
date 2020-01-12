

class BubbleSortArray():

    @staticmethod
    def soringByBubbleSort(arr):

        if type(arr) != type([]):
            return "Error"

        n = len(arr)

        if n == 0:
            return "The array is empty!"

        # all array elements
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n - i - 1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr