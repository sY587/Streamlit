import streamlit at st

st.title("My First App")

name = st.text_input("What is your name?")

if name:
  st.write(f"Hello, {name}!")
  
