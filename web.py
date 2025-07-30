import streamlit as st
from PIL import Image

# Page configuration - customize the tab name here
st.set_page_config(
    page_title="MCOMM PROJECT",  # Replace with your desired tab name
    page_icon="🌟",  # You can change this emoji or use a custom icon
    layout="wide"
)
st.markdown("""
<style>
/* 🌌 General background + font */
body, .stApp {
    background-color: #0a0a23;
    color: #7142D4;
    font-family: 'Comic Neue', cursive;
    
}

/* 🎯 Title, headers, subheaders */
h1, h2, h3 {
    color: #7142D4;
    font-family: 'Brushstroke';
    font-weight: 800;
}

/* 🔗 Link-style buttons */
div.stButton > link_button {
    background-color: transparent;
    color: #1f6feb;
    text-decoration: underline;
    font-weight: bold;
    font-size: 16px;
    border: none;
    padding: 0.4em 0.8em;
    transition: all 0.2s ease-in-out;
    border-radius: 5px;
}

div.stButton > button:hover {
    color: #4ea3ff;
    background-color: rgba(31, 111, 235, 0.1);
    cursor: pointer;
}

/* 🎛 Sidebar styles */
section[data-testid="stSidebar"] {
    background-color: #11111f ;
    color: #e0e0e0;
    font-family: 'papyrus';
}

/* Sidebar content styling (updated selector) */
section[data-testid="stSidebar"] > div {
    color: #1f6feb;
    font-weight: bold;
    font-size: 20px;
    font-family: 'papyrus';
}

/* Additional sidebar element selectors for broader compatibility */
section[data-testid="stSidebar"] .css-ng1t4o,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #1f6feb !important;
    font-weight: bold;
}
@media only screen and (max-width: 600px) {
    /* Scale down titles */
    h1 {
        font-size: 1.8rem !important;
    }
    h2 {
        font-size: 1.4rem !important;
    }
    h3, h4 {
        font-size: 1.1rem !important;
    }
    
    /* Reduce padding/margin around main containers */
    .css-18e3th9, /* main block container */
    .css-1d391kg, /* section containers */
    .css-1lcbmhc, /* columns */
    .css-1v3fvcr { /* text containers */
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }

    /* Make sidebar full width on mobile */
    section[data-testid="stSidebar"] {
        position: relative !important;
        width: 100% !important;
        height: auto !important;
        padding: 0.5rem !important;
        z-index: 1000;
    }
    
    /* Adjust button font size */
    div.stButton > button {
        font-size: 1rem !important;
        padding: 0.5rem 1rem !important;
    }
    
    /* Images scale to full width */
    img {
        max-width: 100% !important;
        height: auto !important;
    }
</style>
""", unsafe_allow_html=True)

# Main title - replace with your title
st.title("MCOMM project site")

# Subtitle (optional)


st.header("INTRODUCTION")
st.subheader("In recent years, social media has become deeply embedded in modern life. While these platforms provide entertainment and a sense of connection, they also raise serious concerns about mental well-being, identity, and self-worth. Our project examines these issues by analysing data from a Kaggle dataset and visualizing key patterns in behaviour and psychology. We focus on the effects of prolonged social media use, particularly regarding distraction, self-esteem, and the need for validation. The following figures explore the complex relationship between digital habits and mental health indicators—including attention disorders, emotional reliance on online engagement, and comparison-driven dissatisfaction..\n\n\n\n\n\n")
# Create columns for layout
st.header("BODY AND DISCUSSION")
st.subheader("To explore the psychological impact of social media, we focused on two central areas: self-esteem and distraction. Using visual data from the Kaggle dataset, we analysed patterns in user behaviour, emotional responses, and mental health indicators. The figures below are grouped into two sections—each addressing a core question at the heart of our research.")
col1, col2, col3, = st.columns([3, 1,3])

# with col3:
#     st.subheader("made by:")
#     st.subheader('Abdul Naser Maamon Rabie')
#     st.subheader('Zaid Aburuman')
#     st.subheader('najeeb')
#     st.subheader('eisa')




