import streamlit as st

st.set_page_config(layout="wide",page_title="Benefícios vs Riscos")


st.title("Riscos e Benefícios da IA")

st.warning("""Nesse módulo você vai entender como a IA está impactando o dia a dia dos brasileiros,
            algumas aplicações e benefícios da IA, alguns riscos atuais e futuros que a IA pode trazer e como podemos evita-los.""")

st.caption("É recomendado seguir a ordem das leituras abaixo. Sugestões de qualquer natureza são bem vindas. ")

#############

with st.expander("Breve introdução: como a IA está impactando o dia a dia dos brasileiros"):

    st.write("""
    A inteligência artificial (IA) está rapidamente remodelando o cenário profissional e cotidiano ao nosso redor, e o Brasil se destaca como o país da América Latina que mais adota essa tecnologia em suas empresas. Com mais de 40% das organizações já implementando IA em processos e outras 34% explorando novas soluções, as possibilidades são vastas, desde automação de tarefas repetitivas até o suporte a decisões estratégicas. Ao mesmo tempo, essa revolução tecnológica suscita uma série de discussões éticas e sociais, abordando questões sobre discriminação algorítmica, privacidade e a substituição de empregos tradicionais por sistemas automatizados. Muitos especialistas alertam para a necessidade de uma regulamentação sólida, que equilibre inovação com segurança, ao mesmo tempo em que profissionais precisam desenvolver habilidades mais flexíveis e adaptáveis.
    Conforme explorado no vídeo, a transformação digital impulsionada pela IA não se limita a um setor específico, afetando áreas como direito, medicina e até mesmo robótica avançada. Esse avanço traz consigo a promessa de um mundo mais eficiente, mas também demanda que nos adaptemos à velocidade disruptiva dessas mudanças. Institutos e empresas se preparam para capacitar suas equipes para essa nova realidade, onde a compreensão de IA e a habilidade de integração tecnológica se tornam diferenciais indispensáveis.
        """)
    
    st.markdown("O resumo acima foi baseado no vídeo [Inteligência artificial - benefícios e riscos | Jornada ](https://www.youtube.com/watch?v=SElGGa4sJ2o)")

with st.expander("Algumas aplicações e benefícios da IA"):

    st.info("A lista abaixo exemplifica **algumas** das aplicações e benefícios da IA, mas não é exaustiva.")
    st.markdown("Todas elas foram retiradas do vídeo [Riscos e benefícios da inteligencia artificial | Marco Aurélio | TEDx](https://youtu.be/6kTrYWXI3f8?t=61)")

    st.write("""
            ### Aplicações Benéficas da Inteligência Artificial

            1. **Sistemas de Recomendação**
                - Sugestão de conexões em redes sociais (Instagram, Facebook).
                - Recomendação de vídeos, músicas e produtos em plataformas como YouTube, Spotify e Amazon.

            2. **Detecção de Fraudes**
                - Análise de transações de cartão de crédito para identificar atividades suspeitas por meio de algoritmos de detecção de anomalias.

            3. **Otimização de Rotas**
                - Logística e trânsito em grandes cidades, visando redução de congestionamentos e entregas rápidas (ex. pizza delivery).

            4. **Análise Física e Pessoal**
                - Relógios de corrida calculam calorias gastas com base em dados como distância, horário e batimento cardíaco, usando algoritmos de regressão.

            5. **Processamento de Linguagem Natural (NLP)**
                - Tradução automática (Google Tradutor), criação de assistentes virtuais e chatbots.
                - Identificação de sentimentos e personalidade, usada na triagem de chamadas de emergência (trote) para serviços de ambulância e polícia.

            6. **Reconhecimento de Imagem e Análise de Vídeo**
                - Detecção de câncer de pele com precisão comparável a médicos.
                - Câmeras descrevem cenas para deficientes visuais.
                - Monitoramento e segurança pública (ex. deslocamento de policiais e identificação de pessoas desaparecidas).

            7. **Robótica e Automação Industrial**
                - Robôs na fabricação de componentes eletrônicos, carros e outros produtos em larga escala.
                - Miniaturização de robôs para uso doméstico, como robôs que varrem a casa, dobram roupas, ou auxiliam na cozinha.

            8. **Carros Autônomos**
                - Integração de diversas tecnologias de IA para navegação, segurança e experiência do usuário.
             """)


    #adidionar noticias relacionadas a cada risco, se possível
