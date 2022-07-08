import streamlit as st
import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


st.title('My Parents New Healthy Diner')

st.header('Breakfast Favorites')
st.markdown(':grapes: Omega 3 & Blueberry Oatmeal')
st.markdown(':cup_with_straw: Kale, Spinach & Rocket Smoothie')
st.markdown(':chicken: Hard-Boiled Free-Range Egg')
st.markdown(':avocado::bread: Avacado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
st.dataframe(my_fruit_list)
