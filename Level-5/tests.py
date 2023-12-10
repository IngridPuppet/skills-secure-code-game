import unittest
import code as c

class TestCrypto(unittest.TestCase):

    # verifies that hash and verification are matching each other
    def test_1(self):
        rd = c.Random_generator()
        bcrypter = c.bcrypt_hasher()
        pass_ver = bcrypter.password_verification("abc", bcrypter.password_hash("abc",rd.generate_salt()))
        self.assertEqual(pass_ver, True)

if __name__ == '__main__':
    unittest.main()
