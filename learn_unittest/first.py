import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('shubhi'.upper(),"SHUBHI")

    def test_isupper(self):
        self.assertFalse("Shubhi".isupper())
        self.assertTrue("SHUBHI".isupper())

    def test_split(self):
        self.assertEqual("Shubhi Goyal".split(),["Shubhi","Goyal"])
        with self.assertRaises(TypeError):
            "shubhi goyal".split(2)

def suite():
    s=unittest.TestSuite()
    s.addTest(TestStringMethods("test_upper"))
    s.addTest(TestStringMethods("test_isupper"))
    return s

if __name__=="__main__":
    runner=unittest.TextTestRunner()
    runner.run(suite())