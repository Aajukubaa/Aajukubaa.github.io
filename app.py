import streamlit as st

# 1. PAGE CONFIGURATION
# This must be the very first Streamlit command. It makes your site wide and sets the tab title.
st.set_page_config(page_title="Kabir Bhuchar | Portfolio", layout="wide")

# 2. SIDEBAR NAVIGATION
# We create a radio button menu in a sidebar. 
# Whatever the user clicks gets stored in the 'page' variable.
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "My Links", "Activities", "School Work"])

# --- PAGE 1: THE LANDING HOMEPAGE ---
if page == "Home":
    st.title("Welcome to My World")
    st.subheader("I am Kabir Bhuchar. Student, Athlete, and Developer.")
    
    # st.columns splits your screen into sections, making it look very professional and technical.
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.write("I am a student from India, currently living in London. I balance my time between competitive sports, strategic board games, and writing Python code.")
        st.write("Use the sidebar on the left to explore my projects, tournament results, and school work.")
    
    with right_column:
        # st.metric creates a cool, dashboard-style stat block. Perfect for a technical look!
        st.metric(label="FIDE Chess Rating", value="1545", delta="Active Player")
        st.metric(label="Basketball Position", value="Center (6'0\")")
        st.metric(label="Violin", value="Suzuki Book 3")

# --- PAGE 2: MY LINKS ---
elif page == "My Links":
    st.title("Connect With Me")
    st.write("This is where you will add your Python code to display your Github, YouTube, and Chess profiles!")

# --- PAGE 3: ACTIVITIES ---
elif page == "Activities":
    st.title("Extracurricular Activities")
    st.write("This is where we will map out your basketball and chess tournaments.")

# --- PAGE 4: SCHOOL WORK ---
elif page == "School Work":
    st.title("Design Portfolios & Presentations")
    st.write("This is where we will use Python to embed your Google Slides.")
