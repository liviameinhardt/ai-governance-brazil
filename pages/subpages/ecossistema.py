import streamlit as st



def eco_page():
    
    st.title("Principais empresas que atuam no setor da IA")
        
    st.warning("""A compreensão das empresas que atuam no setor de inteligência artificial (IA) é essencial para a formulação de políticas eficazes nesta área em rápida evolução. Essas organizações, que vão desde grandes multinacionais até startups inovadoras, não apenas impulsionam o avanço tecnológico, mas também enfrentam desafios éticos, como transparência e viés algorítmico. Conhecer suas práticas e modelos de negócios permitirá que os formuladores de políticas desenvolvam regulamentações que promovam um ambiente seguro e responsável, assegurando que a IA seja utilizada de maneira benéfica para a sociedade.""")
    
    st.header("Empresas globais")

    
    
    st.write("""A Forbes em parceria com Sequoia e Meritech Capital produziu a lista 'IA 50', que reconhece as empresas de inteligência artificial mais promissoras do mundo. 
             Abaixo, resumimos cada um dos setores e subsetores presentes. A imagem apresenta as empresas que compõem a lista de 2024.
             """)
    
    col1, col2 = st.columns(2)
    apps, infra = col1.tabs(["Apps", "Infraestrutura"])

    with apps:
        
        st.write("1. **Consumer Uses (Usos para Consumidores)**: Aplicativos e ferramentas de IA voltados para o público em geral, divididos em entretenimento e produtividade. ")
        cola, colb = st.columns(2)

        cola.info("**Entertainment (Entretenimento)**: Ferramentas de IA para entretenimento, como chats interativos e ferramentas de geração de conteúdo criativo.")
        colb.info("**Productivity (Produtividade)**: Ferramentas de IA que ajudam o usuário a ser mais produtivo em tarefas cotidianas, como assistentes de escrita, tradução e pesquisa.")

        st.write("""2. **Enterprise Stack (Pilha Empresarial)**: Soluções voltadas para o mercado corporativo, com diversas subcategorias:""")
        cola, colb, colc, cold = st.columns(4)

        cola.info("**General Productivity (Produtividade Geral)**: Ferramentas de produtividade que auxiliam as empresas em várias atividades, como escrita, tradução e organização.")
        colb.info("**Learning & Development (Aprendizado e Desenvolvimento)**: Focadas em capacitação e aprendizado dentro de empresas, com treinamentos automatizados e conteúdo educativo.")
        colc.info("**Customer Experience (Experiência do Cliente)**: Ferramentas para melhorar o atendimento ao cliente usando IA, incluindo chatbots e automação de atendimento.")
        cold.info("**Developer & Data Teams (Desenvolvimento e Equipes de Dados)**: Soluções voltadas para desenvolvimento e análise de dados, oferecendo suporte a equipes técnicas.")
        
        st.write(""" 3. **Industry Verticals (Verticais da Indústria)**: Ferramentas especializadas em setores específicos.""")

        cola, colb, colc, cold, cole = st.columns(5)

        cola.info("**Creative (Criativo)**: Plataformas para criação de conteúdo, imagens e vídeos.")
        colb.info("**Defense (Defesa)**: Ferramentas de IA aplicadas ao setor de defesa e segurança.")
        colc.info("**Health & Bio (Saúde e Biotecnologia)**: Soluções de IA focadas em pesquisas biotecnológicas, diagnósticos e cuidados com a saúde.")
        cold.info("**Industrial (Industrial)**: Aplicações industriais de IA, como automação de fábricas e otimização de processos.")
        cole.info("**Professional Services (Serviços Profissionais)**: Ferramentas para serviços como jurídico e consultoria, onde a IA ajuda a otimizar processos de trabalho.")
        

    with infra:

        st.write("1. **Inference Providers (Provedores de Inferência)**: Empresas que fornecem a infraestrutura para rodar modelos de IA, permitindo que outras empresas implementem inteligência artificial em seus serviços.")

        st.write("2. **App Dev Frameworks (Frameworks de Desenvolvimento de Apps)**: Frameworks e bibliotecas que facilitam o desenvolvimento de aplicativos baseados em IA, acelerando o processo de criação.")

        st.write("3. **Model Hubs (Repositórios de Modelos)**: Plataformas que oferecem repositórios de modelos de IA pré-treinados e prontos para serem utilizados ou ajustados.")

        st.write("4. **Foundation Model Providers (Provedores de Modelos Fundamentais)**: Empresas que desenvolvem e fornecem grandes modelos de linguagem e IA, usados como base para outras aplicações")
        
        st.write("5. **Store & Compute**")
        cola, colb, colc = st.columns(3)

        cola.info("**Label / Process Data (Armazenamento e Processamento de Dados)**: Ferramentas e serviços que ajudam a rotular e processar grandes volumes de dados, uma etapa essencial para o treinamento de modelos de IA.")
        colb.info("**Cloud Data Providers (Provedores de Dados em Nuvem)**: Empresas que fornecem soluções de armazenamento e processamento de dados em nuvem, fundamentais para hospedar grandes volumes de dados de IA.")
        colc.info("**Cloud Service Providers (Provedores de Serviços em Nuvem)**: Grandes empresas de tecnologia que oferecem infraestrutura de computação em nuvem, como Google Cloud, AWS e Azure.")
        
        st.write("6. **Hardware**: Empresas que produzem o hardware necessário para rodar modelos de IA, como GPUs e chips especializados.")
        

    col2.image("data/empresas_ia_forbes.png")
    col2.markdown("Fonte: [Blog Forbes](https://forbes.com.br/forbes-tech/2024/04/forbes-ia-50-as-empresas-mais-promissoras-do-mundo-em-inteligencia-artificial/)") 
              
    
    st.header("Empresas Brasileiras")

    st.write("""Para uma visão geral das empresas brasileiras, leia o relatório ["Startups & Inteligência Artificial Generativa"](https://services.google.com/fh/files/events/relatorio_startups_genai.pdf) produzido pela Google.
              **Você só precisa ler as páginas 30-40**""")

    st.markdown("""### LLMS Brasileiros""")
    st.write('Apresentamos aqui duas empresas brasileiras que desenvolvem modelos de linguagem focamos no português:')
    st.markdown("[Maritaca AI](https://www.maritaca.ai): criadora do Sabiá")
    st.markdown(" [Wise labs](https://www.widelabs.com.br): criadora do Amazonia IA")


                
               
                

        
