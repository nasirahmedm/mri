import streamlit as st
import streamlit.components.v1 as components

# Set page title
st.set_page_config(
    page_title="BrainBuddy AI",
    page_icon="🧠",
    initial_sidebar_state="expanded",
)
st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
components.html(
    """
    <style>
        #effect{
            margin:0px;
            padding:0px;
            font-family: "Source Sans Pro", sans-serif;
            font-size: max(8vw, 20px);
            font-weight: 700;
            top: 0px;
            right: 25%;
            position: fixed;
            background: -webkit-linear-gradient(0.25turn,#FF4C4B, #FFFB80);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p{
            font-size: 2rem;
        }
    </style>
    <p id="effect">BrainBuddy AI</p>
    """,
    height=69,
)
st.sidebar.write('Sometimes, mental stress is also the reason behind tumors. Check your stress level to understand brain health')
st.sidebar.markdown(
    f'<a href="https://stress-level-detector.streamlit.app/" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: red; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Stress Level Detection</a>',
    unsafe_allow_html=True
)

def page_layout():
    st.write("BrainBuddy is an app that combines various ML models into one in order to determine if you have a disease, using CNN and MRIs of the patients. The app uses advanced algorithms to diagnose various diseases related to brain")
    
    st.image("https://ausmed-images.s3.ap-southeast-2.amazonaws.com/ausmed.com/ausmed-articles/20170316_cover_V2.jpg")
    st.markdown("## Benefits:")
    st.write("- Fast and accurate diagnosis of diseases")
    st.write("- Non-invasive and painless diagnosis using MRI")
    st.write("- Accessible from anywhere, anytime")
    st.markdown("## Why is our app unique?")
    st.write("- BrainBuddy combines multiple ML models into one app")
    st.write("- The app uses CNN on MRI imagery to diagnose diseases")
    st.write("- BrainBuddy uses advanced algorithms to provide fast and accurate diagnosis")
    st.markdown("## Relevance:")
    st.write("- BrainBuddy can diagnose various diseases, such as brain tumor")
    st.write("- The app can be used by doctors, hospitals, and patients")
    st.write("- BrainBuddy can improve the accuracy and speed of disease diagnosis")
    st.markdown("## Uses:")
    st.write("- Hospitals and clinics can use BrainBuddy to diagnose diseases more quickly")
    st.write("- Patients can use BrainBuddy to get a quick and accurate diagnosis without the need for invasive procedures")

    
# Render page layout
page_layout()
