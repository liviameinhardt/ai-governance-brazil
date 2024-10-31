import streamlit as st


def frameworkds_intro():

        st.title("A Tríade da IA na regulação")

        st.warning("""
                A tríade da IA — composta por algoritmos, dados e capacidade de computação — é uma estrutura útil para compreender e analisar a evolução da inteligência artificial, especialmente à luz do ritmo acelerado de avanços e da complexidade dos sistemas modernos. Essa tríade permite diferenciar inovações que se destacam pelo design algorítmico daquelas que se destacam pelo uso intenso de recursos computacionais, ajudando tanto a desmistificar os avanços em IA quanto a identificar áreas de inovação que requerem abordagens distintas.

                Além de facilitar a compreensão do que está acontecendo na área de IA, a tríade fornece uma estrutura para decisões estratégicas em políticas de segurança nacional. Cada elemento — algoritmos, dados e computação — traz diferentes desafios e oportunidades para as políticas públicas, influenciando a formulação de estratégias conforme a prioridade dada a cada um deles. Ao longo deste texto, exploraremos três cenários principais: (1) quando algoritmos assumem a prioridade máxima, (2) quando os dados ocupam o centro das atenções, e (3) quando a capacidade computacional é considerada o recurso mais crítico. Em cada um desses cenários, emergem diferentes alavancas políticas e questões fundamentais para o desenvolvimento e a segurança da IA.
                """)

        st.caption(""" O conteúdo dessa página altamente é baseado no relatório 
                [*The AI Triad and What It Means for National Security Strategy*](https://cset.georgetown.edu/wp-content/uploads/CSET-AI-Triad-Report.pdf)
                        e foi traduzido e resumido utilizando CHAT-GPT.""")
    
        algorithm, data, gpu = st.tabs(["Algoritmos", "Dados", "Capacidade Computacional"])
        
