import streamlit as st
import google.generativeai as genai

# पन्नों की बुनियादी सेटिंग
st.set_page_config(page_title="Smart AI Prompt", page_icon="🚀", layout="centered")

# अपनी जेमिनी चाबी को यहाँ जोड़ना
GOOGLE_API_KEY = "AQ.Ab8RN6KQnDUujoRUG_cw8B2hG5S9WU9UcIm4sqPNGUdBGSLdFg"
genai.configure(api_key=GOOGLE_API_KEY)

st.title("🚀 Smart AI Prompt Generator")
st.write("अपने 3-4 शब्द लिखें और Midjourney के लिए पूरा प्रॉम्प्ट पाएं!")

# यूज़र के लिए इनपुट बॉक्स
user_ideas = st.text_input("अपने शब्द यहाँ लिखें:", placeholder="जैसे: neon samurai portrait")

if st.button("Generate Professional Prompt"):
    if user_ideas:
        with st.spinner("AI सोच रहा है..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                # एआई को दिया जाने वाला खुफिया निर्देश
                system_instruction = f"तुम एक एक्सपर्ट प्रॉम्प्ट इंजीनियर हो। यूज़र के इस छोटे आइडिया '{user_ideas}' को Midjourney और Stable Diffusion के लिए एक बेहद खूबसूरत और डिटेल्ड प्रॉम्प्ट में बदलो। उसमें 8k क्वालिटी, सिनेमैटिक लाइटिंग, कैमरा एंगल और आर्ट स्टाइल खुद से जोड़ना। जवाब में सिर्फ तैयार प्रॉम्प्ट ही देना, कोई और फालतू बात मत लिखना।"
                
                response = model.generate_content(system_instruction)
                
                st.success("आपका प्रॉम्प्ट तैयार है! 👇")
                st.code(response.text) # इससे यूज़र एक क्लिक में कॉपी कर पाएगा
            except Exception as e:
                st.error("कुछ तकनीकी दिक्कत आ गई है, कृपया दोबारा जांचें।")
    else:
        st.warning("कृपया पहले कुछ शब्द टाइप करें!")
