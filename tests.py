import unittest
import randomarray

# Class for testing should be in new file
class Testing(unittest.TestCase):
    def test_arrays(self):
        array_array = randomarray.rand_seq()
        for i in array_array:
            i.sort()
            self.assertEqual(i,[1,2,3,4,5,6,7,8,9,10])
            
unittest.main()