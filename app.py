import random
import streamlit as st

#ジャンケンの手を表す定数
ROCK = "グー"
SCISSORS = "チョキ"
PAPER = "パー"

st.title("じゃんけんアプリ")

#プレイヤーの手を選択
player_hand = st.selectbox("あなたの手を選択してください", ["グー", "チョキ", "パー"])

#コンピュータの手をランダムに選ぶ
computer_hand = random.choice(["グー", "チョキ", "パー"])

import time
lateset_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    lateset_iteration.text(f'コンピュータ考え中{i+1}%')
    bar.progress(i+1)
    time.sleep(0.03)

#じゃんけんの勝敗を判定
if player_hand == computer_hand:
    result = "あいこ"
elif (player_hand == "グー" and computer_hand == "チョキ") or (player_hand == "チョキ" and computer_hand == "パー") or (player_hand == "パー" and computer_hand == "グー"):
    result = "あなたの勝ちです"
else:
    result = "あなたの負けです"

#結果を表示
st.write(f"あなた:{player_hand}" )
st.write(f"コンピュータ:{computer_hand}")
st.write(f"結果:{result}")
