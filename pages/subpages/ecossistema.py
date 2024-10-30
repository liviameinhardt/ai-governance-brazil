import streamlit as st



def eco_page():
    
    st.title("Principais empresas que atuam no setor da IA")
        
    st.warning("""A compreensão das empresas que atuam no setor de inteligência artificial (IA) é essencial para a formulação de políticas eficazes nesta área em rápida evolução. Essas organizações, que vão desde grandes multinacionais até startups inovadoras, não apenas impulsionam o avanço tecnológico, mas também enfrentam desafios éticos, como transparência e viés algorítmico. Conhecer suas práticas e modelos de negócios permitirá que os formuladores de políticas desenvolvam regulamentações que promovam um ambiente seguro e responsável, assegurando que a IA seja utilizada de maneira benéfica para a sociedade.""")
    
    st.header("Empresas globais")
    
    st.write("A Forbes em parceria com Sequoia e Meritech Capital produziu a lista 'IA 50', que reconhece as empresas de inteligência artificial mais promissoras do mundo:")
    
    st.image("data/empresas_ia_forbes.png")
    st.markdown("Fonte: [Blog Forbes](https://forbes.com.br/forbes-tech/2024/04/forbes-ia-50-as-empresas-mais-promissoras-do-mundo-em-inteligencia-artificial/)") 
              
    st.write("Podemos resumir o que cada um desses setores e subsetores significa: ")
    
    st.header("Apps")
    
    st.write("""
        1. **Consumer Uses (Usos para Consumidores)**: Aplicativos e ferramentas de IA voltados para o público em geral, divididos em entretenimento e produtividade. 
        - **Entertainment (Entretenimento)**: Ferramentas de IA para entretenimento, como chats interativos e ferramentas de geração de conteúdo criativo.
        - **Productivity (Produtividade)**: Ferramentas de IA que ajudam o usuário a ser mais produtivo em tarefas cotidianas, como assistentes de escrita, tradução e pesquisa. """)

    st.write("""
        2. **Enterprise Stack (Pilha Empresarial)**: Soluções voltadas para o mercado corporativo, com diversas subcategorias:
        - **General Productivity (Produtividade Geral)**: Ferramentas de produtividade que auxiliam as empresas em várias atividades, como escrita, tradução e organização.
        - **Learning & Development (Aprendizado e Desenvolvimento)**: Focadas em capacitação e aprendizado dentro de empresas, com treinamentos automatizados e conteúdo educativo.
        - **Customer Experience (Experiência do Cliente)**: Ferramentas para melhorar o atendimento ao cliente usando IA, incluindo chatbots e automação de atendimento.
        - **Developer & Data Teams (Desenvolvimento e Equipes de Dados)**: Soluções voltadas para desenvolvimento e análise de dados, oferecendo suporte a equipes técnicas.""")
        
    st.write("""
        3. **Industry Verticals (Verticais da Indústria)**: Ferramentas especializadas em setores específicos.
        - **Creative (Criativo)**: Plataformas para criação de conteúdo, imagens e vídeos.
        - **Defense (Defesa)**: Ferramentas de IA aplicadas ao setor de defesa e segurança.
        - **Health & Bio (Saúde e Biotecnologia)**: Soluções de IA focadas em pesquisas biotecnológicas, diagnósticos e cuidados com a saúde.
        - **Industrial (Industrial)**: Aplicações industriais de IA, como automação de fábricas e otimização de processos.
        - **Professional Services (Serviços Profissionais)**: Ferramentas para serviços como jurídico e consultoria, onde a IA ajuda a otimizar processos de trabalho.""")

    st.header("Infrastructure (Infraestrutura)")

    st.write("1. **Inference Providers (Provedores de Inferência)**: Empresas que fornecem a infraestrutura para rodar modelos de IA, permitindo que outras empresas implementem inteligência artificial em seus serviços.")

    st.write("2. **App Dev Frameworks (Frameworks de Desenvolvimento de Apps)**: Frameworks e bibliotecas que facilitam o desenvolvimento de aplicativos baseados em IA, acelerando o processo de criação.")

    st.write("3. **Model Hubs (Repositórios de Modelos)**: Plataformas que oferecem repositórios de modelos de IA pré-treinados e prontos para serem utilizados ou ajustados.")

    st.write("4. **Foundation Model Providers (Provedores de Modelos Fundamentais)**: Empresas que desenvolvem e fornecem grandes modelos de linguagem e IA, usados como base para outras aplicações")
    
    st.write("5. **Store / Process Data (Armazenamento e Processamento de Dados)**: Ferramentas e serviços que ajudam a rotular e processar grandes volumes de dados, uma etapa essencial para o treinamento de modelos de IA.")

    st.write("6. **Cloud Data Providers (Provedores de Dados em Nuvem)**: Empresas que fornecem soluções de armazenamento e processamento de dados em nuvem, fundamentais para hospedar grandes volumes de dados de IA.")

    st.write("7. **Cloud Service Providers (Provedores de Serviços em Nuvem)**: Grandes empresas de tecnologia que oferecem infraestrutura de computação em nuvem, como Google Cloud, AWS e Azure.")

    st.write("8. **Hardware**: Empresas que produzem o hardware necessário para rodar modelos de IA, como GPUs e chips especializados.")
    
    
    st.header("Empresas Brasileiras")
    st.warning("EM BREVE")

    
    
    
