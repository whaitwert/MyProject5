import streamlit as st
st.title("Въвеждане на оценки")
theory = st.number_input("Теория (0-50):", value=0)
practical = st.number_input("Практика (0-50):", value=0)
if theory > 50 or practical > 50:
    st.warning("One of the scores is too high! Please enter a value up to 50.")
else:
    total = theory + practical
    st.write(f"Your total score is: **{total}**")
