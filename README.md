# ファイルの説明

## password.py
- ターミナル上で実行する
    - 実行するとパスワードの長さを尋ねられるので、半角数字で入力する
    - 生成されたパスワードが表示される

## web_passgeneratere.py
password.pyの改良版（streamlitを利用しWebアプリにした）
#### [パスワード作成アプリ](https://norma2627-password-generater-web-passgenerater-1775uq.streamlit.app/)

#### [streamlitの初期設定](https://docs.streamlit.io/library/get-started/installation#install-streamlit-on-macoslinux)
- streamlit run web_passgenerater.pyで動作させる
    - ブラウザでポート8501に接続(デフォルトのポートが8501)
    - パスワードの長さと使用する文字の種類を選択する
    - パスワードを作成するのボタンをクリックする
    - 生成されたパスワードが表示される