# """
 
#      - Character.ai
#      - Midjourney
#      - Pika
     
     
#    - **Productivity (Produtividade)**:
#      - ChatGPT
#      - Claude
#      - DeepL
#      - Perplexity
#      - Notion
#      - Tome

# 2. **Enterprise Stack (Pilha Empresarial)**:
#    - **General Productivity (Produtividade Geral)**:
#      - ChatGPT
#      - DeepL
#      - Glean
#      - Tome
#      - Adept
#      - Claude
#      - Notion
#      - Writer
#    - **Learning & Development (Aprendizado e Desenvolvimento)**:
#      - Sana
#      - Synthesia
#    - **Customer Experience (Experiência do Cliente)**:
#      - Cresta
#      - Sierra
#    - **Developer & Data Teams (Desenvolvimento e Equipes de Dados)**:
#      - AssemblyAI
#      - Kumo
#      - Codeium
#      - GitHub

# 3. **Industry Verticals (Verticais da Indústria)**:
#    - **Creative (Criativo)**:
#      - Midjourney
#      - Photoroom
#      - Runway
#      - Rosebud AI
#      - Pika
#      - 11eleven Labs
#      - Leonardo.Ai
#    - **Defense (Defesa)**:
#      - Anduril
#      - Vannevar Labs
#    - **Health & Bio (Saúde e Biotecnologia)**:
#      - Abridge
#      - Cradle
#      - Insitro
#      - Owkin
#    - **Industrial (Industrial)**:
#      - Figure
#      - Traction
#      - Waabi
#    - **Professional Services (Serviços Profissionais)**:
#      - Harvey
#      - Hebbia


# ### Infrastructure (Infraestrutura)

# 1. **Inference Providers (Provedores de Inferência)**:
#    - Anyscale
#    - Databricks
#    - Replicate
#    - Together.ai
#    - Baseten

# 2. **App Dev Frameworks (Frameworks de Desenvolvimento de Apps)**:
#    - LangChain

# 3. **Model Hubs (Repositórios de Modelos)**:
#    - Hugging Face
#    - Replicate

# 4. **Foundation Model Providers (Provedores de Modelos Fundamentais)**:
#    - Anthropic
#    - Cohere
#    - Mistral AI
#    - OpenAI

# 5. **Store / Process Data (Armazenamento e Processamento de Dados)**:
#    - Cleanlab
#    - Scale
#    - Unstructured

# 6. **Cloud Data Providers (Provedores de Dados em Nuvem)**:
#    - Databricks
#    - Pinecone
#    - Weaviate
#    - MongoDB
#    - Snowflake

# 7. **Cloud Service Providers (Provedores de Serviços em Nuvem)**:
#    - Google Cloud
#    - AWS
#    - Azure

# 8. **Hardware**:
#    - Cerebras
#    - NVIDIA
#    - AMD
#    - Intel

# """