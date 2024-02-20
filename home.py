import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Setor Público Português",
        page_icon="🏛️",
    )

if __name__ == "__main__":
    run()

#sidebar
    
with open('styles.css') as f:
    st.sidebar.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.sidebar.markdown(""" 
                    ### info
                    Esta aplicação é baseada na informação pública do sistema de informação da organização do estado. A base de dados pode ser encontrada em [sioe.dgaep.gov.pt](https://www.sioe.dgaep.gov.pt/)""", unsafe_allow_html=True)    

# Body
st.markdown ("""
             # Setor Público Português 🏛️ 
             ___ """)

st.markdown(
    """
    Nesta aplicação é possível visualizar a informação relativa ao universo organizacional do setor público português. O objetivo é disponibilizar informação de forma acessível e intuitiva, permitindo a exploração de dados de forma interativa. Na interação com a aplicação pretende-se que o utilizador fique a conhecer a estrutura organizacional do setor público.

    ___ """
)


# Define a pergunta e a resposta
pergunta = "Quantos organismos tem o setor público no universo das contas nacionais?"
resposta = "8500"

# Mostra a pergunta numa "carta"
st.subheader(pergunta)  # Ou st.write(pergunta) para um texto normal

# Cria um botão que, quando clicado, mostrará a resposta
if st.button('Ver resposta'):
    # Mostra a resposta abaixo do botão
    st.subheader(resposta)  # Ou st.write(resposta) para um texto normal



