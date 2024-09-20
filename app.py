import streamlit as st
from pubchempy import get_compounds, Compound
import sys
import pubchempy as pcp

st.title("Recursos para Química Orgánica")
st.text("Autor: Jesus Alvarado")

st.title("Nombre común a IUPAC")
st.text("")

#moleculaA = "https://raw.githubusercontent.com/inefable12/QuimicaOrganica/refs/heads/main/moleculas/A_gluc.pdb"
entrada = st.text_input("Escribe el nombre de una molécula en inglés:", "glucose")
s= pcp.get_compounds(entrada,'name')

comps_ds = get_compounds(entrada, 'name')
st.text("Nombre IUPAC")
st.text(s[0].iupac_name)
st.text("Representación en SMILES isomérico")
st.text(comps_ds[0].isomeric_smiles)
st.pyplot()
