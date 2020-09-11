import unittest

class primecheckr(unittest.TestCase):
    def check_prime(self,num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, "is not a prime number")
                else:
                    print(num, "is a prime number")

        else:
            print(num, "is not a prime number")
    def mysql(self):
        self.assertEquals(check_prime(4),"is not a prime number")
        self.assertTrue(check_prime(4))
        result = "is not a prime number"
        self.assertEquals(result,"is not a prime number")
        
        
        
        
    def ansckr(self):
        check_prime(2)
        result = "is a prime number"
        self.assertEquals(result,"is a prime number")
        
if __name__ == '__main__':
         unittest.main()
