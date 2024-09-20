import streamlit as st
from pubchempy import get_compounds, Compound
import sys
import pubchempy as pcp

st.title("Recursos para Química Orgánica")
st.text("Autor: Jesus Alvarado")

#moleculaA = "https://raw.githubusercontent.com/inefable12/QuimicaOrganica/refs/heads/main/moleculas/A_gluc.pdb"
entrada = st.text_input("A_gluc.pdb o B_gluc.pdb: ", "moleculaA")
s= pcp.get_compounds('glucose','name')

print(s[0].iupac_name)
st.pyplot()
