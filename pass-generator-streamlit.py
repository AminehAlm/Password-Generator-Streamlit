import streamlit as st
import string
import secrets
import math
from nltk.corpus import brown, stopwords



st.title("🔐 Password Generator")
st.markdown("<span style='color:#A2D2FF'>**Welcome to the Password Generator system!🌹**</span>", unsafe_allow_html=True)
passwordtype = {"Random Password", "Memorable Password", "Pincode"}
lettercase = ["Lowercase", "Uppercase", "Both of them"]
if 'password' not in st.session_state:
    st.session_state.password = ""
if 'entropy_value' not in st.session_state:
    st.session_state.entropy_value = 0
if 'char_set' not in st.session_state:
    st.session_state.char_set = ""
@st.cache_data
def load_words():
    words = brown.words()[:1000]
    exclude_words = stopwords.words('english')
    return [word for word in words if word.lower() not in exclude_words]    
words_list = load_words()
typeinput = st.radio("Which type of password do you prefer to be generated?", passwordtype)
if typeinput == "Random Password":
    st.markdown("----------------------------------------------")
    st.subheader("🌟 Random Password")
    length = st.slider("What is the length of your password?", 6, 50)
    number = st.checkbox("I want my password to be ONLY numbers.(0-9)")
    char = ""
    if number is True:
        char += string.digits
    if number is False:
        char += string.digits
        symbol = st.checkbox("Include symbols. (!@#$ etc.)")
        if symbol is True:
            char += string.punctuation
        letter = st.checkbox("Include letters. (A-Z, a-z)")
        if letter:
            case = st.radio("Which letter case do you want to include?", lettercase)
            if case == "Lowercase":
                char += string.ascii_lowercase
            elif case == "Uppercase":
                char += string.ascii_uppercase
            elif case == "Both of them":
                char += string.ascii_letters
    st.session_state.char_set = char
    if st.button("Generate Password"):
        if char:
            st.session_state.password = ''.join(secrets.choice(char) for _ in range(length))
            st.session_state.entropy_value = length * math.log2(len(char))
        else:
            st.error("❌ Select at least one character type!")
elif typeinput == "Pincode":
    st.markdown("----------------------------------------------")
    st.subheader("🌟 Pincode")
    length = st.slider("What is the length of your password?", 6, 50)
    char = ""
    char = string.digits
    if st.button("Generate Password"):
        if char:
            st.session_state.password = ''.join(secrets.choice(char) for _ in range(length))
            st.session_state.entropy_value = length * math.log2(len(char))
elif typeinput == "Memorable Password":
    st.markdown("----------------------------------------------")
    st.subheader("🌟 Memorable Password")
    length = st.slider("How many words do you want?", 4, 30)
    separator = st.text_input("Choose a separator symbol between your words:(e.g: @, $, etc.)", value=" ")
    dict = {'i': '!', 'o': '0', 'l': '|', 'a': '@'}
    symbol = st.checkbox("Replace some letters with symbols : 'i'--> '!', 'o'--> '0', 'l'--> '|', 'a'--> '@'")
    if st.button("Generate Password"):
        chosen_words = secrets.SystemRandom().sample(words_list, length)
        if len(chosen_words) > 1:
                chosen_words[1] = chosen_words[1].capitalize()
        password = separator.join(chosen_words)
        if symbol:
            password = password.translate(str.maketrans(dict))
        st.session_state.password = password       
        st.session_state.entropy_value = length * math.log2(len(words_list))

if st.session_state.password:  
    st.markdown("----------------------------------------------")      
    st.subheader("Generated Password")
    st.code(st.session_state.password)
    st.subheader("Entropy")
    st.write(f"{round(st.session_state.entropy_value, 2)} bits")
    if st.session_state.entropy_value < 40:
        st.warning("⚠️ Weak Password!")
        st.info("❗️Tip: Increase your length or add more character types")
    elif 40 <= st.session_state.entropy_value <= 50:
        st.info("🥈 Moderate Password")
    elif 50 <= st.session_state.entropy_value <= 60:
        st.success("🥇 Strong Password")
    else:
        st.success("🏆 Excellent! Very Strong Password 🎊")
        