"""
A案: st.tabs でタブを作り、food.py / dishes.py を呼ぶ構成。

streamlit run main.py で起動する。

ヒント:
- データの読み込みは起動時に一度だけ storage.load_items() で行う
- st.session_state に持たせておくと、tab の中でも食品・料理どちらからも
  同じリストを読み書きできる
  （例: "items" キーがまだ無ければ storage.load_items() の結果を入れる）
- st.tabs(["食品", "料理"]) はタブオブジェクトを2つ返す
- with タブオブジェクト: のブロックの中で food.show_food(...) / dishes.show_dishes(...) を呼ぶ
"""

import streamlit as st
import storage
import food
import dishes

st.title("アプリ")

# ここで st.session_state に items を読み込む処理を書く
st.session_state.setdefault("items", storage.load_items())

# 動作確認用の一時的なリセットボタン（本実装には不要なので、確認が終わったら消してOK）
if st.sidebar.button("items をリセット（デバッグ用）"):
    st.session_state["items"].clear()

# ここで st.tabs を作り、それぞれの中身で food.show_food() / dishes.show_dishes() を呼ぶ
tab1,tab2=st.tabs(["食品","料理"])
with tab1:
    food.show_food(st.session_state["items"])
with tab2:
    dishes.show_dishes(st.session_state["items"])