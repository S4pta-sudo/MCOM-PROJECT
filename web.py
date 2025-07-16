import streamlit as st
from PIL import Image

# Page configuration - customize the tab name here
st.set_page_config(
    page_title="MCOMM PROJECT",  # Replace with your desired tab name
    page_icon="🌟",  # You can change this emoji or use a custom icon
    layout="wide"
)

# Main title - replace with your title
st.title("MCOMM project site")

# Subtitle (optional)


st.header("INTRODUCTION")
st.subheader("in recent years, social media has become an integral part of daily life, especially for members of modern society. While platforms offer entertainment and connectivity, they also raise serious concerns about mental well-being, identity, and self-worth. Through our analysis of kaggle data and corresponding visualizations, we explored the psychological effects of prolonged social media usage, with a particular focus on patterns of distraction, self-esteem, and the search for validation. The following figures uncover nuanced relationships between social behaviors and mental health indicators—ranging from attention disorders to emotional reliance on digital engagement.\n\n\n\n")
# Create columns for layout
st.header("BODY AND DISCUSSION")
col1, col2, col3, = st.columns([1, 1,1])

# with col3:
#     st.subheader("made by:")
#     st.subheader('Abdul Naser Maamon Rabie')
#     st.subheader('Zaid Aburuman')
#     st.subheader('najeeb')
#     st.subheader('eisa')




with col1:
    
    st.header("Question: the affect of social media on a person's self-esteem, is there a correlation?")
    st.subheader("")
    st.image(r"C:\Users\naser\OneDrive\Desktop\UNI\MEDIA AND SOCIETY SUMMER\project\images\self-esteem distribution.jpg", caption="Fig 1:the longer people use social media, the lower their self-esteem becomes.", width=400)
    st.image(r"C:\Users\naser\OneDrive\Desktop\UNI\MEDIA AND SOCIETY SUMMER\project\images\validation_from_social_media.jpg", caption="Fig 2:1 would be posting to make people laugh, seeking validation, while 5 would be making fun of murder for clout.", width=400)
    st.image(r"C:\Users\naser\OneDrive\Desktop\UNI\MEDIA AND SOCIETY SUMMER\project\images\meaniingless_media.jpg", caption="Fig 3:tendency for people to scroll aimlessly.", width=400)
    st.image(r"C:\Users\naser\OneDrive\Desktop\UNI\MEDIA AND SOCIETY SUMMER\project\images\comparing_urself_using_social_media.jpg", caption="Fig 4: tendency for people to compare their current state to that of the successes they see on social media.", width=400)
    st.image(r"C:\Users\naser\OneDrive\Desktop\UNI\MEDIA AND SOCIETY SUMMER\project\images\distribution_of_mental_health.jpg", caption="Fig 5: distribution of all participants and how much they suffer from mental illness, prioir to the dataset being made.", width=400)
    
    st.header("**THE ANALYITCAL FAX:**")
    st.subheader("* through the graphs above, the more people use social media, the more desperate they become for attention, as shown in figure 2.")
    st.subheader("* We also noticed a direct correlation between figures 2 and 3, which is proved by figure 1, which itself shows the self-esteem of the same group of people. ")
    st.subheader("* Comparing both figure 2 and figure 4 together show a rather interesting scenario, a majority of social media users end up comparing themselves to online successes, but some cope by seeking online validation from the source of their insecurity, the wired.")
    st.subheader("* Figure 5 shows that the entire dataset is scewed due to the participants in the collection having potential pre-existing mental disorders that could contribute to higher or lower scrores in question.")
    st.header("the consensus:")
    st.subheader("* we believe that the data is pointing at a common GEN Z phenomonon know as \'doom scrolling\', a case where an individual aimlessly and mindlessly flips through content of a given social media platform, usually short-form videos. The data shows that it is tied with with low self-esteem. In our opinion, doom scrolling is both a result of and a contributor to low self-esteem.")
    st.subheader("* The sceweness of figure 5 is a sign that all the participants could have been effected by the social media content they consume, meaning that there is some sort of inherent bias in the data. ")
    st.subheader("* Our data supports to following studies:")
    st.link_button("national library of medicine" ,"https://pmc.ncbi.nlm.nih.gov/articles/PMC10129173/?utm_source=chatgpt.com")
    st.link_button("world journal of advanced research and reviews","https://wjarr.com/sites/default/files/WJARR-2024-3027.pdf?utm_source=chatgpt.com")

