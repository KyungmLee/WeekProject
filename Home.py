import streamlit as st

st.set_page_config(
    page_title='Korea Historic Sites',
    page_icon='🗿',
    layout='wide',
    initial_sidebar_state='expanded')

st.title('Historic Sites in South Korea')
st.subheader('대한민국 **역사 명소** 방문자를 위한 가이드', divider='rainbow')


def centered_text(text):
   st.markdown(f"<div style='text-align: center;'>{text}</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
   centered_text("<b>역사 명소 검색<b>")
   st.image('data/그림1.png',width=250)
   st.write('유형별로 명소를 검색하여 지동상의 분포를 확인할 수 있습니다.')

with col2:
   centered_text("<b>각 명소의 기본정보 제공<b>")
   st.image('data/그림3.png',width=250)
   st.write('명소에 대한 사진과 설명이 함께 제공되며, 최근 6년간의 입장객 추이를 확인할 수 있습니다.')

with col3:
   centered_text("<b>리뷰를 한눈에<b>")
   st.image('data/그림2.png',width=250)
   st.write('명소마다 구글 리뷰를 기반으로 한 워드클라우드가 제공됩니다.')

st.subheader('활용데이터',divider='red')
st.write('''
- **역사 명소** : 문화체육관광부/한국문화관광연구원이 제공하는 주요 관광지점 중 '문화' 유형에 해당하는 장소를 기반으로 선정
- **관광 지점** : 지자체 관광 진흥 정책상 중요하다고 판단하는 대표 지점으로써 관광목적의 비일상적 이용이 주된 목적인 시설 또는 공간
- **역사 명소의 유형** : 한국문화정보원에서 제공되는 '국내 지역별 유적지' 데이터를 기반으로 분류함  
(궁궐/종묘, 왕릉/고분, 보물, 국보, 유명사적/유적지, 비/탑/문/각, 서원/향교/서당, 고택/생가/민속마을, 유명사찰, 성/성터, 천연기념물 등 총 11가지 분류)
''')
st.write('Tour API에 등록된 기본 정보와 주요 관광지점 입장객 통계에서 제공되는 연도별 데이터 중 ***2018~2023년의 데이터***를 활용')

#center>가운데</center>


st.write('')
st.subheader('바로가기',divider='gray')
st.page_link('pages/01_전국.py', label='***전국의 역사 명소 정보***', icon='🗺️')
st.page_link('pages/02_지역.py', label='***각 지역 역사 명소 정보***', icon='🏛️')