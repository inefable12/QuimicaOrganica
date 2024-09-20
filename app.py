import streamlit as st
from pubchempy import get_compounds, Compound
import sys
import pubchempy as pcp

##############
st.sidebar.image("img/gpx4.png",
                 caption="Recursos para Química Orgánica")

#############################Pagina 1############################## 

def Home():
    st.markdown("# Input:")
    st.sidebar.markdown("# Nombre Común")

    st.radio(
        "Escoge 👉",
        key="visibility",
        options=["Nombre Común", "SMILES", "IUPAC"],
    )

    if key == "Nombre Común":
      entrada = st.text_input("Escribe el nombre común en inglés:", "glucose")
    elif:
      entrada = st.text_input("Escribe el código SMILES:", "CCO")
    else:
      entrada = st.text_input("Escribe el código SMILES:", "IUPAC")
    
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
    st.markdown("A partir del Código SMILES")
    st.sidebar.markdown("SMILES")
    
    st.info('Generalidades')
    st.write('''El.''')

#############################Pagina 3##############################    

def page3():
  st.header('Más información', divider='rainbow')
   
  st.link_button("Github", "https://github.com/inefable12/")

################################################################### 
##########################Configuracion############################    
###################################################################    

page_names_to_funcs = {
  "Nombre común": Home,
  "IUPAC": page2,
  "Otros recursos": page3,
}

selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
