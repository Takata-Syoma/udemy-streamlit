import streamlit as st
import time

st.title('**i-STOCK β**\n')
st.markdown("______________________")

'Loading...'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'Complete!!'


text = st.text_input('・コンビニ名を入力してください')
'コンビニ名：', text
st.markdown("______________________")

radius = st.slider('・検索範囲を設定してください、お近くの店舗を検索します。', 0, 10, 5)
'検索範囲：', radius, 'km'
st.markdown("______________________")


category = st.selectbox(
    '・商品のカテゴリーを選択してください',
    ['おにぎり',
     'お寿司',
     'お弁当',
     'ドリンク',
     'サンドウィッチ・ロールパン',
     'パン','そば・うどん・中華麺',
     'スパゲッティ・パスタ',
     'グラタン・ドリア',
     '惣菜',
     'サラダ',
     'スイーツ',
     'アイス',
     '菓子類',
     '日用雑貨',
     '一番くじ',
     'その他'
     ]
    )
'カテゴリー：', category
st.markdown("______________________")

item = st.text_input('・商品名を入力してください')
'商品名：', item, 'の在庫状況を検索します。'
st.markdown("______________________")

st.write(text, '店に、', item, 'は、',len(item),'個あります！')

