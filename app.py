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
    st.title("🔗 Connect With Me")
    st.write("Find me across the web on these platforms. Click any button to visit my profile.")
    
    # We create a 3-column grid to keep the links organized and visually impressive
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Chess")
        # use_container_width=True makes the buttons expand to fill the column perfectly
        st.link_button("♟️ FIDE Profile (1545)", "http://ratings.fide.com/profile/498777", use_container_width=True)
        st.link_button("♞ Chess.com", "http://chess.com/member/aajukubaa", use_container_width=True)
        st.link_button("♘ Lichess", "http://lichess.org/@/onesandzeros", use_container_width=True)
        
    with col2:
        st.subheader("Coding & Content")
        st.link_button("💻 GitHub", "https://github.com/Aajukubaaa", use_container_width=True)
        st.link_button("▶️ YouTube", "https://www.youtube.com/@Aajukubaa", use_container_width=True)
        
    with col3:
        st.subheader("Other Profiles")
        st.link_button("🎮 Roblox", "http://roblox.com/users/6007529811/profile", use_container_width=True)
        st.link_button("👕 Vinted", "http://vinted.co.uk/member/284456392", use_container_width=True)
        st.link_button("📧 Email Me", "mailto:kabirbhuchar@gmail.com", use_container_width=True)

# --- PAGE 3: ACTIVITIES ---
elif page == "Activities":
    st.title("Extracurricular Activities")
    st.write("This is where we will map out your basketball and chess tournaments.")

# --- PAGE 4: SCHOOL WORK ---
elif page == "School Work":
    st.title("Design Portfolios & Presentations")
    st.write("This is where we will use Python to embed your Google Slides.")
