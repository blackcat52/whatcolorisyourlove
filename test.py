import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import random

# GitHub: https://github.com/andfanilo/streamlit-lottie
### --- FUNCTIONS
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
heart = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_izvn2khx.json")
heart2 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_goj7emul.json")

st.set_page_config('What Color Is Your Love?')

### --- TITLE AND ANIMATION
col1, col2 = st.columns(2)
with col1:
    st.title('What Color Is Your Love?')
    st.write('Take our "What Color Is Your Love?" Test and get a “freakishly accurate” description of who you are and why you do things the way you do.')

with col2:
    st_lottie(
        heart2,
        speed=1,
        reverse=False,
        quality="low", # medium , high
        height=260,
        width=None,
        key=None,
)

### --- QUESTIONS --- ###
st.write('1. How do you feel about loving someone your entire life.')
st.checkbox('Feels like I could probably do it.')
st.checkbox('Feels impossible, realistically speaking.')
st.write('')
        
st.write('2. How do you react when someone seems to have a crush on you?')
st.checkbox("You're unable to sleep, heart fluttering and thoughts racing.")
st.checkbox("Nah, can't be. You have a good night's sleep and wake up refreshed.")
st.write('')

st.write("3. If you have to date one of the two, you choose...")
st.checkbox("Someone who calls you 100 times if you don't call them before you go to bed.")
st.checkbox("Someone who you can't get hold of because of how busy they are, but surprises you with with an unexpected gift or date.")
st.write('')

st.write("4. When you go on a blind date, you...")
st.checkbox("Ask about their interest or hobbies first.")
st.checkbox("Wait until they start speaking first.")
st.write('')

st.write("5. When your partner is out drinking and won't answer your calls or messages, you...")
st.checkbox("Get worried, but try to remain calm thinking of how they usually get when they're drunk.")
st.checkbox("Get anxious and restless. worried about what they might have gotten themselves into.")
st.write('')

st.write("6. How do you react when your partner gets slightly jealous about your friendship with another guy/girl?")
st.checkbox("Did I hurt their feelings a lot? I guess I'll see my friend a bit less.")
st.checkbox("I guess I kind of understand, but that doesn't mean I have to see my friend anyy less.")
st.write('')

st.write("7. Between the two, which is worse?")
st.checkbox("A partner with zero empathy.")
st.checkbox("A partner who doesn't try to break their bad habits.")
st.write('')

st.write("8. When you see a bunch of people gathered around when you're on a date, what do you do?")
st.checkbox("Maybe there's a celebrity! We have to check it out.")
st.checkbox("It's just noise and people. we continue on our way.")
st.write('')

st.write("9. How do you react when you see past conversations with your partner on a messenger app?")
st.checkbox("We were so cute back then lol. I enjoy looking back ar our past conversations.")
st.checkbox("Why did i say this! I pull my hairs out from embarrassment.")
st.write('')

st.write("10. How do you react when your partner looks down with no particular reason?")
st.checkbox("Is something bothering them? I worry and feel down with them.")
st.checkbox("Sugar and sweets cures all ills! I take them to a cafe with great food.")
st.write('')

### --- RANDOM COLOR
colors = ["Blue", "Red", "Yellow", "Orange", "Purple", "Green"]
color = random.choice(colors)

if st.button('Submit'):
    st.success(f'Your color is {color}. Click below for your full report.')
    here = st.markdown('<a target="_blank" href="https://www.youtube.com/watch?v=dQw4w9WgXcQ/">Click Here</a>', unsafe_allow_html=True)

st_lottie(
        heart,
        speed=3,
        reverse=False,
        quality="low", # medium , high
        height=300,
        width=None,
        key=None,
)