# https://aisafetyfundamentals.com/blog/ai-risks/?_gl=1*an39nl*_ga*MTEzODI4NjYzOC4xNzI3MDQ5MjI0*_ga_8W59C8ZY6T*MTczMDI5NzMxNC4xNy4xLjE3MzAzMDIyNjguMC4wLjA
# https://www.safe.ai/ai-risk
#problema do controle: https://youtu.be/UJuWTpAzuyc


with st.expander("Riscos atuais e possíveis da IA"): 
    
    st.header("Riscos atuais e possíveis da IA")

    st.write("A lista abaixo apresenta *alguns* riscos que a IA já comete, com exemplos reais e ainda introduz alguns riscos futuros. A lista não é exaustiva, caso tenha interesse busque outros exemplos e tipos de riscos.")

    st.markdown("[Quais são os riscos que a IA apresenta?  de Adam Jones](https://aisafetyfundamentals-com.translate.goog/blog/ai-risks/?_gl=1*an39nl*_ga*MTEzODI4NjYzOC4xNzI3MDQ5MjI0*_ga_8W59C8ZY6T*MTczMDI5NzMxNC4xNy4xLjE3MzAzMDIyNjguMC4wLjA&_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=wapp)")

    st.write("Ao final da lista, o autor aborda o problema do controle. Para entender melhor esse risco, recomenda-se o seguinte vídeo:")
    col1,col2,col3 = st.columns([1,2,1])
    col2.video("https://youtu.be/UJuWTpAzuyc")

    st.write("Por fim, destacamos outros riscos catastróficos que podem surgir com a IA:")
    st.markdown("[Uma visão geral dos riscos catastróficos da IA](https://www-safe-ai.translate.goog/ai-risk?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=wapp)")

             

with st.expander("Alinhamento"): 
    # st.error("EM BREVE")

    st.header("O problema do Alinhamento da IA")
    col1,col2,col3 = st.columns([1,2,1])
    col2.video("https://youtu.be/IH-wBijX53M")

    st.markdown("Entenda mais sobre o que é alinhamento no post [O que é alinhamento de IA? de Adam Jones](https://aisafetyfundamentals-com.translate.goog/blog/what-is-ai-alignment/?_gl=1*k9eobs*_ga*MTg0MTc1OTcxNy4xNzI1OTI3MjU4*_ga_8W59C8ZY6T*MTczMDMzNTg3MS4yMC4xLjE3MzAzMzg2MTUuMC4wLjA&_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=wapp)")

    # pass #adidionar noticias relacionadas a cada risco, se possível
    # O Verdadeiro Problema de Inteligências Artificiais: 
    # https://aisafetyfundamentals.com/blog/what-is-ai-alignment/?_gl=1*k9eobs*_ga*MTg0MTc1OTcxNy4xNzI1OTI3MjU4*_ga_8W59C8ZY6T*MTczMDMzNTg3MS4yMC4xLjE3MzAzMzg2MTUuMC4wLjA.
    

with st.expander("Recursos Extras"):
    st.markdown("[A IA terá um impacto duradouro na forma como vivemos? *Blog Bosch* ](https://www.bosch.com.br/noticias-e-historias/aiot/bosch-tech-compass-2024/?utm_source=sem&utm_medium=click&utm_campaign=Digitaliza%C3%A7%C3%A3o&utm_content=Techcompass&gad_source=1&gclid=Cj0KCQjwsoe5BhDiARIsAOXVoUsha25LKap6ybqk-mZ_emOoYDJqbshTTNMVHCVW0gBhFhTFT3Y7X10aAkX9EALw_wcB)")
    st.markdown("[The Transformative Potential of AGI — and When It Might Arrive | Shane Legg and Chris Anderson | TED](https://youtu.be/kMUdrUP-QCs?t=108) *somente em inglês*")
    st.markdown("[Intro to AI Safety, Remastered](https://youtu.be/pYXy-A4siMw) *somente em inglês*")
    st.markdown("[Curso de Alinhamento da Bluedot](https://course.aisafetyfundamentals.com/alignment?session=2) *somente em inglês*")



