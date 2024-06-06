# streamlitを使用してブラウザ上に作成したパスワードを表示するプログラム


import streamlit as st
import random
import string

# タイトルを表示
st.title('パスワード作成ツール')

# 説明文の表示
st.header('使用方法')
st.info('1.パスワードの長さをスライダーで設定してください')
st.info('2.使用したい文字のチェックボックスを選択してください')
st.info('3.「パスワードを作成する」をクリックしてください')
st.text('\n')

# スライダーを作成し、パスワードの長さを選択する
length = st.slider('パスワードの長さ', 8, 30)

# チェックボックスを作成し、パスワードに含める文字を選択する
use_uppercase = st.checkbox('大文字を使用する')
use_lowercase = st.checkbox('小文字を使用する')
use_numbers = st.checkbox('数字を使用する')
use_symbols = st.checkbox('記号を使用する')

# パスワードを生成する
def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# 「パスワードを作成する」ボタンを作成し、ボタンがクリックされたらパスワードを生成して表示する
if st.button('パスワードを作成する'):
    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols)
    st.write('作成されたパスワード：', password)
