import unittest
from APITests import APITestSuit 

if __name__ == "__main__":
    # Create test suite
    suite = unittest.TestSuite()
    # Add test cases
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(APITestSuit.TestAPI))
    # Run test suite
    unittest.TextTestRunner().run(suite)