with col1:
    st.header("This section examines how prolonged social media use influences self-esteem, emotional reliance, and the pursuit of validation. The visualizations explore trends in how users engage with content, seek approval, and compare themselves to others.")
    st.header("Question: the effect of social media on a person's self-esteem, is there a correlation?")
    st.subheader("")
    st.image("self-esteem distribution.jpg", caption="Fig 1:Self-Esteem Decline with Screen Time.", width=600)
    st.image("validation_from_social_media.jpg", caption="Fig 2:Emotional Reliance on Social Media Validation.", width=600)
    st.image("meaniingless_media.jpg", caption="Fig 3: Frequency of ‘Doom Scrolling’.", width=600)
    st.image("comparing_urself_using_social_media.jpg", caption="Fig 4: Frequency of Social Comparisons to Successful Individuals in Social Media.", width=600)
    st.image("distribution_of_mental_health.jpg", caption="Fig 5: Mental Health Scores Among Social Media Users.", width=600)
    
    st.header("**THE ANALYITCAL FAX:**")
    st.subheader("* through the graphs above, the more people use social media, the more desperate they become for attention, as shown in figure 2.")
    st.subheader("* We also noticed a direct correlation between figures 2 and 3, which is proved by figure 1, which itself shows the self-esteem of the same group of people. ")
    st.subheader("* Comparing both figure 2 and figure 4 together show a rather interesting scenario, a majority of social media users end up comparing themselves to online successes, but some cope by seeking online validation from the source of their insecurity, the wired.")
    st.subheader("* Figure 5 shows that the entire dataset is scewed due to the participants in the collection having potential pre-existing mental disorders that could contribute to higher or lower scrores in question.")
    st.header("the consensus:")
    st.subheader("* we believe that the data is pointing at a common GEN Z phenomenon known as \'doom scrolling\', a case where an individual aimlessly and mindlessly flips through content of a given social media platform, usually short-form videos. The data shows that it is tied with with low self-esteem. In our opinion, doom scrolling is both a result of and a contributor to low self-esteem.")
    st.subheader("* The skeweness of figure 5 is a sign that all the participants could have been effected by the social media content they consume, meaning that there is some sort of inherent bias in the data. ")
    st.subheader("* Our data supports to following studies:")
    st.link_button("national library of medicine" ,"https://pmc.ncbi.nlm.nih.gov/articles/PMC10129173/?utm_source=chatgpt.com")
    st.link_button("world journal of advanced research and reviews","https://wjarr.com/sites/default/files/WJARR-2024-3027.pdf?utm_source=chatgpt.com")

with col3:
    st.header("This section focuses on attention span, digital restlessness, and the potential relationship between social media and disorders like ADHD. The figures explore how easily users are distracted and how dependent they may be on constant online engagement.")
    st.header("Question: Distractions and the role social media has in it")
    st.subheader("")
    st.image("difficulty_in_concentration.jpg", caption="Fig 6: Difficulty in Concentrating.", width=600)
    st.image("distraction_by_social_media.jpg", caption="Fig 7: Frequency of Being Distracted From Work By Social Media.", width=600)
    st.image("distribution_ADHD.jpg", caption="Fig 8: Severity of Self-Reported ADHD Symptoms Among Social Media Users.", width=600)
    st.image("easeily_distracted.jpg", caption="Fig 9: Distraction Levels Among Social Media Users.", width=600)
    st.image("restless_without_media.jpg", caption="Fig 10: Prevalence of Restlessness During Social Media Abstinence.", width=600)
    
    st.header("**THE ANALYITCAL FAX:**")
    st.subheader("* figures 6 and 7 have a direct correlation with eachother, considering that someone who cannot concentrate is someone who is easily distracted.")
    st.subheader("* figures 8 and 10, have a direct correlation with eachother, where people prone to ADHD are prone to being restless and more likely to be distracted by social media.")
    st.subheader("* figures 9 and 6 have a similar correlation to figures 6 and 7.")
    st.subheader("* We also noticed a direct correlation between figures 2 and 3, which is proved by figure 1, which itself shows the self-esteem of the same group of people. ")
    st.header("the consensus:")
    st.subheader("* similar to the other figures, the data shows that there is some form of bias from figures such as the ADHD distribution showing that the participants could have had trouble with social media to begin with.")
    st.subheader("* We also believe that technological advancements aid in the ease of distraction, particularly, in the decible levels of phones, when different sources of notifications grab the user's attention due to genuinely being a surprise.")
    st.subheader("* Our data supports to following studies:")
    st.link_button("youtube video discussing our topics","https://youtu.be/FZvee3-PEzo?si=lqVfvh3pzq448frZ")
    st.link_button("baptist health article", "https://www.baptisthealth.com/blog/family-health/how-social-media-affects-attention-span")
    

# Section with labels and content


# # Labels with content

# st.write("Content for label 1 goes here")

# st.write("**YOUR_LABEL_2:**")
# st.write("Content for label 2 goes here")

# st.write("**YOUR_LABEL_3:**")
# st.write("Content for label 3 goes here")

# # Buttons section
# st.header("Interactive Elements")

# # Create columns for buttons
# button_col1, button_col2, button_col3 = st.columns(3)

# with button_col1:
#     if st.button("YOUR_BUTTON_1_LABEL"):
#         st.success("Button 1 clicked! Add your functionality here.")

