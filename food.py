"""
食品タブの表示処理。（A案: st.tabs から呼ばれる想定）

決め事:
- 食品の登録: 名前 + 賞味期限を入力する
- 表示: 期限が近い順に並べる
"""

import streamlit as st
from datetime import date
import storage
def show_food(items):
    """
    食品の登録フォームと一覧を表示する。

    引数の想定:
    - items: 食品・料理すべてを含む1つのリスト（st.session_state で共有しているもの）

    ヒント:
    - 入力: st.text_input（名前）、st.date_input（賞味期限）
    - まとめて送信したいなら st.form + st.form_submit_button が便利
    - 新しく作る辞書には "種類": "食品" を必ず入れる（他の種類と区別するため）
    - 登録後は storage.save_items(items) を呼んで保存する
    - 表示前に、items から "種類" が "食品" のものだけに絞り込む
      （リスト内包表記、または filter() を使う）
    - 期限が近い順に並べる: sorted(絞り込んだリスト, key=lambda item: item["期限"])
    - 一覧の見せ方は st.write / st.dataframe / for文中で st.write するなど自由でよい
    """
    with st.form("食品登録ボタン"):
        name=st.text_input("食品の名前を入力してください")
        expiration=st.date_input("食品の賞味期限(消費期限)を入力してください")
        submitted=st.form_submit_button("登録")
    
    if submitted and name and expiration:
        items.append({"種類":"食品","名前":name,"期限":expiration})
        storage.save_items(items)

    food_items=[item for item in items if item["種類"]=="食品" and item["期限"]>=date.today()]
    show_food_items=sorted(food_items, key=lambda item: item["期限"])
    for item in show_food_items:
        st.write(item["名前"], item["期限"], f"あと{(item["期限"]-date.today()).days}日です")