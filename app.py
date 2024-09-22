import streamlit as st
from pubchempy import get_compounds, Compound
import sys
import pubchempy as pcp

import streamlit.components.v1 as components
import py3Dmol
from stmol import showmol
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem

##############
st.sidebar.image("img/gpx4.png",
                 caption="Recursos para Química Orgánica")

#############################Pagina 1############################## 

def Home():
    st.header('Input :cat:', divider='rainbow')
    st.sidebar.markdown("""# Nombre clásico:
    Trivial name, non-systematic name for a chemical substance, son otras denominaciones en inglés
    """)

    entrada = st.text_input("Escribe el nombre común en inglés:", "glucose")

    #if key == "Nombre Común":
    #  entrada = st.text_input("Escribe el nombre común en inglés:", "glucose")
    #elif key == "SMILES":
    #  entrada = st.text_input("Escribe el código SMILES:", "CCO")
    #else:
    #  entrada = st.text_input("Escribe el código SMILES:", "IUPAC")
    
    st.markdown("### IUPAC")  
    nombreiupac = pcp.get_compounds(entrada,'name')
    st.text(nombreiupac[0].iupac_name)
    
    st.markdown("### SMILES Isomérico")
    smilesisomerico = get_compounds(entrada, 'name')
    st.text(smilesisomerico[0].isomeric_smiles)

    st.markdown("### Masa molecular (g/mol)")
    masamolecular = get_compounds(entrada, 'name')
    st.text(masamolecular[0].exact_mass)
  
    st.markdown("### Coeficiente de partición")
    coeficientedeparticion = get_compounds(entrada, 'name')
    st.text(coeficientedeparticion[0].xlogp)
  
    st.pyplot()

#############################Pagina 2############################## 

def page2():
    st.header('Input :smiley:', divider='rainbow')
    st.sidebar.markdown("""# Simplified Molecular Input Line Entry System
                           Sistema de introducción molecular lineal simplificada
                           """)
    
    entrada = st.text_input("Escribe el nombre SMILES: ", "C1=CC2=C(C3=C(C=CC=N3)C=C2)N=C1")
    st.markdown("### PubChem ID:")
    st.text(pcp.get_compounds(entrada, 'smiles'))
  
    st.pyplot()

#############################Pagina 3##############################    

def page3():
  st.header('Visualización en 3D 🍫', divider='rainbow')
  st.sidebar.markdown("# Simpl")
  st.sidebar.markdown(Simplified Molecular Input Line Entry )
  #st.link_button("Adaptación de José Manuel Nápoles Duarte", "https://github.com/napoles-uach")

  def showm(smi, style='stick'):
      mol = Chem.MolFromSmiles(smi)
      mol = Chem.AddHs(mol)
      AllChem.EmbedMolecule(mol)
      AllChem.MMFFOptimizeMolecule(mol, maxIters=200)
      mblock = Chem.MolToMolBlock(mol)
  
      view = py3Dmol.view(width=350, height=350)
      view.addModel(mblock, 'mol')
      view.setStyle({style:{}})
      view.zoomTo()
      #view.show()
      #view.render()
      showmol(view)
      #t =view.js()
      #f = open('viz.html', 'w')
      #f.write(t.startjs)
      #f.write(t.endjs)
      #f.close()
  
  compound_smiles=st.text_input('Ingresa tu código SMILES','FCCC(=O)[O-]')
  m = Chem.MolFromSmiles(compound_smiles)
  
  Draw.MolToFile(m,'mol.png')
  
  
  
  #HtmlFile = open("viz.html", 'r', encoding='utf-8')
  #source_code = HtmlFile.read() 
  c1,c2=st.columns(2)
  with c1:
    st.write('Molecule 2D :smiley:')
    st.image('mol.png')
  with c2:
    st.write('Molecule 3D :frog:')
    showm(compound_smiles)

################################################################### 
##########################Configuracion############################    
###################################################################    

page_names_to_funcs = {
  "Nombre común": Home,
  "SMILES": page2,
  "Vista 3D": page3,
}

selected_page = st.sidebar.selectbox("Tipo de entrada", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
