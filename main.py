import folium
import streamlit as st
from folium.plugins import Draw
from streamlit_folium import st_folium

m = folium.Map(location=[39.949610, -75.150282], zoom_start=5)

# 描画プラグインを有効化
Draw(export=True).add_to(m)

# 地図データの描画
st_data = st_folium(m, width=700, height=500)

# 現在の状態を出力
st.write(st_data)