"""
料理タブの表示処理。（A案: st.tabs から呼ばれる想定）

決め事:
- 料理は「作った日」ではなく、食品と同じ "期限" というキーで持つ
- 登録時に 今日 + 2日 を計算して、それを期限として保存する（日数は2日で固定、可変にしない）
- 表示するだけ。「食べきった」「捨てた」ボタンは作らない
- 期限を過ぎた料理は表示フィルタで自動的に隠す。データからは消さない
"""

import streamlit as st
from datetime import date, timedelta
import storage

def show_dishes(items):
    """
    料理の登録フォームと一覧を表示する。

    引数の想定:
    - items: 食品・料理すべてを含む1つのリスト（st.session_state で共有しているもの）

    ヒント:
    - 入力: st.text_input（料理名）だけでよい。期限日はユーザーに入力させない
    - 期限の計算: date.today() + timedelta(days=2)
    - 新しく作る辞書には "種類": "料理" を必ず入れる
    - 登録後は storage.save_items(items) を呼んで保存する
    - 表示前に、items から "種類" が "料理" かつ 期限 >= date.today() のものだけに絞り込む
      （期限切れのものはここで弾く。データからの削除はしない）
    - 期限が近い順に並べる: sorted(絞り込んだリスト, key=lambda item: item["期限"])
    - 「あと何日で食べきる必要があるか」を出すには (item["期限"] - date.today()).days
    """
    with st.form("料理登録ボタン"):
        name=st.text_input("料理の名前を入力してください")
        submitted=st.form_submit_button("登録")

    if submitted and name:
        expiration=date.today() + timedelta(days=2)
        items.append({"種類":"料理","名前":name,"期限":expiration})
        storage.save_items(items)

    dishes_items=[item for item in items if item["種類"]=="料理" and item["期限"] >= date.today()]
    show_dishes_items=sorted(dishes_items, key=lambda item:item["期限"])
    for item in show_dishes_items:
        st.write(item["名前"], item["期限"], f"あと{(item["期限"]-date.today()).days}日です")