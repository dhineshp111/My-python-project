import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

crypto = pd.read_csv("C:/Users/Dinakar MMD/Downloads/crypto-23.csv")

fig, ax=plt.subplots()

ax.plot(crypto['Month'], crypto['BTC'])
ax.plot(crypto['Month'], crypto['ETH'])
plt.xlabel("Month")
plt.ylabel("Closing value (USD)")
plt.title("BTC/ETH performance")
plt.legend(['BTH','ETH'])
st.pyplot(fig)
