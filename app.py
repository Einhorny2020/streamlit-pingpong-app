import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="🏓 Jeu Ping-Pong IA", layout="centered")
st.title("🏓 Jeu de Ping-Pong – Version Intégrée")

st.markdown("### 🕹️ Utilisez les flèches ← → pour contrôler la raquette.")
st.markdown("**Objectif** : Garder la balle en jeu le plus longtemps possible.")

with open("game.html", "r") as f:
    game_html = f.read()

components.html(game_html, height=450, scrolling=False)