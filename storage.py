import os
import json
from datetime import date
"""
食品・料理データの読み込みと保存をまとめるファイル。（A案・B案 共通の内容）

決め事:
- 食品と料理は1つのリストにまとめる。各要素は dict で、"種類" キー（"食品" or "料理"）を持つ。
- 日付は datetime.date 型で扱うが、そのまま json.dump に渡すと TypeError になる。
  保存時は .isoformat() で文字列に、読み込み時は date.fromisoformat() で date 型に戻す。
- 保存先はローカルの JSON ファイル（例: data.json）。
"""

DATA_FILE = "data.json"  # 保存先のファイル名（好きな名前に変えてOK）


def load_items():
    """
    JSON ファイルからアイテムのリストを読み込んで返す。

    ヒント:
    - ファイルがまだ存在しない場合は空リスト [] を返す
      （os.path.exists() で確認する / try: ... except FileNotFoundError: の両方が使える）
    - json.load(f) でファイルの中身を Python のリストに変換できる
    - 読み込んだ各要素の "期限" は文字列になっているので、date.fromisoformat() で date 型に戻す
      （リスト全体を for でまわして、各 dict の "期限" を上書きするイメージ）
    """
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, encoding="utf-8") as f:
            items=json.load(f)
        for item in items:
            item["期限"] = date.fromisoformat(item["期限"])
        return items
    else:
        return []


def save_items(items):
    """
    アイテムのリストを JSON ファイルに書き込む。

    ヒント:
    - items の中の "期限" は date 型なので、そのまま json.dump するとエラーになる
    - 保存用に各要素のコピーを作り（例: dict(item)）、"期限" を .isoformat() で文字列にしてから
      新しいリストにまとめ、それを json.dump する
    - 元の items（呼び出し側が持っているリスト）を書き換えないように注意
    """
    save_list=[]
    item_copy={}
    for item in items:
        item_copy=dict(item)
        item_copy["期限"] = item_copy["期限"].isoformat()
        save_list.append(item_copy)
    with open(DATA_FILE,"w",encoding="utf-8") as f:
        json.dump(save_list,f,ensure_ascii=False)