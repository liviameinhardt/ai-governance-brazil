import streamlit as st

from pages.subpages.frameworkds_intro import frameworkds_intro

st.set_page_config(layout="wide",page_title="Frameworks de Governança")

st.title("Frameworks de Governança")

# st.warning("""Nesse módulo você vai """)

st.caption("É recomendado seguir a ordem das leituras abaixo. Sugestões de qualquer natureza são bem vindas. ")

with st.expander("A Tríade da IA para regulamentação"):
    frameworkds_intro()

with st.expander("Um framework para regulamentação"):
    st.warning("EM BREVE")
    # 2. https://cetas.turing.ac.uk/sites/default/files/2023-08/cetas-cltr_ai_risk_briefing_paper.pdf


with st.expander("Governança tecnológica e acordos internacionais"):
    st.markdown("[Estudos de casos históricos de governança tecnológica e acordos internacionais (compilação – vários autores)](https://aisafetyfundamentals-com.translate.goog/blog/historical-case-studies/?_gl=1*j8sygm*_ga*MTg0MTc1OTcxNy4xNzI1OTI3MjU4*_ga_8W59C8ZY6T*MTczMDMzNTg3MS4yMC4xLjE3MzAzNDAxNjkuMC4wLjA&_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=wapp)")
    st.markdown("[Cooperação Internacional brasileira para Transformação digital](https://www.gov.br/governodigital/pt-br/estrategias-e-governanca-digital/transformacao-digital/cooperacao-internacional)")