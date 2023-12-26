import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd 

st.title("Génère ton plan de cours !")

niveau = st.selectbox(
    'Quel niveau ?',
    ('CP', 'CE1', 'CE2', 'CM1', 'CM2'))

duree = st.selectbox(
    'Quelle durée ?',
    ('1H', '2H', '1J', '2J', '5J'))

theme = st.selectbox(
    'Quel thème ?',
    ('Les dinosaures', 'Les pharaons', 'La grèce antique'))

matière = st.selectbox(
    'Quelle matière ?',
    ('Maths - Additions/soustraction', 'Français - Compréhension de texte', 'Culture générale'))

res = st.button("Générer", key=None, help=None,args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)

st.text(np.add(2,3))