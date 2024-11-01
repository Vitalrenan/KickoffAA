import streamlit as st
import pandas as pd
from datetime import datetime
st.set_page_config(layout="wide")         
df =  pd.read_parquet('base_parquet')
nomes_alunos = ['Junior','Aninha','Carlos','Maria']
cursos={
        'gastronomia':['PLANEJAMENTO DE CARDÁPIO', 'ADMINISTRAÇÃO APLICADA À GASTRONOMIA'],
        'engenharia_civil':['FÍSICA GERAL E EXPERIMENTAL - MECÂNICA','QUÍMICA E CIÊNCIA DOS MATERIAIS'],
        'ciencias_contabeis':['ANÁLISE DE CUSTOS', 'MÉTODOS QUANTITATIVOS'],
        'publicidade_propaganda':['SISTEMAS BRASILEIROS DE COMUNICAÇÃO', 'SOCIEDADE BRASILEIRA E CIDADANIA']
    }

st.session_state['data_hora']= datetime.now().strftime("%d/%m/%Y %H:%M")
#render
colA, colB = st.columns(spec=[0.7,0.3])
with colA:
    st.title("Feedback Personalizado")
with colB:
    logo='logo_cogna.png'
    st.image(logo)
  
with st.sidebar:
    st.image(logo)
    user_name = st.selectbox("Nome aluno", (nomes_alunos))
    curso = df[df.nome_aluno==user_name]['curso']
    user_curso = st.selectbox("Curso", (curso))
    if user_curso:
        user_materia = st.selectbox("Materia", cursos[user_curso])
        

st.markdown(
    df[
         (df.nome_aluno==user_name)
        &(df.curso==user_curso)
    ]['feedback'].item()
)
st.divider()
st.dataframe(df)


    
