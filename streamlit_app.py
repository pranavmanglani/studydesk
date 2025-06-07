import streamlit as st
import webbrowser

# ---------------------------
# Streamlit Page Config
# ---------------------------
st.set_page_config(page_title="Utility Desk", layout="centered")

st.title("📚 Utility Desk")

# ---------------------------
# Search Bar
# ---------------------------
st.subheader("🔍 Search Notes or Videos")
query = st.text_input("Enter your topic:")

if st.button("Search YouTube"):
    if query:
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    else:
        st.warning("Please enter a topic to search.")

# ---------------------------
# Quick Links
# ---------------------------
st.subheader("📂 Quick Access")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📘 Classroom"):
        webbrowser.open("https://classroom.google.com")

with col2:
    if st.button("💬 WhatsApp"):
        webbrowser.open("https://web.whatsapp.com")

with col3:
    if st.button("🎵 Spotify"):
        webbrowser.open("https://open.spotify.com")

# ---------------------------
# Calculator
# ---------------------------
st.subheader("🧮 Calculator")

calc_exp = st.text_input("Enter expression (e.g., 12 + 4 * 3):")

if st.button("Calculate"):
    try:
        result = eval(calc_exp)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error("Invalid Expression")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
