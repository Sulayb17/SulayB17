import unittest #import class module





############################################


class TestStringMethods(unittest.TestCase):#Create class from the imports

   #------------------------------Create 3 different functions

    def test_upper(self):#Creating a function for the test calling it self
        self.assertEqual('foo'.upper(), 'FOO')#Check if its uppercase


    def test_isupper(self):#Create another function
        self.assertTrue('FOO'.isupper())#Checks if it has an actual upper case
        self.assertFalse('Foo'.isupper())#Checks the upper case

    def test_split(self):#Create  function
        s = 'hello world'#Creating a variable called s
        self.assertEqual(s.split(), ['hello', 'world']}#Pass in string into brackets

#Check that s.split fails when the seperator is not a string
                         
    with self.assertRaises(TypeError):
        s.split(2)

if __name__ == '__main__':#Call the main function
    unittest.main()#Calls function
