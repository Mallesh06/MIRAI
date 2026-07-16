import streamlit as st
import requests
import random
from urllib.parse import quote

# -------------------------------
# Page Title
# -------------------------------
st.set_page_config(page_title="AI Image Studio", page_icon="🎨")

st.title("🎨 AI Image Studio")
st.sidebar.title("⚙️ Settings")

# -------------------------------
# Sidebar
# -------------------------------
art_style = st.sidebar.selectbox(
    "Choose Art Style",
    ["Sketch", "Portrait", "Oil Paint", "Ghibli Art", "Animation"]
)

width = st.sidebar.slider(
    "Width",
    min_value=256,
    max_value=1200,
    value=512
)

height = st.sidebar.slider(
    "Height",
    min_value=256,
    max_value=1200,
    value=512
)

# Task 3
magic_enhance = st.sidebar.checkbox("✨ Enable Magic Enhance")

# -------------------------------
# Surprise Prompts
# -------------------------------
surprise_prompts = [
    "An astronaut riding a horse on Mars",
    "A cyberpunk street food vendor in Tokyo",
    "A dragon reading books in a magical library",
    "A futuristic underwater city with glowing whales",
    "A robot painting a sunset in the Himalayas"
]

# -------------------------------
# User Prompt
# -------------------------------
user_prompt = st.chat_input("Describe your image...")

# Task 4
surprise = st.button("🎲 Surprise Me!")

# -------------------------------
# Decide Prompt
# -------------------------------
prompt = None

if surprise:
    prompt = random.choice(surprise_prompts)
    st.success(f"Prompt: {prompt}")

elif user_prompt:
    prompt = user_prompt

# -------------------------------
# Generate Image
# -------------------------------
if prompt:

    with st.spinner("Generating image..."):

        full_prompt = f"{prompt} with {art_style} style"

        # Task 3
        if magic_enhance:
            full_prompt += ", masterpiece, 8k resolution, highly detailed, trending on artstation, unreal engine 5 render"

        encoded_prompt = quote(full_prompt)

        # Task 1
        url = (
            f"https://image.pollinations.ai/prompt/{encoded_prompt}"
            f"?width={width}&height={height}"
        )

        response = requests.get(url)

        if response.status_code == 200:

            st.image(
                response.content,
                caption="Generated Image",
                use_container_width=True
            )

            # Task 2
            st.download_button(
                label="📥 Download Image",
                data=response.content,
                file_name=f"{art_style.lower().replace(' ','_')}_image.png",
                mime="image/png"
            )

        else:
            st.error("Failed to generate image.")