import streamlit as st
import json

# Carrega os dados do quiz
with open('content/quiz_data.json', 'r', encoding='utf-8') as f:
    quiz_data = json.load(f)

# Inicia variáveis de sessão se ainda não existirem
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = None
if 'answer_submitted' not in st.session_state:
    st.session_state.answer_submitted = False

def restart_quiz():
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.selected_option = None
    st.session_state.answer_submitted = False

# Função para lidar com a submissão da resposta
def submit_answer():
    st.session_state.answer_submitted = True
    if st.session_state.selected_option == quiz_data[st.session_state.current_index]['resposta']:
        st.session_state.score += 10

# Função para avançar para a próxima pergunta
def next_question():
    st.session_state.current_index += 1
    st.session_state.selected_option = None
    st.session_state.answer_submitted = False

# Mostra a pergunta e as opções de resposta
question_item = quiz_data[st.session_state.current_index]
st.write(f"Q{st.session_state.current_index + 1}: {question_item['pergunta']}")
st.write(question_item['informacao'])

# Seleção de resposta
options = question_item['opcoes']
for i, option in enumerate(options):
    if st.button(option, key=i, use_container_width=True):
        st.session_state.selected_option = option

st.markdown(""" ___
<style>
div.stButton > button:first-child {
    display: block;
    margin: 0 auto;
}
</style>
""", unsafe_allow_html=True)

# Botão de submissão e lógica de exibição da resposta
if st.session_state.answer_submitted:
    if st.session_state.selected_option == question_item['resposta']:
        st.success("Resposta correta!")
    else:
        st.error(f"Resposta incorreta! A resposta correta é: {question_item['resposta']}")
    if st.session_state.current_index < len(quiz_data) - 1:
        st.button('Avançar', on_click=next_question)
    else:
        st.write(f"Quiz concluído! A tua pontuação é: {st.session_state.score} / {len(quiz_data) * 10}")
        if st.button('Reiniciar', on_click=restart_quiz):
            # Este botão reiniciará o questionário
            pass
else:
    if st.session_state.current_index < len(quiz_data):  # Garante que o botão Submeter só apareça se ainda houver perguntas.
        st.button('Submeter', on_click=submit_answer)



# Barra de progresso
progress_bar_value = (st.session_state.current_index + 1) / len(quiz_data)

