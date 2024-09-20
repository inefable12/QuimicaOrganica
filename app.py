import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import MolFromSmiles
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import MolsToGridImage
from rdkit.Chem.Draw import IPythonConsole
from pubchempy import get_compounds, Compound
import sys
import pubchempy as pcp
import ipywidgets as widgets
from faerun_notebook import SmilesDrawer
#from google.colab import output
#output.enable_custom_widget_manager()
import py3Dmol
import matplotlib.pyplot as plt

st.title("Recursos para Química Orgánica")
st.text("Autor: Jesus Alvarado")

moleculaA = "https://raw.githubusercontent.com/inefable12/QuimicaOrganica/refs/heads/main/moleculas/A_gluc.pdb"
entrada = st.text_input("A_gluc.pdb o B_gluc.pdb: ", "moleculaA")

view = py3Dmol.view(width=600, height=200, viewergrid=(1,3), linked=True)
view.addModel(open(entrada, 'r').read(),'pdb')
view.setStyle({'line':{'colorscheme':'spectrum','scale':2.0}}, viewer=(0,0))
view.setStyle({'stick':{'colorscheme':'cyanCarbon'}}, viewer=(0,1))
view.setStyle({'sphere':{'colorscheme':'silver','scale':0.7}}, viewer=(0,2))
view.setBackgroundColor('darkgreen',viewer=(0,0))
view.setBackgroundColor('purple',viewer=(0,1))
view.setBackgroundColor('black',viewer=(0,2))
view.zoomTo()
view.render()
view.show()

st.markdown("Resultado :gift:")
st.pyplot()
