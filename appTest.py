import unittest
import mainApp as app

class TestMyApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app
    
    def test_show(self):
        list = ["Dima", "Petro"]
        self.assertEqual(app.funcForTest("Fedir", list), ["Dima", "Petro", "Fedir"])

if __name__ == '__main__':
    unittest.main()