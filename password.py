# パスワードを生成するプログラム

import random
import string


def generate_password(length):
    # 生成するパスワードの長さを指定
    password_length = length

    # パスワードに含める文字の種類(英数字と記号）を指定
    password_characters = string.ascii_letters + string.digits + string.punctuation

    # ランダムにパスワードを生成する
    password = ''.join(random.choice(password_characters) for i in range(password_length))

    # 生成したパスワードを返す
    return password


# 生成したいパスワードの長さを尋ねる
print('何文字でパスワードを作りますか？(半角数字で入力して下さい):')

# 数字を受け取る
length = int(input())

# 関数を呼び出してパスワードを生成する
password = generate_password(length)

# 生成したパスワードを表示する
print(password)