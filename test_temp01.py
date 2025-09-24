import unittest
from temp01 import check_password_strength, generate_strong_password

class TestPasswordFunctions(unittest.TestCase):
    def test_check_password_strength_weak(self):
        self.assertEqual(check_password_strength('abc'), '弱')
        self.assertEqual(check_password_strength('1234567'), '弱')
        self.assertEqual(check_password_strength('abcdefg'), '弱')

    def test_check_password_strength_medium(self):
        self.assertEqual(check_password_strength('abcd1234'), '中等')
        self.assertEqual(check_password_strength('Abcdefgh'), '中等')
        self.assertEqual(check_password_strength('abcd!@#$'), '中等')

    def test_check_password_strength_strong(self):
        self.assertEqual(check_password_strength('Abcd1234!'), '強')
        self.assertEqual(check_password_strength('A1b2c3d4!'), '強')

    def test_generate_strong_password(self):
        pwd = generate_strong_password()
        self.assertEqual(len(pwd), 12)
        self.assertEqual(check_password_strength(pwd), '強')
        # 測試自訂長度
        pwd8 = generate_strong_password(8)
        self.assertEqual(len(pwd8), 8)
        self.assertEqual(check_password_strength(pwd8), '強')

if __name__ == '__main__':
    unittest.main()
