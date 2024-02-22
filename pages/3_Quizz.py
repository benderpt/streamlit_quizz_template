import streamlit as st

st.markdown("""
             # O Setor Público Português 
             ___ 
             Nesta secção é possível testar os conhecimentos sobre o setor público português.
             ___ 
             """ )
quiz = [
        {"pergunta": "Qual é a entidade responsável pela administração fiscal em Portugal?", "informacao": "Esta entidade é responsável pela gestão dos tributos e supervisão aduaneira.", "opcoes": ["Autoridade Tributária e Aduaneira", "Banco de Portugal", "Instituto de Segurança Social", "Direção-Geral da Educação"], "resposta": "Autoridade Tributária e Aduaneira"},
    {"pergunta": "Qual é o sistema de saúde pública em Portugal?", "informacao": "Este sistema engloba uma rede de entidades que prestam cuidados de saúde aos cidadãos portugueses.", "opcoes": ["Serviço Nacional de Saúde", "Hospital das Forças Armadas", "Rede de Cuidados Continuados Integrados", "Centros de Saúde Privados"], "resposta": "Serviço Nacional de Saúde"},
        {
            "pergunta": "Qual é o órgão máximo do sistema judiciário em Portugal?",
            "informacao": "Este órgão é a mais alta instância da hierarquia dos tribunais judiciais em Portugal.",
            "opcoes": ["Tribunal Constitucional", "Supremo Tribunal de Justiça", "Tribunal de Contas", "Supremo Tribunal Administrativo"],
            "resposta": "Supremo Tribunal de Justiça"
        },
        {
            "pergunta": "Qual entidade é responsável pela supervisão da educação em Portugal?",
            "informacao": "Esta entidade governamental é responsável por regular e supervisionar o sistema educativo português.",
            "opcoes": ["Direção-Geral da Educação", "Fundação para a Ciência e a Tecnologia", "Instituto de Avaliação Educativa", "Agência para o Desenvolvimento e Coesão"],
            "resposta": "Direção-Geral da Educação"
        }

]

# Inicialização do estado de sessão

if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'user_choice' not in st.session_state:
    st.session_state.user_choice = [None] * len(quiz)
if 'estado_botao' not in st.session_state:
    st.session_state.estado_botao = 'Submeter'
    

def handle_quiz_action():
    current_question = st.session_state.current_question
    if st.session_state.estado_botao == 'Submeter':
        st.session_state.show_answer = True
        st.session_state.answered = True
        if current_question < len(quiz):
            if st.session_state.user_choice[current_question] == quiz[current_question]["resposta"]:
                st.session_state.score += 10
        st.session_state.estado_botao = 'Avançar'
    elif st.session_state.estado_botao == 'Avançar':
        if current_question < len(quiz) - 1:
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
        st.session_state.user_choice = [None] * len(quiz)
        st.session_state.estado_botao = 'Submeter'

def display_question(question):
    st.subheader(question["pergunta"])
    st.write(question["informacao"])
    # Usa st.columns para criar uma única coluna que irá conter os botões
    col = st.columns([1])  # Aqui estamos a criar uma única coluna para simplicidade
    for i, option in enumerate(question["opcoes"]):
        # Cada botão é agora colocado dentro da coluna e configurado para usar a largura total
        with col[0]:
            if st.button(option, key=f"{st.session_state.current_question}_{i}", use_container_width=True):
                st.session_state.user_choice[st.session_state.current_question] = option

# Exibe a pergunta atual e o botão de ação
if st.session_state.current_question < len(quiz):
    display_question(quiz[st.session_state.current_question])

st.markdown(""" ___ """ )


# Utiliza markdown com CSS para centralizar o botão
st.markdown("""
<style>
div.stButton > button:first-child {
    display: block;
    margin: 0 auto;
}
</style>
""", unsafe_allow_html=True)

# Renderiza o botão centralizado
if st.button(st.session_state.estado_botao):
    handle_quiz_action()


if st.session_state.show_answer:
    # Imediatamente após o usuário selecionar uma opção e clicar para submeter
    correct_answer = quiz[st.session_state.current_question]["resposta"]
    if st.session_state.user_choice[st.session_state.current_question] == correct_answer:
        st.success('Correto!')
    else:
        st.error(f'Errado! A resposta correta é {correct_answer}.')

# Antes de renderizar o botão "Submeter/Avançar/Reiniciar"
if st.session_state.current_question < len(quiz) and st.session_state.user_choice[st.session_state.current_question] is None:
    st.warning("Por favor, selecione uma opção antes de avançar.")

# No final do quiz
if st.session_state.current_question >= len(quiz):
    st.write(f"Fim do quiz! A tua pontuação é {st.session_state.score} / {len(quiz) * 10}.")
    if st.button("Reiniciar Quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.user_choice = [None] * len(quiz)
        st.experimental_rerun()

# Atualiza a pontuação e o progresso na sidebar
st.sidebar.metric(label="Pontuação", value=f"{st.session_state.score} / {len(quiz) * 10}")
st.sidebar.progress(st.session_state.current_question / len(quiz))
