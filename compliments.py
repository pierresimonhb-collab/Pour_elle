import streamlit as st
import random
import os

# Configuration de la page (titre de l'onglet et émoji)
st.set_page_config(page_title="Pour Toi ❤️", page_icon="❤️", layout="centered")

# --- STYLE CSS CHIRURGICAL ---
# On injecte un peu de CSS pour styliser le gros bouton cœur et centrer le texte
st.markdown("""
    <style>
    /* Centrer tout le contenu */
    .block-container {
        padding-top: 5rem;
        text-align: center;
    }
    h1 {
        color: #ff477e !important;
        font-family: 'Segoe UI', sans-serif;
        font-size: 2rem !important;
        margin-bottom: 2rem !important;
    }
    /* Style du gros bouton cœur */
    div.stButton > button {
        background-color: #ff477e;
        color: white;
        font-size: 3rem;
        padding: 20px 40px;
        border-radius: 50px;
        border: none;
        box-shadow: 0 10px 20px rgba(255, 71, 126, 0.3);
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #ff7096;
        transform: scale(1.05);
        border: none;
    }
    div.stButton > button:active {
        transform: scale(0.95);
    }
    /* Boîte à compliments */
    .compliment-box {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-top: 2rem;
        font-size: 1.3rem;
        color: #4a4a4a;
        line-height: 1.6;
        border-left: 5px solid #ff477e;
    }
    </style>
""", unsafe_allow_html=True)

# --- CHARGEMENT DES POÈMES ---

poemes_et_compliments=["magnifique","drole","forte au rugby","rayonnant","musclée","combattive","classe","talents lectuaires indéniables","bien foutue","souriante","intelligente","impliquée","belle","sublime","hypnotisante"]
# --- INTERFACE ---
st.title("Clique sur le cœur pour chaque fois où tu penses à moi... ✨")

# Bouton interactif
if st.button("❤️"):
    # On choisit un poème ou compliment au hasard
    choix = random.choice(poemes_et_compliments)
    
    # On l'affiche joliment dans notre boîte stylisée en CSS
    st.markdown(f'<div class="compliment-box">{choix.replace("\n", "<br>")}</div>', unsafe_allow_html=True)