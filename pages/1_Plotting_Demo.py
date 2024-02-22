import streamlit as st
import json

# Carregar dados do quiz
with open('content/quiz_data.json') as f:
    quiz_data = json.load(f)

# Inicializar estado se não existir
if 'current_index' not in st.session_state:
    st.session_state['current_index'] = 0
    st.session_state['score'] = 0
    st.session_state['selected_option'] = None

def handle_submit():
    current_question = quiz_data[st.session_state['current_index']]
    if st.session_state['selected_option'] == current_question['resposta']:
        st.session_state['score'] += 10
    st.session_state['current_index'] += 1
    st.session_state['selected_option'] = None  # Resetar seleção para a próxima pergunta

def handle_restart():
    st.session_state['current_index'] = 0
    st.session_state['score'] = 0
    st.session_state['selected_option'] = None

# Mostrar pergunta e opções
if st.session_state['current_index'] < len(quiz_data):
    current_question = quiz_data[st.session_state['current_index']]
    st.write(current_question['pergunta'])
    st.write(current_question['informacao'])
    
    options = current_question['opcoes']
    st.session_state['selected_option'] = st.radio("Escolha uma resposta:", options, key=f"question_{st.session_state['current_index']}")
    
    if st.button('Submeter', key=f"submit_{st.session_state['current_index']}"):
        handle_submit()

else:
    st.write(f"Parabéns, terminaste o quiz! A tua pontuação é {st.session_state['score']}.")
    if st.button('Reiniciar'):
        handle_restart()

# Mostrar pontuação e progresso
st.write(f"Pontuação: {st.session_state['score']}")
progress_bar_value = (st.session_state['current_index'] / len(quiz_data)) * 100
st.progress(int(progress_bar_value))
