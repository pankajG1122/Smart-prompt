import streamlit as st
from google import genai

# 1. पेज की सेटिंग और फ़ुटर/मेनू को छिपाना
st.set_page_config(page_title="Smart AI Prompt Generator", page_icon="🚀")

hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# 2. Gemini API क्लाइंट को कनेक्ट करना
try:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    st.error("कृपया Streamlit डैशबोर्ड के Secrets में GEMINI_API_KEY सेट करें।")

# 3. ऐप का इंटरफ़ेस (UI)
st.title("🚀 Smart AI Prompt Generator")
st.write("अपने 3-4 शब्द लिखें और Midjourney के लिए पूरा प्रॉम्प्ट पाएं!")

user_input = st.text_input("अपने शब्द यहाँ लिखें:", placeholder="जैसे: neon samurai portrait")

if st.button("Generate Professional Prompt"):
    if user_input:
        with st.spinner("AI आपके लिए प्रॉम्प्ट तैयार कर रहा है..."):
            try:
                # AI को प्रॉम्प्ट इंजीनियरिंग के लिए निर्देश देना
                system_instruction = (
                    "You are an expert Midjourney prompt engineer. Take the user's short input "
                    "and expand it into a highly detailed, cinematic, and professional Midjourney prompt. "
                    "Include details like lighting, camera lens, style, resolution, and aspect ratios (e.g., --ar 16:9 --v 6.0). "
                    "Output ONLY the final prompt inside a code block, nothing else."
                )
                
                # Gemini Model से रिस्पॉन्स मांगना
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=f"User keywords: {user_input}\nSystem Instruction: {system_instruction}"
                )
                
                # स्क्रीन पर रिजल्ट दिखाना जिसे यूजर आसानी से कॉपी कर सके
                st.success("आपका Midjourney प्रॉम्प्ट तैयार है!")
                st.code(response.text, language="text")
                
            except Exception as e:
                st.error(f"प्रॉम्प्ट जनरेट करने में समस्या आई: {e}")
    else:
        st.warning("कृपया पहले इनपुट बॉक्स में कुछ शब्द लिखें!")

