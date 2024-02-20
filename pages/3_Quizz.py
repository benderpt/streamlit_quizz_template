import streamlit as st
from streamlit.logger import get_logger


st.markdown ("""
             # Quizz 

             ___ 
             
             
             
                Nesta secção é possível testar os conhecimentos sobre o setor público português.
             ___ 
             """)

import streamlit as st

# Define as perguntas, opções e respostas corretas
quiz = [
    {"pergunta": "Pergunta 1", "informacao": "Informação 1", "opcoes": ["A", "B", "C", "D"], "resposta": "A"},
    {"pergunta": "Pergunta 2", "informacao": "Informação 2", "opcoes": ["A", "B", "C", "D"], "resposta": "B"},
    # Adiciona mais perguntas conforme necessário
]

# Inicializa o estado necessário
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False  # Nova flag para controlar a exibição da resposta

# Função para exibir a pergunta e as opções
def display_question(question):
    st.subheader(question["pergunta"])
    st.write(question["informacao"])
    chosen_option = st.radio("Escolhas:", question["opcoes"], key=f"question_{st.session_state.current_question}")
    return chosen_option

# Lógica para controlar o fluxo do quiz
if st.session_state.current_question < len(quiz):
    user_choice = display_question(quiz[st.session_state.current_question])
    if st.session_state.show_answer:
        # Mostra a resposta correta e atualiza a pontuação
        if user_choice == quiz[st.session_state.current_question]["resposta"]:
            st.success('Correto!')
            if not st.session_state.answered:
                st.session_state.score += 10  # Aumenta a pontuação apenas uma vez por pergunta
        else:
            st.error(f'Errado! A resposta correta é {quiz[st.session_state.current_question]["resposta"]}.')
        button_label = "Avançar"
    else:
        button_label = "Submeter resposta"
        st.session_state.answered = False  # Resetar o estado de resposta dada para a próxima pergunta

    if st.button(button_label):
        if st.session_state.show_answer:
            # Avança para a próxima pergunta
            st.session_state.current_question += 1
            st.session_state.show_answer = False
        else:
            # Mostra a resposta para a pergunta atual
            st.session_state.show_answer = True
            st.session_state.answered = True  # Marcar que o usuário já respondeu à pergunta

# Final do quiz
if st.session_state.current_question >= len(quiz):
    st.write(f"Fim do quiz! A tua pontuação é {st.session_state.score} de {len(quiz) * 10}.")
    if st.button("Reiniciar Quiz"):
        st.session_state.score = 0
        st.session_state.current_question = 0
        st.session_state.show_answer = False

# Mostra a pontuação e o progresso na sidebar
st.sidebar.metric(label="Pontuação", value=f"{st.session_state.score} / {len(quiz) * 10}")
st.sidebar.progress(st.session_state.current_question / len(quiz))