with col3:
    st.header("Question: Distractions and the role social media has in it")
    st.subheader("")
    st.image(r"C:\Users\naser\OneDrive\Desktop\UNI\MEDIA AND SOCIETY SUMMER\project\images\difficulty_in_concentration.jpg", caption="Fig 6: The participants started out with carying attention spans.", width=400)
    st.image(r"C:\Users\naser\OneDrive\Desktop\UNI\MEDIA AND SOCIETY SUMMER\project\images\distraction_by_social_media.jpg", caption="Fig 7: The lack of concentration on work leads to suseptability to social media distractions.", width=400)
    st.image(r"C:\Users\naser\OneDrive\Desktop\UNI\MEDIA AND SOCIETY SUMMER\project\images\distribution_ADHD.jpg", caption="Fig 8: The distribution in ADHD, type unspecified, in the participants, similar to figure 1.", width=400)
    st.image(r"C:\Users\naser\OneDrive\Desktop\UNI\MEDIA AND SOCIETY SUMMER\project\images\easeily_distracted.jpg", caption="Fig 9: direct correlation with figure 6, though with questionable readings.", width=400)
    st.image(r"C:\Users\naser\OneDrive\Desktop\UNI\MEDIA AND SOCIETY SUMMER\project\images\restless_without_media.jpg", caption="Fig 10: restlessness of a person without social media.", width=400)
    
    st.header("**THE ANALYITCAL FAX:**")
    st.subheader("* figures 6 and 7 have a direct correlation with eachother, considering that someone who cannot concentrate is someone who is easily distracted.")
    st.subheader("* figures 8 and 10, have a direct correlation with eachother, where people prone to ADHD are prone to being restless and more likely to be distracted by social media.")
    st.subheader("* figures 9 and 6 have a simialr correlation to figures 6 and 7.")
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

# # Sidebar with additional content
# st.sidebar.header("media and sociey project website:")
# st.sidebar.write("**Abdul Naser Maamon Rabie, 202211579**")
# st.sidebar.write("**Zaid Aburuman**, 202108408")
# st.sidebar.write("**Najeeb**")
# st.sidebar.write("**eisa**")



# # Sidebar image placeholder
# # st.sidebar.image("path_to_sidebar_image.jpg", caption="Sidebar image caption")
# st.sidebar.write("🖼️ **SIDEBAR IMAGE PLACEHOLDER**")

# # Sidebar button
# if st.sidebar.button("YOUR_SIDEBAR_BUTTON_LABEL"):
#     st.sidebar.success("Sidebar button clicked!")

# Footer
st.markdown("---")
st.header("CONCLUSION")
st.subheader("From the data and figures analyzed, a clear pattern emerges: excessive social media use is closely tied to increased distraction, lowered self-esteem, and a cycle of seeking validation from the very sources that provoke insecurity. Several figures show overlapping trends, reinforcing correlations between restlessness, ADHD tendencies, and emotional instability. However, potential dataset skew—highlighted in Figure 5—reminds us that many participants may have entered the study with existing psychological conditions, which could amplify the observed effects. Still, this doesn’t undermine the larger implication: Gen Z's relationship with social media is both psychologically complex and deeply affected by platform design. The rise of doom scrolling, in particular, appears not only as a byproduct of digital fatigue but also as a contributing factor to it—creating a loop of disengagement, comparison, and cognitive overload. Ultimately, these findings underscore the urgent need for awareness, digital literacy, and healthier interaction with social technology.")
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