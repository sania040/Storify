import io
from story_generator import generate_story
import streamlit as st

st.title(" Storify")
st.subheader("Give me ingredients I will give you tea... ")

# User Inputs
genre = st.selectbox("Select a Genre", ["Fantasy", "Sci-Fi", "Mystery", "Romance", "Adventure"])
character = st.text_input("Main Character's Names")
setting = st.text_input("Story Setting (e.g., ancient forest, futuristic city)")
tone = st.selectbox("Tone", ["Funny", "Serious", "Dark", "Inspiring"])
length = st.selectbox("Story Length", ["Short", "Medium", "Long"])

# Submit Button
if st.button("Generate Story"):
    with st.spinner("Writing your story... "):
        story = generate_story(genre, character, setting, tone, length)
    
    # Display the story
    st.markdown("### Your AI-Generated Story:")
    st.write(story)

    # Create a download button for the story as a text file
    if story:  # Ensure there's a story before trying to download
        story_file = io.StringIO(story)  # Convert string to a file-like object
        st.download_button(
            label="Download Story as .txt",
            data=story_file.getvalue(),
            file_name="ai_generated_story.txt",
            mime="text/plain"
        )
