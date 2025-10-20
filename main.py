import streamlit as st
st.title('sumadora de numeros')

numero1 = st.number_input('numero 1', value=0)
numero2 = st.number_input('numero 2', value=0)

suma = numero1 + numero2

st.write(f'suma: {numero1} + {numero2} = {suma}')
