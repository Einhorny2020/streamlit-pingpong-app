import streamlit as st

st.set_page_config(page_title="Jeu Ping Pong IA", layout="centered")

st.title("Jeu de Ping-Pong (Streamlit Cloud + GitHub CI/CD)")

st.markdown("""
<style>
iframe {
    border: none;
    width: 100%;
    height: 400px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
#### 🎮 Instructions :
- Utilisez les flèches gauche/droite de votre clavier pour déplacer la raquette.
- Le but est de garder la balle en jeu le plus longtemps possible !
""")
st.components.v1.html("""
<iframe src="https://games.construct.net/2834/latest"></iframe>
""", height=450)