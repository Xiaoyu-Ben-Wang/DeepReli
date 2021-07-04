import streamlit as st
import content

# CONFIG
st.set_page_config(layout='wide')


class Option:
    HOME = '🏠 Home'
    TEAM = '👨‍🔬 Meet The Team'
    RESEARCH = '🧪 Read Our Research'
    PROJECT = '🧠 DeepReli'
    CREDITS = '📝 Acknowledgments'


OPTIONS = [Option.HOME, Option.TEAM, Option.RESEARCH, Option.PROJECT, Option.CREDITS]

st.sidebar.title('🧭Navigation')
OPTION = Option.PROJECT
OPTION = st.sidebar.radio('', OPTIONS)

if OPTION == Option.HOME:
    content.homePage()
elif OPTION == Option.TEAM:
    content.teamPage()
elif OPTION == Option.PROJECT:
    content.deepReliPage()
