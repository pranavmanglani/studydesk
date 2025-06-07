import streamlit as st
import fitz  # PyMuPDF for PDF
import base64

st.set_page_config(page_title="📚 Utility Desk", layout="wide")

st.title("📚 Utility Desk Dashboard")

# ------------------------
# Dashboard Tabs
# ------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔍 Search", "🧮 Calculator", "📓 Notes Viewer", "💬 WhatsApp", "🎵 Spotify"])

# ------------------------
# Tab 1: Search Tool
# ------------------------
with tab1:
    st.header("🔍 Search Notes or Videos")
    query = st.text_input("Enter your topic:")
    if st.button("Search on YouTube"):
        if query:
            url = f"https://www.youtube.com/results?search_query={query}"
            st.markdown(f"[Click here to view results ▶]({url})", unsafe_allow_html=True)
        else:
            st.warning("Please enter a search query.")

# ------------------------
# Tab 2: Calculator
# ------------------------
with tab2:
    st.header("🧮 Simple Calculator")
    expression = st.text_input("Enter expression (e.g., 3 + 4 * 2):")

    if st.button("Calculate"):
        try:
            result = eval(expression)
            st.success(f"Result: {result}")
        except:
            st.error("Invalid Expression")

# ------------------------
# Tab 3: Notes Viewer
# ------------------------
with tab3:
    st.header("📓 Notes Viewer")

    uploaded_file = st.file_uploader("Upload a note (PDF or .md)", type=["pdf", "md"])

    if uploaded_file:
        if uploaded_file.name.endswith(".md"):
            content = uploaded_file.read().decode("utf-8")
            st.markdown(content)
        elif uploaded_file.name.endswith(".pdf"):
            doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            for page in doc:
                st.image(page.get_pixmap().tobytes(), use_column_width=True)

# ------------------------
# Tab 4: WhatsApp
# ------------------------
with tab4:
    st.header("💬 WhatsApp Web")

    st.warning("WhatsApp cannot be embedded due to security restrictions.")
    st.markdown("[👉 Click here to open WhatsApp Web](https://web.whatsapp.com)", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg", width=100)

# ------------------------
# Tab 5: Spotify
# ------------------------
with tab5:
    st.header("🎵 Spotify Player")

    st.markdown("Enjoy your music while working:")
    spotify_iframe = """
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DXcBWIGoYBM5M?utm_source=generator" 
    width="100%" height="400" frameBorder="0" allowfullscreen="" 
    allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    """
    st.markdown(spotify_iframe, unsafe_allow_html=True)

st.markdown("---")
st.caption("Made with ❤️ using Streamlit – Your all-in-one study dashboard")
