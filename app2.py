import streamlit as st
from transformers import pipeline

# ---------------- Load Model ----------------
@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="vedabtpatil07/Mental-Health-Analysis"
    )

classifier = load_model()

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="🧠 Mental Health Text Classifier",
    page_icon="🧠",
    layout="centered",
)
# ---------------- Custom CSS ----------------
st.markdown("""
    <style>
    /* 🌈 Background gradient */
    .stApp {
        background: linear-gradient(135deg, #EEF2FF 0%, #E0EAFC 100%);
        font-family: 'Segoe UI', sans-serif;
        color: #1A1A1A;
    }

    /* 🧠 Headings */
    h1, h2, h3, h4 {
        text-align: center;
        color: #2C3E50;
        font-weight: 700;
    }

    /* ✨ Card-style container */
    .main {
        background-color: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
    }

    /* 💬 Text area styling */
    textarea {
        border-radius: 12px !important;
        border: 1px solid #D1D9E6 !important;
        font-size: 1.05em;
        padding: 0.8em !important;
        background-color: #FAFBFF !important;
        color: #2C3E50 !important;
    }

    /* 🚀 Buttons */
    div.stButton > button {
        background: linear-gradient(90deg, #5A60F2, #7B61FF);
        color: white;
        border-radius: 10px;
        padding: 0.6em 1.4em;
        border: none;
        font-weight: 600;
        box-shadow: 0 3px 6px rgba(90, 96, 242, 0.3);
        transition: all 0.25s ease;
    }

    div.stButton > button:hover {
        background: linear-gradient(90deg, #4A50E0, #6B50F5);
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(90, 96, 242, 0.4);
    }

    /* ✅ Success message */
    .stAlert {
        border-radius: 12px;
        padding: 1.2em;
        background-color: #E8F9F1 !important;
        border: 1px solid #B3E6D4 !important;
        color: #006644 !important;
    }

    /* ⚠ Warning styling */
    .stAlert[data-baseweb="notification"] {
        border-radius: 10px;
        background-color: #FFF5E5 !important;
        border: 1px solid #FFD580 !important;
        color: #663C00 !important;
    }

    /* 📊 Progress bar color */
    .stProgress > div > div {
        background-color: #5A60F2;
        border-radius: 10px;
    }

    /* 🧭 Input labels */
    label {
        font-weight: 600 !important;
        color: #2C3E50 !important;
    }
    </style>
""", unsafe_allow_html=True)
# ---------------- Landing Page ----------------
if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    st.title("🧠 Mental Health Text Classifier")
    st.markdown(
        """
        ### AI-powered Mental Health Text Analyzer  
        ---
        ⚠ *Disclaimer: This tool is for **research/educational purposes only.*  
        It is *not a substitute for professional medical advice, diagnosis, or treatment.*
        """
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("Analyze emotional and mental health cues from your text using AI 🧩.")
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("🚀 Get Started", on_click=lambda: st.session_state.update(started=True))
    st.stop()

# ---------------- Input Section ----------------
st.header("💬 Enter Your Text")
st.write("Provide a paragraph, message, or post you'd like to analyze.")
user_input = st.text_area("🧾 Paste text here:", height=150)

# ---------------- Analysis Section ----------------
if st.button("🔎 Analyze"):
    if user_input.strip():
        with st.spinner("🧠 Analyzing emotional tone..."):
            results = classifier(user_input, top_k=None)

        # Sort by probability
        results = sorted(results, key=lambda x: x['score'], reverse=True)

        # ---------------- Show Primary Result ----------------
        top_result = results[0]
        primary_label = top_result['label']
        primary_score = top_result['score'] * 100

        st.markdown("---")
        st.success(f"### ✅ Primary Result: *{primary_label}* detected (Confidence: {primary_score:.2f}%)")

        # ---------------- Explanation Section ----------------
        st.subheader("🧩 Explanation of Findings")
        explanation = {
            "depression": "The text might contain signs of hopelessness, sadness, or self-deprecating language often associated with depressive thoughts.",
            "anxiety": "The text may include language reflecting excessive worry, fear, or tension commonly seen in anxious expressions.",
            "suicidal ideation": "The AI may have detected phrases indicating self-harm, hopelessness, or thoughts about ending one’s life.",
            "neutral": "The text seems emotionally balanced with no significant distress signals detected.",
            "positive": "The content reflects optimism, calmness, or healthy emotional expression."
        }
        exp_text = explanation.get(primary_label.lower(), "The model detected emotional cues that align with this category.")
        st.info(exp_text)

        # ---------------- Confidence Distribution ----------------
        st.markdown("### 📊 Confidence Distribution:")
        for res in results:
            label = res['label']
            score = res['score'] * 100

            # Color coding
            if label.lower() in ["depression", "anxiety", "suicidal ideation"]:
                emoji = "🔴"
            elif label.lower() in ["positive", "neutral"]:
                emoji = "🟢"
            else:
                emoji = "🟡"

            st.write(f"{emoji} {label}** ({score:.2f}%)")
            st.progress(int(score))
            st.write("")

        # ---------------- Feedback Section ----------------
        st.markdown("---")
        st.subheader("💬 Feedback")
        st.write("Did the AI get it right? Help us improve the model by sharing your feedback 👇")

        col1, col2 = st.columns(2)
        with col1:
            feedback_choice = st.radio("Model's prediction was:", ["✅ Correct", "❌ Incorrect"])
        with col2:
            user_label = st.text_input("If incorrect, what should it be? (Optional)")

        user_comments = st.text_area("Any additional comments or notes:", height=80)

        if st.button("📨 Submit Feedback"):
            st.success("🙏 Thank you! Your feedback will help improve the model’s accuracy.")
            # (Optional) You can log or save this feedback using Google Sheets / Firebase / Supabase here
            # Example: save_feedback(user_input, primary_label, feedback_choice, user_label, user_comments)

    else:
        st.warning("⚠ Please enter some text before analyzing.")