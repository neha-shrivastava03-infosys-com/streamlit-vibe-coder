import streamlit as st
from agents.code_agent import generate_code
from agents.refinement_agent import refine_code

# Page config
st.set_page_config(
    page_title="Vibe Coder",
    page_icon="🎨",
    layout="wide"
)

# Custom CSS for colorful UI
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #667eea, #764ba2);
}

.main {
    background: linear-gradient(135deg, #fdfbfb, #ebedee);
    padding: 2rem;
    border-radius: 20px;
}

/* Title styling */
.title {
    font-size: 3rem;
    font-weight: bold;
    background: linear-gradient(90deg, #ff4b2b, #ff416c);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Button styling */
.stButton button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 12px;
    padding: 0.6rem 1.5rem;
    font-size: 18px;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #ff512f, #dd2476);
}

/* Text area styling */
.stTextArea textarea {
    border-radius: 15px;
    border: 2px solid #667eea;
    padding: 10px;
    font-size: 16px;
}

/* Code block styling */
.stCodeBlock {
    border-radius: 15px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background: linear-gradient(135deg, #89f7fe, #66a6ff);
    color: black;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">🎨 Vibe Coding Pair Programmer</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="card">Describe your UI and let AI generate beautiful Streamlit apps instantly ✨</div>',
    unsafe_allow_html=True
)

# Layout columns
col1, col2 = st.columns([2, 1])

with col1:

    description = st.text_area(
        "Describe your UI",
        placeholder="Example: Create a colorful login page with gradient buttons and glassmorphism effect",
        height=150
    )

    generate_btn = st.button("🚀 Generate UI Code")

with col2:

    st.markdown("""
    ### 💡 Ideas
    
    Try prompts like:
    
    • Netflix dashboard  
    • Modern login page  
    • Analytics dashboard  
    • Glassmorphism UI  
    • Spotify homepage  
    """)

# Tabs for output
tab1, tab2 = st.tabs(["🧠 Generated Code", "👁 Preview Instructions"])

if generate_btn and description:

    with st.spinner("🧠 AI is generating your UI..."):

        code = generate_code(description)
        refined_code = refine_code(code)

        with tab1:
            st.success("✨ UI generated successfully!")
            st.code(refined_code, language="python")

        with open("generated_ui.py", "w", encoding="utf-8") as f:
            f.write(refined_code)

        with tab2:
            st.info("Run this in terminal to preview your generated UI:")
            st.code("streamlit run generated_ui.py")

# Footer
st.markdown("---")
st.markdown(
    "<center>Built with ❤️ using Streamlit + OpenAI</center>",
    unsafe_allow_html=True
)