# with button_col2:
#     if st.button("YOUR_BUTTON_2_LABEL"):
#         st.info("Button 2 clicked! Add your functionality here.")

# with button_col3:
#     if st.button("YOUR_BUTTON_3_LABEL"):
#         st.warning("Button 3 clicked! Add your functionality here.")

# # Additional interactive elements
# st.header("More Interactive Elements")

# # Text input with custom label
# user_input = st.text_input("YOUR_INPUT_LABEL_HERE", placeholder="Enter your text here")

# # Selectbox with custom label
# option = st.selectbox("YOUR_SELECTBOX_LABEL_HERE", ["Option 1", "Option 2", "Option 3"])

# # Slider with custom label
# slider_value = st.slider("YOUR_SLIDER_LABEL_HERE", 0, 100, 50)

# # Display user selections
# if user_input:
#     st.write(f"You entered: {user_input}")

# st.write(f"You selected: {option}")
# st.write(f"Slider value: {slider_value}")

# Sidebar with additional content
st.sidebar.header("media and sociey project website:")
st.sidebar.write("**Abdul Naser Maamon Rabie, 202211579**")
st.sidebar.write("**Zaid Aburuman**, 202108408")
st.sidebar.write("**Najeeb Abdulrahman Abdi**, 202307172 ")
st.sidebar.write("**eisa Al-Malki, 202102387**")



# # Sidebar image placeholder
# # st.sidebar.image("path_to_sidebar_image.jpg", caption="Sidebar image caption")
# st.sidebar.write("🖼️ **SIDEBAR IMAGE PLACEHOLDER**")

# # Sidebar button
# if st.sidebar.button("YOUR_SIDEBAR_BUTTON_LABEL"):
#     st.sidebar.success("Sidebar button clicked!")

# Footer
st.markdown("---")
st.header("Beyond the Data: A Human Perspective:")
st.subheader("While our analysis focuses on measurable trends in mental health and social media use, the broader cultural shifts driven by technology deserve equal attention. Modern platforms are carefully designed to capture and monetize attention, often leading to compulsive use, unhealthy comparisons, and declining self-worth. People curate idealized versions of their lives online, creating distorted perceptions of reality that can leave others feeling inadequate. Algorithms, optimized for engagement rather than well-being, reinforce echo chambers and push sensational content, shaping how users think, feel, and interact. As virtual interactions increase, genuine human connection and spontaneous social moments diminish. What emerges is a cycle where distraction, disconnection, and emotional fatigue become normalized. This highlights the need for conscious, mindful engagement with digital platforms—and a re-centering of human values in an increasingly algorithm-driven world.")
st.header("CONCLUSION")
st.subheader("Our analysis reveals a clear pattern: excessive social media use is linked to lower self-esteem, increased distraction, and a growing reliance on external validation. Behaviors like 'doom scrolling' reflect a cycle where users seek comfort from the very platforms that contribute to their distress. "
    "While some bias may exist—such as pre-existing mental health conditions in participants—the overall trends suggest that platform design plays a significant role in shaping emotional and cognitive well-being. "
    "Ultimately, the findings highlight the need for greater awareness around how digital habits affect mental health. As Gen Z continues to navigate an online world optimized for engagement, fostering healthier, more intentional use of social media is essential."
)
st.link_button("the original dataset from kaggle","https://www.kaggle.com/datasets/souvikahmed071/social-media-and-mental-health?.com")
# Instructions for customization (remove this section when deploying)
# st.markdown("---")
# st.markdown("### 📝 Customization Instructions:")
# st.markdown("""
# **Replace the following placeholders:**
# - `YOUR_TAB_NAME_HERE` - Name that appears in the browser tab
# - `YOUR_MAIN_TITLE_HERE` - Main page title
# - `YOUR_SECTION_HEADER_HERE` - Section headers
# - `YOUR_LABEL_1`, `YOUR_LABEL_2`, etc. - Custom labels for your content
# - `YOUR_BUTTON_1_LABEL`, `YOUR_BUTTON_2_LABEL`, etc. - Button text
# - `YOUR_INPUT_LABEL_HERE` - Label for text input
# - `YOUR_SELECTBOX_LABEL_HERE` - Label for dropdown menu
# - `YOUR_SLIDER_LABEL_HERE` - Label for slider
# - `YOUR_SIDEBAR_TITLE_HERE` - Sidebar title
# - `YOUR_FOOTER_TEXT_HERE` - Footer text

# **For images:**
# - Uncomment the `st.image()` lines and replace with your image paths
# - Supported formats: PNG, JPG, JPEG, GIF, SVG

# **To run this app:**
# ```bash
# pip install streamlit pillow
# streamlit run your_app_name.py
# ```
# """)
