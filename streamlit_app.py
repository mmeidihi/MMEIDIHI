import streamlit as st 
import pandas as pd 
#import requests
#from st_aggrid import AgGrid

house = pd.read_csv('house_clean.csv')

def main() : 
  st.write('Minimal Example')

if _name_ == '_main_' : 
  main()

def main() : 
  st.header('Halaman Streamlit Alif')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')

  st.dataframe(house)
if _name_ == '_main_' : 
  main()