#     st.title("Algoritmos")
        with algorithm:

                st.write("""
                        Em um mundo onde os algoritmos reinam, o talento e os recursos de pesquisa para desenvolvê-los se tornam preeminentes. A oferta atual desse talento não atende à demanda global. Como resultado, formuladores de políticas em nível nacional devem encontrar maneiras de atrair talentos estrangeiros para seu país, reter os que chegam e desenvolver novos talentos. As alavancas políticas resultantes incluem controle de vistos, estratégias industriais, requalificação de trabalhadores e marcos de certificação para habilidades em IA, além de investimentos educacionais para enfrentar a escassez de professores de IA. Dada a centralidade do talento em IA para os avanços algorítmicos, essas funções governamentais de rotina podem assumir significativas implicações de segurança nacional e econômica. Embora aparentemente mundanas, essas áreas são o terreno onde a competição geopolítica na era da IA é primeiramente disputada.
                        """)
                
        # st.title("Dados")
        with data:

                st.write("""
                        No entanto, se os dados forem a prioridade mais alta, surgem diferentes alavancas políticas. Sob um paradigma de aprendizado de máquina orientado por dados selecionados por humanos, a possibilidade de sistemas tendenciosos a partir de conjuntos de dados tendenciosos aumenta substancialmente. Monitorar e medir o risco de viés torna-se, assim, mais importante com os dados no centro da IA; especialistas em assuntos específicos devem ser consultados para entender as possíveis fontes de viés não intencional. Algumas ideias concretas, como um sistema semelhante à rotulagem nutricional para aprendizado de máquina, também podem ajudar a esclarecer sobre os dados subjacentes nos quais os algoritmos foram treinados. Mesmo que os algoritmos permaneçam opacos e incapazes de explicar suas decisões, a transparência sobre os dados de treinamento usados e as informações contidas nesses dados poderia aumentar a confiança nos sistemas.

                        Questões de privacidade ganham importância na medida em que os dados são mais relevantes para a IA. Na medida em que existe uma tensão entre os direitos de privacidade dos usuários e o valor de seus dados no treinamento de sistemas de aprendizado de máquina, os governos devem equilibrar essa relação. Eles terão que elaborar leis e regulamentos de privacidade que protejam as liberdades civis e os direitos dos indivíduos sem restringir excessivamente a inovação que o uso de seus dados para treinamento pode viabilizar. Não é uma equação de soma zero, pois pesquisas técnicas adicionais em sistemas de aprendizado de máquina que preservam a privacidade podem ajudar os algoritmos a aprender com os dados sem revelar informações sobre indivíduos. Embora promissores, esses tipos de algoritmos constituem uma fração comparativamente pequena da pesquisa atual em aprendizado de máquina e merecem financiamento governamental adicional. Os governos também poderiam exigir que algoritmos de alto impacto – como os relacionados a decisões de liberdade condicional, risco de crédito e saúde – passem por uma avaliação rigorosa de reguladores tecnicamente informados antes de serem implantados.

                        Outras questões políticas surgirão se os dados forem centrais para o progresso do aprendizado de máquina. A importância crescente dos dados poderia motivar a aquisição e armazenamento de conjuntos de dados cada vez maiores, gerando considerações secundárias sobre cibersegurança e políticas de responsabilidade em caso de violação de dados, já que esses dados devem ser protegidos. O papel do governo como coletor e provedor de dados também se torna mais relevante nesse mundo centrado em dados. Por exemplo, como o governo deve reunir conjuntos de dados para resolver seus problemas e quais procedimentos governamentais precisam ser alterados para coletar e organizar esses dados? Mais geralmente, quais dos vastos repositórios de dados do governo devem ser disponibilizados, de que forma e para quem? Todas essas questões exigirão políticas cuidadosas para serem abordadas.
                                """)
                
        # st.title("Capacidade Computacional")
        with gpu:
                        
                st.write(""" 
                        O cenário final é que a computação seja a maior prioridade. Se for esse o caso, é vital gerenciar o fluxo de chips de computador poderosos, otimizados para cálculos de aprendizado de máquina. O controle de exportação emerge, portanto, como uma alavanca política significativa, especialmente para os Estados Unidos e seus aliados, que atualmente desfrutam de uma vantagem na fabricação de chips de computador avançados. A China depende do acesso a empresas ocidentais para equipamentos de fabricação de semicondutores avançados, como fotolitografia. Para a China, uma estratégia para desenvolver ainda mais sua indústria doméstica de chips de computador torna-se essencial para preservar a flexibilidade econômica e de segurança nacional na era da IA; por essa razão, entre outras, Pequim buscou agressivamente alternativas aos chips ocidentais. A eficácia do controle de exportação depende da tecnologia negada a nações adversárias ser superior àquela que essas nações podem produzir ou obter. Embora ainda aberta, a janela para o uso de tais controles contra a China provavelmente esteja começando a se fechar.

                        De modo mais geral, o custo da computação é uma questão importante. Se a computação se tornar muito cara para pesquisadores acadêmicos utilizarem, a pesquisa mudará para o setor privado, com potenciais efeitos negativos na inovação a longo prazo. O governo poderia desempenhar um papel em tornar a computação acessível aos pesquisadores acadêmicos para que possam continuar a formar novos especialistas e contribuir para o progresso da IA.
                        """)
        
        st.title("Conclusão")
        st.write("""
                
                Então, qual parte da tríade os formuladores de políticas devem priorizar? Depende muito do que acontece a portas fechadas nos laboratórios de pesquisa. Em geral, no entanto, os dados parecem um tanto supervalorizados e exagerados na era moderna, especialmente com o surgimento de inovações tecnológicas específicas, como a geração de dados representativos de fontes artificiais ou o desenvolvimento de algoritmos que não dependem de dados de treinamento selecionados por humanos. Embora as preocupações com privacidade e agregação de dados sejam reais, essas preocupações provavelmente são independentes da pesquisa de aprendizado de máquina verdadeiramente avançada. Embora há uma década os dados parecessem centrais – o cientista-chefe do Google, Peter Norvig, disse famosamente: “Nós não temos algoritmos melhores do que ninguém; só temos mais dados” – sua importância comparativa diminuiu um pouco, à medida que o poder dos algoritmos e da computação se tornou mais evidente.

                Os algoritmos parecem mais bem avaliados, mesmo que apenas em teoria. Os formuladores de políticas reconhecem cada vez mais a importância das inovações nessa área, mas, nos Estados Unidos, atrair o talento necessário para desenvolver algoritmos ainda não se tornou uma prioridade nacional suficiente. Em contraste, aliados como o Reino Unido, Canadá e França tentam nutrir suas indústrias domésticas de IA e atrair novos pesquisadores do exterior. A China também desenvolveu agressivamente seu programa Mil Talentos para recrutar mentes de ponta em IA e pesquisadores de outras áreas. Os Estados Unidos, que formam grande parte dos talentos de IA do mundo em suas universidades, poderiam fazer muito mais para aproveitar essa vantagem doméstica antes que ela se perca.

                Embora os dados pareçam supervalorizados e os algoritmos recebam apenas consideração superficial sem grande ação política nos Estados Unidos, a computação parece subvalorizada e subestimada em quase todos os lugares. Os avanços computacionais são difíceis de explicar e ainda mais difíceis de visualizar, talvez explicando a negligência. Dito isso, como mostra a pesquisa da OpenAI, o crescimento exponencial da computação aplicada aos sistemas de aprendizado de máquina nos últimos anos tem impulsionado uma grande parte do progresso observado. A observação mais ampla de Sutton sobre esse padrão é igualmente impressionante. O boom de startups no Vale do Silício trabalhando em computação avançada para IA sugere que ainda mais progresso nessa área está por vir, com potenciais efeitos significativos para o futuro do aprendizado de máquina, sistemas de segurança nacional que dependem dela e as escolhas disponíveis para os formuladores de políticas.
                                
                """)