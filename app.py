import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Simulador de Cashback",
    layout="wide"
)

# Estilo (fundo preto, letra branca)
st.markdown("""
<style>
body {
    background-color: #000000;
}
.block-container {
    padding: 2rem;
}
h1, h2, h3, h4, h5, h6, label, p, span, div {
    color: #FFFFFF !important;
}
input, select, textarea {
    color: #000000 !important;
}
.stButton > button {
    background-color: #FFD700;
    color: #000000;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

# Título
st.title("🧮 Simulador Interno de Cashback")

st.write("Ferramenta interna para simulação de uso de cashback.")

st.divider()

# Configurações
st.subheader("Configurações")

col1, col2 = st.columns(2)

with col1:
    cashback_total = st.number_input(
        "Cashback total disponível (R$)",
        min_value=0.0,
        step=50.0
    )

with col2:
    proporcao = st.selectbox(
        "Proporção de uso",
        [3, 4]
    )

st.divider()

# Modo de cálculo
modo = st.radio(
    "O que você quer calcular?",
    (
        "Quanto preciso comprar para usar um valor de cashback",
        "Quanto de cashback posso usar com um valor de compra"
    )
)

mensagem = ""

# Modo 1
if modo == "Quanto preciso comprar para usar um valor de cashback":
    cashback_desejado = st.number_input(
        "Quanto de cashback deseja utilizar (R$)",
        min_value=0.0,
        max_value=cashback_total,
        step=50.0
    )

    valor_compra = cashback_desejado * proporcao

    st.success(f"Valor mínimo da compra: R$ {valor_compra:,.2f}")

    mensagem = (
        f"Simulação de Cashback\n"
        f"Cashback utilizado: R$ {cashback_desejado:,.2f}\n"
        f"Proporção: {proporcao}x\n"
        f"Valor mínimo da compra: R$ {valor_compra:,.2f}"
    )

# Modo 2
else:
    valor_compra = st.number_input(
        "Valor da compra (R$)",
        min_value=0.0,
        step=100.0
    )

    cashback_utilizado = valor_compra / proporcao

    st.success(f"Cashback utilizado: R$ {cashback_utilizado:,.2f}")

    mensagem = (
        f"Simulação de Cashback\n"
        f"Valor da compra: R$ {valor_compra:,.2f}\n"
        f"Proporção: {proporcao}x\n"
        f"Cashback utilizado: R$ {cashback_utilizado:,.2f}"
    )

st.divider()

# Mensagem WhatsApp
st.subheader("Mensagem para WhatsApp")

st.text_area(
    "Copie e cole no atendimento",
    mensagem,
    height=150
)

st.button("📋 Copiar mensagem")
