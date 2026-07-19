import streamlit as st
import random
import os
from database import init_db, log_submission, get_submissions, clear_all_data
from story_generator import generate_story



# Set page configuration
st.set_page_config(
    page_title="Imaginary Love Story Generator",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize database
init_db()

# Custom CSS for rich aesthetics (pink/purple gradient, custom fonts, glassmorphism)
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Playfair+Display:ital,wght@0,600;0,800;1,600&display=swap" rel="stylesheet">
<style>
    /* Full page background gradient */
    .stApp {
        background: linear-gradient(135deg, #fbcfe8 0%, #e9d5ff 50%, #f472b6 100%);
        background-attachment: fixed;
    }
    
    /* Center container adjustments */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
    }
    
    /* Header typography */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #4c0519 !important;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.5);
    }
    
    /* Card design */
    .story-card {
        background: rgba(255, 255, 255, 0.7);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(244, 114, 182, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.5);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .story-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 40px 0 rgba(244, 114, 182, 0.3);
    }
    
    /* Card headers styling */
    .card-header {
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        font-weight: 800;
        color: #881337;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Paragraph text styling */
    .card-body {
        font-family: 'Outfit', sans-serif;
        font-size: 1.1rem;
        line-height: 1.6;
        color: #312e81;
    }
    
    /* Big Titles */
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        color: #9d174d;
        margin-bottom: 5px;
        line-height: 1.2;
    }
    
    .sub-title {
        font-family: 'Outfit', sans-serif;
        font-size: 1.25rem;
        text-align: center;
        color: #701a75;
        margin-bottom: 30px;
        font-weight: 300;
    }
    
    /* Disclaimer text */
    .disclaimer {
        font-family: 'Outfit', sans-serif;
        font-size: 0.85rem;
        color: #9d174d;
        font-style: italic;
        margin-top: -10px;
        margin-bottom: 20px;
        text-align: left;
    }
    
    /* Compatibility Score circle / styling */
    .comp-box {
        background: linear-gradient(135deg, #f472b6 0%, #db2777 100%);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        color: white;
        margin-top: 30px;
        box-shadow: 0 10px 25px rgba(219, 39, 119, 0.4);
    }
    .comp-title {
        font-family: 'Outfit', sans-serif;
        font-size: 1.3rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 600;
        margin-bottom: 5px;
    }
    .comp-score {
        font-family: 'Playfair Display', serif;
        font-size: 4rem;
        font-weight: 800;
        margin: 10px 0;
    }
    .comp-message {
        font-family: 'Outfit', sans-serif;
        font-size: 1.15rem;
        font-style: italic;
    }

    /* Style Streamlit forms and selections */
    div[data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.6) !important;
        border-radius: 20px !important;
        padding: 25px !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        box-shadow: 0 8px 32px 0 rgba(244, 114, 182, 0.15) !important;
        backdrop-filter: blur(8px) !important;
    }
    
    /* Style buttons */
    .stButton>button {
        background: linear-gradient(135deg, #db2777 0%, #be185d 100%) !important;
        color: white !important;
        border-radius: 25px !important;
        border: none !important;
        padding: 0.6rem 2rem !important;
        font-family: 'Outfit', sans-serif !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 15px rgba(219, 39, 119, 0.3) !important;
        transition: all 0.3s ease !important;
        width: 100%;
        margin-top: 10px;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(219, 39, 119, 0.45) !important;
    }
</style>
""", unsafe_allow_html=True)

# Define compatibility messages based on score ranges
def get_compatibility_message(score, user_name, crush_name):
    user = user_name.strip().title()
    crush = crush_name.strip().title()
    if score >= 95:
        return f"❤️ {score}% - Match Made in Heaven! {user} and {crush} are a cosmic alignment of romantic comedy perfection. Time to start planning the wedding!"
    elif score >= 90:
        return f"✨ {score}% - Electric Chemistry! You two fit together like coffee and Sunday mornings. Sparks are flying everywhere!"
    elif score >= 80:
        return f"🍿 {score}% - Popcorn & Chill Vibe! {user} and {crush} are the ultimate dynamic duo. Your inside jokes are top-tier."
    else:
        return f"🧁 {score}% - Sweet and Cheesy! {score}% match. You two are cute enough to cause cavities, with just the right amount of chaos!"

# Initialize session state variables
if "page" not in st.session_state:
    st.session_state.page = "input"
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "crush_name" not in st.session_state:
    st.session_state.crush_name = ""
if "story_stages" not in st.session_state:
    st.session_state.story_stages = {}
if "stage_keys" not in st.session_state:
    st.session_state.stage_keys = ["The Meeting", "The Eye Contact", "The First Conversation", "Falling for Each Other", "Happily Ever After"]
if "current_stage_idx" not in st.session_state:
    st.session_state.current_stage_idx = 0
if "compatibility_score" not in st.session_state:
    st.session_state.compatibility_score = 0

# Page 1: Landing screen and input form
if st.session_state.page == "input":
    st.markdown("<div class='main-title'>💌 Imaginary Love Story Generator</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Craft your own hilarious & heartwarming rom-com adventure!</div>", unsafe_allow_html=True)

    with st.form("love_story_form"):
        st.markdown("### 💖 The Characters")
        col1, col2 = st.columns(2)
        with col1:
            user_name = st.text_input("Your Name", placeholder="e.g. Romeo", max_chars=30)
        with col2:
            crush_name = st.text_input("Your Crush's Name", placeholder="e.g. Juliet", max_chars=30)
            
        st.markdown("<div class='disclaimer'>💌 Your entries help us improve the app and are stored securely.</div>", unsafe_allow_html=True)
        
        st.markdown("### 🗺️ Choose Your Adventure")
        
        meet_place = st.selectbox(
            "1. Where did you first meet? 📍",
            options=["Coffee shop", "College campus", "Through friends", "Online", "Random accident like bumping into them"]
        )
        
        vibe = st.radio(
            "2. What was the vibe when your eyes first met? 👀",
            options=["Slow motion movie moment", "Awkward but cute", "Instant sparks", "Total coincidence"],
            horizontal=True
        )
        
        first_conv = st.selectbox(
            "3. What happened during your first conversation? 💬",
            options=["Talked for hours", "Nervous small talk", "One of you spilled coffee", "Exchanged numbers immediately"]
        )
        
        realization = st.radio(
            "4. How did they realize they liked you? ✨",
            options=["You made them laugh", "A grand gesture", "Slowly over time", "Love at first sight"],
            horizontal=True
        )
        
        first_date = st.selectbox(
            "5. What was your disastrously perfect first date? 🎡",
            options=[
                "Fancy dinner where a dog ate your steak",
                "Amusement park where one of you got stuck on a ride",
                "Stargazing on a roof but it started pouring rain",
                "Karaoke night singing horribly out-of-tune duets"
            ]
        )
        
        challenge = st.selectbox(
            "6. What silly challenge did you two face together? 🧩",
            options=[
                "Assembling Swedish flat-pack furniture",
                "Surviving an escape room under extreme pressure",
                "Cooking a complex recipe that ended in ordering pizza",
                "Meeting the quirky in-laws for the first time"
            ]
        )
        
        submit_btn = st.form_submit_button("Generate Our Story ✨")
        
        if submit_btn:
            if not user_name.strip() or not crush_name.strip():
                st.error("⚠️ Please fill in both your name and your crush's name!")
            elif user_name.strip().lower() == crush_name.strip().lower():
                st.warning("🧐 Self-love is important, but this generator works best with two different names!")
            else:
                # Save data to session state
                st.session_state.user_name = user_name
                st.session_state.crush_name = crush_name
                
                # Generate story
                answers = {
                    "meet_place": meet_place,
                    "vibe": vibe,
                    "first_conv": first_conv,
                    "realization": realization,
                    "first_date": first_date,
                    "challenge": challenge
                }
                st.session_state.story_stages = generate_story(user_name, crush_name, answers)
                
                # Calculate compatibility score
                st.session_state.compatibility_score = random.randint(70, 99)
                st.session_state.current_stage_idx = 0
                st.session_state.page = "reveal"
                
                # Log to SQLite DB
                log_submission(user_name, crush_name, answers, st.session_state.compatibility_score)
                
                # Rerun to switch page
                st.rerun()

    # View Submissions Log Section (Outside the form)
    st.markdown("<br><hr>", unsafe_allow_html=True)
    with st.expander("📊 View Past Stories & Compatibility Logs"):
        df = get_submissions()
        if not df.empty:
            st.dataframe(
                df,
                use_container_width=True,
                column_config={
                    "id": "ID",
                    "user_name": "User Name",
                    "crush_name": "Crush Name",
                    "meet_place": "Meet Place",
                    "vibe": "Vibe",
                    "first_conv": "First Conversation",
                    "realization": "Realization",
                    "first_date": "First Date",
                    "challenge": "Silly Challenge",
                    "compatibility": st.column_config.NumberColumn(
                        "Compatibility %",
                        format="%d%%"
                    ),
                    "timestamp": "Timestamp"
                }
            )
        else:
            st.info("No stories generated yet. Be the first to try it out! 💕")

# Page 2: Story reveal screen
elif st.session_state.page == "reveal":

    user = st.session_state.user_name.strip().title()
    crush = st.session_state.crush_name.strip().title()
    
    st.markdown(f"<div class='main-title'>💖 {user} & {crush}</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Our Imaginary Love Story</div>", unsafe_allow_html=True)
    
    # Stage icon mapping
    icons = {
        "The Meeting": "📍",
        "The Eye Contact": "👀",
        "The First Conversation": "💬",
        "Falling for Each Other": "✨",
        "Happily Ever After": "🎉"
    }
    
    # Display all revealed stages so far
    for i in range(st.session_state.current_stage_idx + 1):
        stage_key = st.session_state.stage_keys[i]
        stage_content = st.session_state.story_stages[stage_key]
        icon = icons.get(stage_key, "❤️")
        
        st.markdown(f"""
        <div class="story-card">
            <div class="card-header">{icon} Stage {i+1}: {stage_key}</div>
            <div class="card-body">{stage_content}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Bottom actions / progress
    max_idx = len(st.session_state.stage_keys) - 1
    
    if st.session_state.current_stage_idx < max_idx:
        # Show "Continue the story →" button
        if st.button("Continue the story →"):
            st.session_state.current_stage_idx += 1
            st.rerun()
    else:
        # Show Compatibility Score
        score = st.session_state.compatibility_score
        message = get_compatibility_message(score, user, crush)
        
        st.markdown(f"""
        <div class="comp-box">
            <div class="comp-title">💘 Compatibility Rating 💘</div>
            <div class="comp-score">{score}%</div>
            <div class="comp-message">{message}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        st.write("")
        
        # Show "Start Over" button
        if st.button("Start Over 🔄"):
            # Reset state
            st.session_state.page = "input"
            st.session_state.user_name = ""
            st.session_state.crush_name = ""
            st.session_state.story_stages = {}
            st.session_state.current_stage_idx = 0
            st.session_state.compatibility_score = 0
            st.rerun()
