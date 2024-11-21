import streamlit as st

col1, col2, col3, col4 = st.columns(4)

with col1:
	st.header("A cat")
	st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
	st.header("A dog")
	st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
	st.header("A owl")
	st.image("https://static.streamlit.io/examples/owl.jpg")

with col4:
	st.header("A cat")
	st.image("https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")