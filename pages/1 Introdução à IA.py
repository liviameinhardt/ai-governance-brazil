import streamlit as st

from pages.subpages.ia_triad import ia_triad
from pages.subpages.ecossistema import eco_page


st.set_page_config(layout="wide",page_title="Introdução à IA")

st.title("Introdução à Inteligência Artificial")

st.warning("""Neste módulo, você vai entender o que de fato é a IA, como os modelos são treinados, sua evolução ao longo dos anos e, finalmente,
           as principais empresas que compõe o ecossistema global de IA. """)

st.caption("É recomendado seguir a ordem das leituras abaixo. Sugestões de qualquer natureza são bem vindas. ")

with st.expander("Breve introdução à IA"):
    st.markdown("[O que é inteligência artificial (IA)? *pela IBM*](https://www.ibm.com/br-pt/topics/artificial-intelligence)")

with st.expander("Diferença entre IA, Machine Learning e Deep Learning"):
    st.markdown("[Qual é a Diferença entre Inteligência Artificial, Machine Learning e Deep Learning? *pela NVIDIA*](https://blog.nvidia.com.br/blog/qual-e-a-diferenca-entre-inteligencia-artificial-machine-learning-e-deep-learning/)")

with st.expander("A Tríade da IA: Algoritmos, Dados e Poder Computacional"):
    ia_triad()
    
with st.expander("Evolução da IA"):
    st.markdown("[Visualizando a revolução do aprendizado profundo *por Ricardo Ngo; traduzido*](https://medium-com.translate.goog/@richardcngo/visualizing-the-deep-learning-revolution-722098eb9c5?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=wapp&_x_tr_hist=true)")

with st.expander("Como funciona o GPT"):
    st.markdown("[Explicação para não técnicos *por Guodong (Troy) Zhao; tradução*](https://newrizon.global/blog/entendendo-o-funcionamento-do-chatgpt-de-forma-simples-um-guia-para-nao-tecnicos/)")
    st.markdown("[Explicação mais técnica *por 3b1b; animação*](https://youtu.be/wjZofJX0v4M) Assita somente se quiser saber mais detalhes sobre o funcionamento do GPT")


with st.expander("Principais empresas no ecossistema da IA"):
    eco_page()


with st.expander("Recursos Extras"):
    st.markdown("[Como deep learning funciona](https://www.3blue1brown.com/topics/neural-networks) *por 3b1b; série de vídeos em inglês, com teor matemático*")
    st.markdown("[Recursos da Bluedot](https://course.aisafetyfundamentals.com/governance?session=1) *por Bluedot; curso em inglês sobre governança de IA*")
    st.markdown("[Como um modelo é construido](https://medium.com/@elieser_ribeiro/construindo-um-c%C3%A9rebro-em-10-minutos-2e6afd38a632) *por NVIDIA; traduzido por Eliéser de Freitas Ribeiro*")

