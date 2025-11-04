import streamlit as st

st.set_page_config(
    page_title="Project Orbit",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Project Orbit")
st.header("Welcome to Project Orbit Dashboard")

st.write("This is a basic Streamlit application.")

# Simple interactive elements
name = st.text_input("Enter your name:", value="")

if name:
    st.success(f"Hello, {name}!")

# Display some example data
st.subheader("Sample Data")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Users", "1,234", "+12%")

with col2:
    st.metric("Revenue", "$45,678", "+8%")

with col3:
    st.metric("Growth", "23%", "+5%")

# Simple button
if st.button("Click me!"):
    st.balloons()
    st.info("Button clicked!")