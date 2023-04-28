import unittest
import random

array = []

def rand_seq():
    for i in range(1,10):
        sub_array = []
        for j in random.sample(range(1,11),10-i):
            sub_array.append(j)
        array.append(sub_array)
        print(sub_array)
    return array
    


class Testing(unittest.TestCase):
    def test_arrays(self):
        array_array = rand_seq()
        for i in array_array:
            i.sort()
            self.assertEqual(i,[1,2,3,4,5,6,7,8,9,10])
            
unittest.main()