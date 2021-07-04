import streamlit as st
from PIL import Image
import deepreli



def homePage():
    with open('./assets/md/home.md') as f:
        st.markdown(f.read(), True)


def teamPage():
    st.markdown("<h1 style='text-align: center;'>Meet the DeepReli Team!</h1><br>", unsafe_allow_html=True)
    b, c1, b, c2, b, c3, b, c4, b = st.beta_columns([1, 4, 1, 4, 1, 4, 1, 4, 1])
    kevinImg = Image.open('./assets/img/kevin.png')
    jessicaImg = Image.open('./assets/img/jessica.png')
    rafayImg = Image.open('./assets/img/rafay.png')
    benImg = Image.open('./assets/img/ben.png')

    c1.image(kevinImg, use_column_width=True)
    f1 = open('./assets/md/bio/kevin.md')
    c1.markdown(f1.read(), unsafe_allow_html=True)

    c2.image(jessicaImg, use_column_width=True)
    f2 = open('./assets/md/bio/jessica.md')
    c2.markdown(f2.read(), unsafe_allow_html=True)

    c3.image(rafayImg, use_column_width=True)
    f3 = open('./assets/md/bio/rafay.md')
    c3.markdown(f3.read(), unsafe_allow_html=True)

    c4.image(benImg, use_column_width=True)
    f4 = open('./assets/md/bio/ben.md')
    c4.markdown(f4.read(), unsafe_allow_html=True)

    f1.close()
    f2.close()
    f3.close()
    f4.close()


def readPaperPage():

    pass

def deepReliPage():
    st.markdown("<h1 style='text-align: center;'>Try Our DeepReli Model!</h1><br>", unsafe_allow_html=True)
    option = st.selectbox('Please Select An Input Option', ('By Text', 'By URL'))
    if option == 'By URL':
        url_input = st.text_input('Website URL')
        fetchurl = st.button('Fetch Article')
        if url_input or fetchurl:
            result = deepreli.getTextFromURL(url_input)
            st.write(result[0])
            if len(result[1]) > 750:
                st.write(result[1][:750]+"...")
            else:
                st.write(result[1])
            process = st.button("Run DeepReli")
            if process:
                predvalue = runDeepReli(result[1])
                st.markdown("<h4 style='text-align: center;'>DeepReli Score</h4>", unsafe_allow_html=True)
                if predvalue >= 0.75:
                    st.write("Article Looks Solid - DeepReli Score: {:.2}".format(predvalue))
                elif predvalue <= 0.25:
                    st.write("Article Looks Bad - DeepReli Score: {:.2}".format(predvalue))
                elif 0.5 <= predvalue <= 0.75:
                    st.write("Article Looks Ok - DeepReli Score: {:.2}".format(predvalue))
                elif 0.25 <= predvalue <= 0.5:
                    st.write("Article Looks Sus - DeepReli Score: {:.2}".format(predvalue))

    elif option == 'By Text':
        txt_input = st.text_area('Article Text', max_chars=5000, height=250)
        process = st.button("Run DeepReli")
        if txt_input and process:
            predvalue = runDeepReli(txt_input)
            st.markdown("<h2 style='text-align: center;'>DeepReli Score</h2>", unsafe_allow_html=True)
            if predvalue >= 0.65:
                st.markdown("<h2 style='text-align: center; color: #00FF00'>{:.2}</h2>".format(predvalue, 2),
                            unsafe_allow_html=True)
            elif predvalue <= 0.35:
                st.markdown("<h2 style='text-align: center; color: #FF4500'>{:.2}</h2>".format(predvalue),
                            unsafe_allow_html=True)
            elif 0.5 <= predvalue <= 0.65:
                st.markdown("<h2 style='text-align: center; color: #9ACD32'>{:.2}</h2>".format(predvalue),
                            unsafe_allow_html=True)
            elif 0.35 <= predvalue <= 0.5:
                st.markdown("<h2 style='text-align: center; color: #E1E100'>{:.2}</h2>".format(predvalue),
                            unsafe_allow_html=True)


@st.cache(suppress_st_warning=True, show_spinner=False)
def runDeepReli(txt):
    txt = deepreli.cleanText(txt)
    txt = deepreli.split_into_sentences(txt)
    predvalue = deepreli.predict(txt)
    return predvalue
