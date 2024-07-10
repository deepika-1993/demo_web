import streamlit as st

st.title("welcome to website")
st.header("front end developer")
st.header("java ,css")
st.markdown("I love HtMl")
st.code("""for in range (1,5,1):
        print("Hello")
                  """)

name = st.text_input("Enter your name:")
fname = st.text_input("Enter your Father name:")
adr = st.text_area("Enter your text:")
classdata = st.selectbox("Enter your class:",(1,2,3,4,5))

button = st.button("done")
if button :
    st.markdown(f"""
    Name :{name}
    Father name :{fname}
    address :{adr}
    class :{classdata}
    """)











