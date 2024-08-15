import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Pratiksha Darade")
    content = """
    Hi, I am Pratiksha! I am a Computer Engineering graduate with a strong foundation in software development, programming languages, and problem-solving techniques. My academic experience, coupled with hands-on projects, has equipped me with skills in areas such as software development, mobile app development, and algorithm design. I am proficient in languages like Python, Java, with experience in tools such as Pycharm and Android Studio. I am passionate about applying my knowledge to real-world challenges and continuously learning to stay updated with emerging technologies.

I am eager to contribute my skills and grow in the field of software development, cybersecurity, or data engineering. I’m looking for opportunities that will allow me to work on innovative projects, collaborate with experienced professionals, and continue building my technical and problem-solving capabilities.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")