import streamlit as st
import webbrowser

st.set_page_config(page_title="Utility Desk", layout="wide")

# ----------------------------
# SIDEBAR - Calculator
# ----------------------------
st.sidebar.title("🧮 Calculator")

calc_input = st.sidebar.text_input("Enter expression (e.g., 2+2):")

if st.sidebar.button("Calculate"):
    try:
        result = eval(calc_input)
        st.sidebar.success(f"Result: {result}")
    except:
        st.sidebar.error("Invalid Expression")

st.sidebar.markdown("---")
st.sidebar.caption("Simple Python Eval Calculator")

# ----------------------------
# MAIN APP LAYOUT
# ----------------------------

col1, col2, col3 = st.columns([2, 3, 3])

# LEFT COLUMN - YouTube Search
with col1:
    st.subheader("🔍 Search YouTube")
    search_query = st.text_input("Search topic (notes, videos, etc.)")

    if st.button("Search"):
        if search_query:
            search_url = f"https://www.youtube.com/results?search_query={search_query}"
            st.markdown(f"[Click to view results ▶]({search_url})", unsafe_allow_html=True)
        else:
            st.warning("Enter a topic to search.")

# MIDDLE COLUMN - WhatsApp
with col2:
    st.subheader("💬 WhatsApp Web")

    # WhatsApp cannot be embedded due to CSP — we give a link with explanation
    st.warning("WhatsApp Web does not support embedding due to security restrictions.")
    st.markdown("[Open WhatsApp Web in new tab](https://web.whatsapp.com)", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg", width=100)

# RIGHT COLUMN - Spotify Player
with col3:
    st.subheader("🎵 Spotify Player")

    # You can embed a Spotify playlist/player if it's public
    spotify_embed = """
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DXcBWIGoYBM5M?utm_source=generator" 
    width="100%" height="380" frameBorder="0" allowfullscreen="" 
    allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    """
    st.markdown(spotify_embed, unsafe_allow_html=True)

st.markdown("---")
st.caption("📚 Utility Desk App – Built with Streamlit")
