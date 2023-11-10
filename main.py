import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
st.title("1000 SLAMA")
df =pd.read_excel("data.xlsx",engine='openpyxl')
govers=df['governrate'].unique()

govern_in=st.sidebar.selectbox("اخنر المحافظة",options=govers)
govdf=df.query("governrate == @govern_in ") #


areas=govdf['area'].unique()

area_in=st.sidebar.selectbox("اخنر المنطقة",options=areas)


types=govdf['service_provider_type'].unique()
serv_type=st.sidebar.selectbox("نوع الخدمة",options=types)
specials=govdf['speciality'].unique()
specials_in=st.sidebar.selectbox("التخصص",options=specials)

# print(df)
newdf=govdf.query("area == @area_in and  service_provider_type==@serv_type") #
st.write(newdf)
