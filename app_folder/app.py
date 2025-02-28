# Hi, I'm Ivy. This is my LeadSmart app designed for Streamlit this semester. Enjoy!
import streamlit as st
import random
import base64

# I configure the page with a title, icon, and wide layout.
st.set_page_config(
    page_title="LeadSmart Educational Games",
    page_icon="🎮",
    layout="wide"
)

# Injected custom CSS to style the sidebar, center text, buttons, and the expander.
st.markdown(
    """
    <style>
    /* I style the sidebar */
    [data-testid="stSidebar"] > div:first-child {
        background-color: #FBC02D !important;
        color: #000000 !important;
    }

    /* I define a utility class to center text */
    .center-text {
        text-align: center;
    }

    /* I style buttons globally: light green background with bold, black text and a border */
    .stButton > button {
        background-color: #C5E1A5 !important;
        color: #000000 !important;
        border: 2px solid #333 !important;
        border-radius: 0 !important; 
        padding: 0.5em 1em !important;
        font-weight: bold !important;
        font-family: 'sans-serif', Arial !important;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #A5D6A7 !important;
        border-color: #555 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# I create helper functions for setting the background, centering text, updating progress, and navigation.
def set_background(image_path: str):
    #I set the app background image using a base64 encoded image.
    bg_image_base64 = get_base64_image(image_path)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bg_image_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def get_base64_image(image_path: str) -> str:
    # I open the image file and convert its content to a base64 string.
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def center_text(text: str, tag: str = "h2"):
    #I center text by embedding it in an HTML tag with a center class.
    st.markdown(f"<{tag} class='center-text'>{text}</{tag}>", unsafe_allow_html=True)

def update_progress():
    #I update and display the user's progress based on their current score.
    progress = (st.session_state.user_score / 5) * 100 if st.session_state.user_score > 0 else 0
    st.progress(int(progress))
    st.markdown(
        f"<div class='center-text'><strong>Games Explored: {round(progress, 1)}%</strong></div>",
        unsafe_allow_html=True
    )

def create_navigation_buttons():
    col_left, col_right = st.columns([3, 1])  # I adjust column widths for positioning.

    # In the left column, I place the Finish button and set its action.
    with col_left:
        st.markdown("<div id='finish_button_container' style='margin-top: 80px;'>", unsafe_allow_html=True)
        if st.button("Finish", key="finish_button_python"):
            st.session_state.current_page = "final"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # In the right column, I place the Back button and define its action.
    with col_right:
        st.markdown("<div id='back_button_container' style='text-align: right; margin-top: 80px;'>", unsafe_allow_html=True)
        if st.button("Back", key="back_button_python"):
            st.session_state.current_page = "objectives"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

def choose_random_objective() -> str:
    # Randomly selects one of the key business skills.
    options = [
        "Design Thinking",
        "Decision-Making",
        "Resource Management",
        "Avoiding Conflict",
        "Communication"
    ]
    return random.choice(options)

def mark_objective_completed(objective: str):
    # Marks an objective as completed and update the score if it hasn't been completed before.
    if objective not in st.session_state.completed_objectives:
        st.session_state.user_score += 1
        st.session_state.completed_objectives.append(objective)

# Initializes session state variables if they don't already exist.
if 'current_page' not in st.session_state:
    st.session_state.current_page = "welcome"
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.completed_objectives = []

# I define functions to create the header, footer, and sidebar.
def create_header():
    # Creates a header with a title and subtitle.
    st.markdown("""
    <div style='text-align:center; padding: 20px; color: white; 
                background-color: rgba(0,0,0,0.3); margin-bottom: 20px;'>
        <h2 style='margin-bottom: 0;'>LeadSmart: The Skillful Leadership Edition</h2>
        <p style='margin-top: 5px;'>Enhance your business skills through fun educational games!</p>
    </div>
    """, unsafe_allow_html=True)

def create_footer():
    # I add a footer with a horizontal rule for separation.
    st.markdown("""
    <hr style='border-top: 2px solid #FFB74D;'/>
    <div style='text-align:center; font-size: 14px; color: #555; margin-top: 10px;'></div>
    """, unsafe_allow_html=True)

def create_sidebar():
    # Builds the sidebar to display progress and quick tips.
    with st.sidebar:
        st.markdown("## Progress")
        update_progress()
        st.markdown("---")
        st.markdown("**Quick Tips:**")
        st.markdown("- Select a skill from the main page.")
        st.markdown("- Expand the 'How to Play' to see instructions.")
        st.markdown("- Use the Finish button to see your final score.")

# Creates functions to build each page of the app.
def create_welcome_screen():
    # I build the welcome screen with header, sidebar, background image, and a button.
    create_header()
    create_sidebar()
    set_background("app_folder/image/welcome_page_bg.png")
    st.markdown(
        """
        <div style="background-color: #FFD600; color: #8B0000; text-align: center; padding: 10px;">
            <h3 style="margin: 0;">Welcome to the Digital Handbook for Educational Games!</h3>
            <h4 style="margin-top: 5px;">Are you ready to play and learn?</h4>
        </div>
        """,
        unsafe_allow_html=True
    )
    # Adds extra space before the "Let's Play!" button.
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    if st.button("Let's Play!", key="play"):
        st.session_state.current_page = "instructions"
        st.rerun()
    create_footer()

def create_instructions_page():
    # I made the instructions page to guide the user on how to use the app.
    create_header()
    create_sidebar()
    set_background("app_folder/image/clean_bg.png")
    st.markdown(
        """
        <div style="background-color: #FFD600; color: #8B0000; text-align: center; padding: 5px;">
            <h3 style="margin: 0; font-size: 1.8em;">How to Use Your Educational Digital Handbook:</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    # I add margin to push the instructions a bit down.
    st.markdown("<div style='margin-top: 30px;'>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>Choose a key business skill you want to master or let the computer choose for you.</li>
        <li>For each skill, open the "How to Play" expander to view instructions.</li>
        <li>Follow the instructions to play the game with your group.</li>
        <li>Track your progress in the sidebar →</li>
        <li><strong>Most Important:</strong> HAVE FUN! 🌟</li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    if st.button("START", key="start_objectives"):
        st.session_state.current_page = "objectives"
        st.rerun()
    create_footer()

def create_objectives_page():
    # Builds the objectives page where the user selects the business skill they want to master.
    create_header()
    create_sidebar()
    set_background("app_folder/image/clean_bg.png")
    st.markdown(
        """
        <div style="background-color: #FFD600; color: #8B0000; text-align: center; padding: 5px; margin-top: 50px;">
            <h3 style="margin: 0;">Choose a Key Business Skill You Want to Master:</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)

    # I wrap the objective buttons in a container.
    st.markdown("<div id='objectives_container'>", unsafe_allow_html=True)
    # First row: I create three columns for the initial skill choices.
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Design Thinking", key="design_thinking"):
            st.session_state.current_page = "design_thinking"
            st.rerun()
    with col2:
        if st.button("Resource Management", key="resource_management"):
            st.session_state.current_page = "resource_management"
            st.rerun()
    with col3:
        if st.button("Avoiding Conflict", key="avoiding_conflict"):
            st.session_state.current_page = "avoiding_conflict"
            st.rerun()

    # Second row: I create two more buttons and a RANDOM option.
    col4, col5, col6 = st.columns(3)
    with col4:
        if st.button("Decision-Making", key="decision_making"):
            st.session_state.current_page = "decision_making"
            st.rerun()
    with col5:
        if st.button("Communication", key="communication"):
            st.session_state.current_page = "communication"
            st.rerun()
    with col6:
        if st.button("RANDOM", key="random_choice"):
            st.session_state.current_page = choose_random_objective()
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    create_navigation_buttons()
    create_footer()

def create_design_thinking_page():
    # Creates the Design Thinking page with details about the game.
    create_header()
    create_sidebar()
    set_background("app_folder/image/objective_specific_bg.png")
    # Displays the objective title and game name with centered text.
    center_text(
        "<span style='background-color: #FFD600; color: #8B0000; padding: 3px; font-size: 1.5em;'>Design Thinking</span>",
        "h4")
    center_text(
        "<span style='background-color: #FFD600; color: #8B0000; padding: 2px; font-size: 1.2em;'>Game: Marshmallow Challenge</span>",
        "h5")

    st.markdown("""
    <ul style='text-align:left; list-style:none; margin-top:10px;'>
      <li><strong>Time:</strong> 45 minutes</li>
      <li><strong>Participants:</strong> 4-6</li>
      <li><strong>Setting:</strong> Indoors or workspace</li>
      <li><strong>Outcome:</strong> Creativity and problem-solving</li>
    </ul>
    """, unsafe_allow_html=True)

    with st.expander("How to Play"):
        st.markdown("""
        1. Provide each group with 20 spaghetti sticks, 1 yard of tape, 1 yard of string, and 1 marshmallow.<br>
        2. Build the tallest freestanding structure that can hold the marshmallow on top.<br>
        3. You have 18 minutes for planning and construction.<br>
        4. Measure the height of each structure to determine the winner.<br>
        5. Discuss iteration and prototyping in the design process.
        """, unsafe_allow_html=True)
    mark_objective_completed("Design Thinking")
    create_navigation_buttons()
    create_footer()

def create_decision_making_page():
    # Creates the Decision-Making page.
    create_header()
    create_sidebar()
    set_background("app_folder/image/objective_specific_bg.png")
    center_text("<span style='background-color: #FFD600; color: #8B0000; padding: 3px; font-size: 1.5em;'>Decision-Making</span>", "h4")
    center_text("<span style='background-color: #FFD600; color: #8B0000; padding: 2px; font-size: 1.2em;'>Game: The Balloon Debate</span>", "h5")
    st.markdown("""
    <ul style='text-align:left; list-style:none; margin-top:10px;'>
      <li><strong>Time:</strong> 30-45 minutes</li>
      <li><strong>Participants:</strong> 4-6</li>
      <li><strong>Setting:</strong> Classroom or meeting room</li>
      <li><strong>Outcome:</strong> Decision-making under pressure</li>
    </ul>
    """, unsafe_allow_html=True)
    with st.expander("How to Play"):
        st.markdown("""
        1. Each participant represents a famous person or character in a balloon.<br>
        2. The balloon is losing altitude, and one person must be thrown out to save the others.<br>
        3. Participants take turns making arguments for why they should stay.<br>
        4. After everyone speaks, a vote is taken and one person is removed.<br>
        5. Continue until one person remains, who is declared the winner.
        """, unsafe_allow_html=True)
    mark_objective_completed("Decision-Making")
    create_navigation_buttons()
    create_footer()

def create_resource_management_page():
    # Creates the Resource Management page.
    create_header()
    create_sidebar()
    set_background("app_folder/image/objective_specific_bg.png")
    center_text("<span style='background-color: #FFD600; color: #8B0000; padding: 3px; font-size: 1.5em;'>Resource Management</span>", "h4")
    center_text("<span style='background-color: #FFD600; color: #8B0000; padding: 2px; font-size: 1.2em;'>Game: Supply Chain Puzzle</span>", "h5")
    st.markdown("""
    <ul style='text-align:left; list-style:none; margin-top:10px;'>
      <li><strong>Time:</strong> 25-35 minutes</li>
      <li><strong>Participants:</strong> 4-6 per team</li>
      <li><strong>Setting:</strong> Indoors, classroom or office setup</li>
      <li><strong>Outcome:</strong> Plan and manage resources effectively</li>
    </ul>
    """, unsafe_allow_html=True)
    with st.expander("How to Play"):
        st.markdown("""
        1. Each team is given resources (colored paper, scissors, glue, markers).<br>
        2. Create a supply chain on a poster, showing how a product moves from raw materials to the customer.<br>
        3. Manage resources carefully with limited paper for each stage.<br>
        4. You have 20 minutes to complete your poster.<br>
        5. Each team then presents their poster and explains their resource decisions.
        """, unsafe_allow_html=True)
    mark_objective_completed("Resource Management")
    create_navigation_buttons()
    create_footer()

def create_avoiding_conflict_page():
    # Creates the Avoiding Conflict page.
    create_header()
    create_sidebar()
    set_background("app_folder/image/objective_specific_bg.png")
    center_text("<span style='background-color: #FFD600; color: #8B0000; padding: 3px; font-size: 1.5em;'>Avoiding Conflict</span>", "h4")
    center_text("<span style='background-color: #FFD600; color: #8B0000; padding: 2px; font-size: 1.2em;'>Game: Win as Much as You Can</span>", "h5")
    st.markdown("""
    <ul style='text-align:left; list-style:none; margin-top:10px;'>
      <li><strong>Time:</strong> 30-40 minutes</li>
      <li><strong>Participants:</strong> 8-12</li>
      <li><strong>Setting:</strong> Classroom or meeting room</li>
      <li><strong>Outcome:</strong> Collaboration, trust-building</li>
    </ul>
    """, unsafe_allow_html=True)
    with st.expander("How to Play"):
        st.markdown("""
        1. Divide participants into teams and give each group vote cards (X or Y).<br>
        2. Teams vote either X or Y in several rounds.<br>
        3. If all teams vote Y, everyone earns points; if any team votes X, that team earns more points while others lose.<br>
        4. Announce points after each round and allow group discussion.<br>
        5. Discuss competition versus collaboration and trust.
        """, unsafe_allow_html=True)
    mark_objective_completed("Avoiding Conflict")
    create_navigation_buttons()
    create_footer()

def create_communication_page():
    # Creates the Communication page.
    create_header()
    create_sidebar()
    set_background("app_folder/image/objective_specific_bg.png")
    center_text("<span style='background-color: #FFD600; color: #8B0000; padding: 3px; font-size: 1.5em;'>Communication</span>", "h4")
    center_text("<span style='background-color: #FFD600; color: #8B0000; padding: 2px; font-size: 1.2em;'>Game: Telephone Pictionary (Telestrations)</span>", "h5")
    st.markdown("""
    <ul style='text-align:left; list-style:none; margin-top:10px;'>
      <li><strong>Time:</strong> 20-30 minutes</li>
      <li><strong>Participants:</strong> 6-8</li>
      <li><strong>Setting:</strong> Indoor, sitting at a table</li>
      <li><strong>Outcome:</strong> Enhances communication and interpretation</li>
    </ul>
    """, unsafe_allow_html=True)
    with st.expander("How to Play"):
        st.markdown("""
        1. Each participant starts with a drawing pad and writes a sentence at the top.<br>
        2. Pass the pad to the next person to draw an illustration based on that sentence.<br>
        3. The next person writes a sentence interpreting the drawing.<br>
        4. Alternate between drawing and writing until the pad returns to the original person.<br>
        5. Share the final sentence and original to compare how the message evolved.
        """, unsafe_allow_html=True)
    mark_objective_completed("Communication")
    create_navigation_buttons()
    create_footer()

def navigate_to_skill(skill: str) -> str:
    # I map each full skill name to its corresponding page identifier.
    skill_mapping = {
        "Design Thinking": "design_thinking",
        "Decision-Making": "decision_making",
        "Resource Management": "resource_management",
        "Avoiding Conflict": "avoiding_conflict",
        "Communication": "communication"
    }
    return skill_mapping.get(skill, "objectives")

def create_random_result_page(selected_skill: str):
    # Displays the randomly selected skill and offer a button to learn more.
    create_header()
    create_sidebar()
    set_background("app_folder/image/clean_bg.png")
    center_text(f"The computer has selected: <strong>{selected_skill}</strong>! 🎲", "h2")
    # A "Learn More" button that routes to the corresponding skill page.
    if st.button("Learn More", key="learn_more_random"):
        st.session_state.current_page = navigate_to_skill(selected_skill)
        st.rerun()
    create_footer()

def create_final_page():
    # Creates the final page with a congratulatory message and display the final progress.
    create_header()
    create_sidebar()
    set_background("app_folder/image/finish_bg.png")
    center_text("🌟 Congratulations! 🌟", "h2")
    center_text("You're now better equipped to LeadSmart with confidence and creativity! 🚀", "h4")
    st.markdown(
        "<div style='text-align:center; margin-top:10px; font-size:16px;'>"
        "Keep going and apply these skills in your daily life! YOU'RE A STAR!"
        "</div>",
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    final_progress = (st.session_state.user_score / 5) * 100
    cols = st.columns(3)
    with cols[1]:
        st.markdown(
            f"<h2 style='font-size:2.5em; color:#BA68C8; text-align:center; margin-top:100px;'>Final Result: {int(final_progress)}%</h2>",
            unsafe_allow_html=True
        )
    if st.button("Back to Objectives"):
        st.session_state.current_page = "objectives"
        st.rerun()
    create_footer()

# I define the page routing: each page identifier maps to its creation function.
page_routes = {
    "welcome": create_welcome_screen,
    "instructions": create_instructions_page,
    "objectives": create_objectives_page,
    "design_thinking": create_design_thinking_page,
    "decision_making": create_decision_making_page,
    "resource_management": create_resource_management_page,
    "avoiding_conflict": create_avoiding_conflict_page,
    "communication": create_communication_page,
    "final": create_final_page
}

current_page = st.session_state.current_page

# Routes to the appropriate page based on the current session state.
if current_page in page_routes:
    page_routes[current_page]()
elif current_page in [
    "Design Thinking", "Decision-Making",
    "Resource Management", "Avoiding Conflict", "Communication"
]:
    create_random_result_page(current_page)
else:
    st.error("Page not found!")
