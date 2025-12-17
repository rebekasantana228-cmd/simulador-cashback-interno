import streamlit as st

st.set_page_config(page_title="Simulador de Cashback", layout="wide")

st.markdown("""
<style>
body {
    background-color: #000;
}
.block-container {
    padding: 2rem;
}
h1, h2, h3, label, p {
    color: #FFD700 !important;
}
.stButton>button {
    background-color: #FFD700;
    color: black;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("🧮 Simulador de Cashback")

st.subheader("Configurações")

cashback_total = st.number_input("Valor total de cashback disponível (R$)", min_value=0.0, step=50.0)
proporcao = st.selectbox("Proporção de uso", [3, 4])

st.divider()

modo = st.radio(
    "O que você quer calcular?",
    ["Quanto preciso comprar para usar parte do cashback",
     "Quanto de cashback posso usar com uma compra"]
)

if modo == "Quanto preciso comprar para usar parte do cashback":
    cashback_desejado = st.number_input(
        "Quanto de cashback você quer usar (R$)",
        min_value=0.0,
        max_value=cashback_total,
        step=50.0
    )

    valor_compra = cashback_desejado * proporcao

    st.success(f"🛒 Valor mínimo da compra: R$ {valor_compra:,.2f}")

    mensagem = (
        f"Simulação de cashback:\n"
        f"Cashback utilizado: R$ {cashback_desejado:,.2f}\n"
        f"Proporção: {proporcao}x\n"
        f"Compra mínima: R$ {valor_compra:,.2f}"
    )

else:
    valor_compra = st.number_input("Valor da compra (R$)", min_value=0.0, step=100.0)
    cashback_utilizado = valor_compra / proporcao

    st.success(f"💰 Cashback utilizado: R$ {cashback_utilizado:,.2f}")

    mensagem = (
        f"Simulação de cashback:\n"
        f"Valor da compra: R$ {valor_compra:,.2f}\n"
        f"Proporção: {proporcao}x\n"
        f"Cashback utilizado: R$ {cashback_utilizado:,.2f}"
    )

st.divider()

st.text_area("Mensagem para WhatsApp", mensagem, height=150)

st.button("📋 Copiar mensagem")
