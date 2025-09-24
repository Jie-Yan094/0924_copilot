#建立一個名為 check_password_strength 的函式,接收一個 password 字串
#規則1. 檢查密碼長度是否大於等於8,如果是,分數+1
#規則2. 檢查密碼是否包含至少一個數字,如果是,分數+1
#規則3. 檢查密碼是否包含至少一個大寫字母,如果是,分數+1
#規則4. 檢查密碼是否包含至少一個小寫字母,如果是,分數+1
#規則5. 檢查密碼是否包含至少一個特殊符號,如果是,分數+1
#最後根據總分回傳強度等級:0-2分回傳"弱",3-4分回傳"中等”,5分回傳"強”
import re
import random
import string
import sys

def check_password_strength(password):
    """
    檢查密碼強度，根據長度、數字、大寫、小寫、特殊符號給分。
    0-2分回傳"弱"，3-4分回傳"中等"，5分回傳"強"。
    :param password: 欲檢查的密碼字串
    :return: 密碼強度等級（弱/中等/強）
    """
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    if score <= 2:
        return "弱"
    elif score <= 4:
        return "中等"
    else:
        return "強"

def generate_strong_password(length=12):
    """
    產生一組強密碼，包含大寫、小寫、數字、特殊符號，且長度預設12。
    :param length: 密碼長度，預設12
    :return: 強密碼字串
    """
    if length < 8:
        length = 8
    # 至少一個大寫、一個小寫、一個數字、一個特殊符號
    chars = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice('!@#$%^&*(),.?":{}|<>')
    ]
    # 剩下的隨機填滿
    all_chars = string.ascii_letters + string.digits + '!@#$%^&*(),.?":{}|<>'
    chars += random.choices(all_chars, k=length - 4)
    random.shuffle(chars)
    return ''.join(chars)

if __name__ == '__main__':
    """
    命令列執行邏輯：
    - 若有參數，檢查該密碼強度。
    - 若無參數，自動產生一組強密碼並顯示。
    """
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print(f"密碼強度: {check_password_strength(password)}")
    else:
        pwd = generate_strong_password()
        print(f"產生的強密碼: {pwd}")
        print(f"密碼強度: {check_password_strength(pwd)}")
        