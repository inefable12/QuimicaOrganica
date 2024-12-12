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
                 caption="Jesus Alvarado-Huayhuaz")

#############################Pagina 1############################## 

def Home():
    st.header('De nombre común a 2D :cat:', divider='rainbow')
    st.sidebar.markdown("# Nombre clásico:")
    st.sidebar.markdown("Trivial name, non-systematic name for a chemical substance, son otras denominaciones en inglés")

    entrada = st.text_input("Escribe el nombre común en inglés:", "glucose")
    
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

    st.markdown("### PubChem ID")
    id_pubchem = pcp.get_compounds(entrada, 'name')
    st.text(id_pubchem)

    st.markdown("### Representación simplificada")
    m0 = Chem.MolFromSmiles(smilesisomerico[0].isomeric_smiles)    
    Draw.MolToFile(m0,'mol0.png')
    #st.pyplot()
    st.write('Molecule 2D :smiley:')
    st.image('mol0.png')

#############################Pagina 2############################## 

def page2():
    st.header('De SMILES a 2D :smiley:', divider='rainbow')
    st.sidebar.markdown("# Simplified Molecular Input Line Entry System")
    st.sidebar.markdown("Sistema de introducción molecular lineal simplificada")
    
    entrada = st.text_input("Escribe el nombre SMILES: ", "C1=CC2=C(C3=C(C=CC=N3)C=C2)N=C1")
    st.markdown("### PubChem ID:")
    identificador = pcp.get_compounds(entrada, 'smiles')
    st.text(identificador)

    st.markdown("### Nombre IUPAC")  
    nombreiupac = pcp.get_compounds(entrada,'smiles')
    st.text(nombreiupac[0].iupac_name)

    st.markdown("### Representación simplificada")
    m1 = Chem.MolFromSmiles(entrada)    
    Draw.MolToFile(m1,'mol1.png')
    st.write('Molecule 2D :smiley:')
    st.image('mol1.png')
  
#############################Pagina 3##############################    

def page3():
  st.header('De SMILES a visualización 3D 🍫', divider='rainbow')
  st.sidebar.markdown("# 1D 🖙 3D")
  st.sidebar.markdown("Generación de estructura tridimensional a partir del código SMILES")
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
      showmol(view)
  
  compound_smiles=st.text_input('Ingresa tu código SMILES','FCCC(=O)[O-]')
  m = Chem.MolFromSmiles(compound_smiles)
  
  Draw.MolToFile(m,'mol.png')

  c1,c2=st.columns(2)
  with c1:
    st.write('Molecule 2D :smiley:')
    st.image('mol.png')
    #botón de descarga 
    with open('mol.png', 'rb') as f:
        st.download_button('Descargar 2D (en formato PNG)', f, file_name='mol.png', mime='image/png')
  with c2:
    st.write('Molecule 3D :frog:')
    showm(compound_smiles)
    mol_3d = Chem.MolFromSmiles(compound_smiles)
    mol_3d = Chem.AddHs(mol_3d)
    AllChem.EmbedMolecule(mol_3d)
    AllChem.MMFFOptimizeMolecule(mol_3d, maxIters=200)
    mol_block = Chem.MolToMolBlock(mol_3d)
    with open('mol3d.mol', 'w') as f:
        f.write(mol_block)
    #botón de descarga 
    with open('mol3d.mol', 'rb') as f:
      st.download_button('Descargar 3D (en formato MOL)', f, file_name='mol3d.mol', mime='chemical/x-mdl-molfile')

################################################################### 
##########################Configuracion############################    
###################################################################    

page_names_to_funcs = {
  "Nombre común a 2D": Home,
  "SMILES a 2D": page2,
  "Vista 3D": page3,
}

selected_page = st.sidebar.selectbox("Tipo de operación", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
