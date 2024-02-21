import streamlit as st

st.markdown("""
             # Quizz 

             ___ 
             
             
             
                Nesta secção é possível testar os conhecimentos sobre o setor público português.
             ___ 
             """)

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
    st.session_state.show_answer = False
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'estado_botao' not in st.session_state:
    st.session_state.estado_botao = 'Submeter'

# Função para lidar com as ações do botão
def handle_quiz_action():
    if st.session_state.estado_botao == 'Submeter':
        st.session_state.show_answer = True
        st.session_state.answered = True
        if st.session_state.current_question < len(quiz):
            if user_choice == quiz[st.session_state.current_question]["resposta"]:
                st.session_state.score += 10
        st.session_state.estado_botao = 'Avançar'
    elif st.session_state.estado_botao == 'Avançar':
        if st.session_state.current_question < len(quiz) - 1:
            st.session_state.current_question += 1
            st.session_state.show_answer = False
            st.session_state.answered = False
            st.session_state.estado_botao = 'Submeter'
        else:
            st.session_state.estado_botao = 'Reiniciar'
    elif st.session_state.estado_botao == 'Reiniciar':
        st.session_state.score = 0
        st.session_state.current_question = 0
        st.session_state.show_answer = False
        st.session_state.answered = False
        st.session_state.estado_botao = 'Submeter'

def display_question(question):
    st.subheader(question["pergunta"])
    st.write(question["informacao"])
    # A chave no 'st.radio' ajuda a garantir que diferentes chamadas sejam tratadas de forma independente
    chosen_option = st.radio("Escolhas:", question["opcoes"], key=f"question_{st.session_state.current_question}")
    return chosen_option

# Exibe a pergunta atual e as opções
if st.session_state.current_question < len(quiz):
    user_choice = display_question(quiz[st.session_state.current_question])
    if st.session_state.show_answer:
        if user_choice == quiz[st.session_state.current_question]["resposta"]:
            st.success('Correto!')
        else:
            st.error(f'Errado! A resposta correta é {quiz[st.session_state.current_question]["resposta"]}.')
else:
    st.write(f"Fim do quiz! A tua pontuação é {st.session_state.score} de {len(quiz) * 10}.")

# Botão para ação com base no estado
if st.button(st.session_state.estado_botao):
    handle_quiz_action()

# Atualiza a pontuação e o progresso na sidebar
st.sidebar.metric(label="Pontuação", value=f"{st.session_state.score} / {len(quiz) * 10}")
st.sidebar.progress(st.session_state.current_question / len(quiz))
