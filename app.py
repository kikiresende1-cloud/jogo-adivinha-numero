import streamlit as st
import random

st.set_page_config(page_title="Adivinha o Número", page_icon="🎮")

st.title("🎮 Jogo: Adivinha o Número")
st.write("Tenta descobrir o número secreto!")

dificuldade = st.selectbox(
    "Escolhe a dificuldade:",
    ["Fácil (1-50, 10 tentativas)", "Médio (1-100, 7 tentativas)", "Difícil (1-200, 5 tentativas)"]
)

if dificuldade == "Fácil (1-50, 10 tentativas)":
    max_numero = 50
    max_tentativas = 10
elif dificuldade == "Médio (1-100, 7 tentativas)":
    max_numero = 100
    max_tentativas = 7
else:
    max_numero = 200
    max_tentativas = 5

if "numero_secreto" not in st.session_state:
    st.session_state.numero_secreto = random.randint(1, max_numero)
    st.session_state.tentativas = 0
    st.session_state.fim_jogo = False
    st.session_state.dificuldade_atual = dificuldade

if st.session_state.dificuldade_atual != dificuldade:
    st.session_state.numero_secreto = random.randint(1, max_numero)
    st.session_state.tentativas = 0
    st.session_state.fim_jogo = False
    st.session_state.dificuldade_atual = dificuldade

st.info(f"Escolhi um número entre 1 e {max_numero}. Tens {max_tentativas} tentativas.")

palpite = st.number_input(
    "Qual é o teu palpite?",
    min_value=1,
    max_value=max_numero,
    step=1
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Tentar") and not st.session_state.fim_jogo:
        st.session_state.tentativas += 1

        if palpite < st.session_state.numero_secreto:
            st.warning("🔺 O número é maior.")
        elif palpite > st.session_state.numero_secreto:
            st.warning("🔻 O número é menor.")
        else:
            st.success(f"🎉 Acertaste em {st.session_state.tentativas} tentativas!")
            st.balloons()
            st.session_state.fim_jogo = True

        if st.session_state.tentativas >= max_tentativas and not st.session_state.fim_jogo:
            st.error(f"😢 Perdiste! O número secreto era {st.session_state.numero_secreto}.")
            st.session_state.fim_jogo = True

with col2:
    if st.button("Novo jogo"):
        st.session_state.numero_secreto = random.randint(1, max_numero)
        st.session_state.tentativas = 0
        st.session_state.fim_jogo = False
        st.session_state.dificuldade_atual = dificuldade
        st.rerun()

st.info(f"📊 Tentativas: {st.session_state.tentativas} / {max_tentativas}")

if st.session_state.fim_jogo:
    st.write("Podes carregar em **Novo jogo** para jogar outra vez.")
    