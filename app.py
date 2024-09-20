import streamlit as st
from pubchempy import get_compounds, Compound
import sys
import pubchempy as pcp

##############
st.sidebar.image("img/gpx4.png",
                 caption="Recursos para Química Orgánica")

#############################Pagina 1############################## 

def Home():
    st.markdown("# A partir del nombre común")
    st.sidebar.markdown("# Nombre Común")

    entrada = st.text_input("Escribe el nombre de una molécula en inglés:", "glucose")
    s= pcp.get_compounds(entrada,'name')
    
    comps_ds = get_compounds(entrada, 'name')
    st.markdown("## Nombre IUPAC")
    st.text(s[0].iupac_name)
    st.markdown("## Representación en SMILES isomérico")
    st.text(comps_ds[0].isomeric_smiles)
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
