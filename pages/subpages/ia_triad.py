import streamlit as st
import pandas as pd 
import plotly.express as px

# st.set_page_config(layout="wide",page_title="Introdução à IA")

#REFERENCIAS 
def ia_triad():
    

    #INTRO 

    st.title("Tríade da Inteligência Artificial")
    st.warning(""" A inteligência artificial (IA) moderna pode ser resumida pela frase: sistemas de aprendizado de máquina utilizam poder computacional para executar algoritmos que aprendem com dados.
    A importância da IA se reflete em seu uso cotidiano por assistentes virtuais como Alexa e Siri, nas inovações científicas, nas dinâmicas econômicas globais e na segurança nacional, onde traz tanto benefícios quanto desafios, como a transparência e o viés. 
    Para que formuladores de políticas possam lidar efetivamente com a IA, é crucial que entendam seus fundamentos e limitações, especialmente no contexto do aprendizado profundo, que se distingue dos sistemas especialistas anteriores. 
    A tríade da IA — dados, algoritmos e poder computacional — é essencial para alcançar resultados significativos e precisa ser compreendida em profundidade pelos responsáveis pela formulação de políticas.
    """)
        
    st.caption(""" O conteúdo dessa página altamente é baseado no relatório 
                        [*The AI Triad and What It Means for National Security Strategy*](https://cset.georgetown.edu/wp-content/uploads/CSET-AI-Triad-Report.pdf)
                        e foi traduzido e resumido utilizando CHAT-GPT.""")


    #SESSAO 

    st.title("Algoritmos")
    col1, col2 = st.columns(2)


    col1.write("""
    Um algoritmo é uma sequência de instruções para processar informações e resolver problemas. Em matemática, por exemplo, o algoritmo PEMDAS (Parênteses, Expoentes, Multiplicação/Divisão, e Adição/Subtração) define a ordem das operações, e em programação, algoritmos orientam computadores a executar tarefas específicas, incluindo lógicas condicionais como “se isso, então aquilo”. Historicamente, sistemas de IA eram projetados com instruções diretas, como o programa DeepBlue, que usou diretrizes de mestres de xadrez para vencer Kasparov. 

    O aprendizado de máquina (ML) difere ao não depender de instruções explícitas, mas de dados, usando redes neurais para identificar padrões. Assim, o ML consegue “aprender” a ordem de operações (como PEMDAS) analisando dados e extraindo regras. Esse tipo de aprendizado não só revela padrões como resolve problemas complexos sem definições precisas, mas traz limitações, como a dificuldade em explicar o processo de decisão.

    Existem três principais abordagens de ML: aprendizado supervisionado, não supervisionado e por reforço. No aprendizado supervisionado, o algoritmo aprende com dados rotulados para fazer previsões em novos contextos, como prever preços de carros com base em características prévias. No não supervisionado, o algoritmo analisa dados sem respostas pré-definidas, segmentando, por exemplo, grupos de consumidores para marketing. Já no aprendizado por reforço, o sistema interage com um ambiente e se ajusta para maximizar recompensas, sendo útil para cenários estratégicos como o jogo Go, onde o programa AlphaZero da DeepMind superou a habilidade humana. 

    O aprendizado por reforço também é aplicado em robótica e veículos autônomos, essencial em contextos como segurança nacional, onde decisões rápidas e complexas em ambientes incertos são necessárias.
    """)

    col2.write("### Exemplos")
    col2.write("""
    **Algoritmo**
    1. Uma receita de bolo. Ela lista passos claros, como misturar ingredientes, assar a massa e decorar, assim como um algoritmo fornece instruções para resolver um problema.

    2. PEMDAS: Na expressão 7 + 5 × (1 + 3), o algoritmo PEMDAS orienta a resolver primeiro o que está dentro dos parênteses (1 + 3 = 4), depois multiplicar (5 × 4 = 20) e, por último, adicionar (7 + 20 = 27).

    **Aprendizado Supervisionado**
    Um algoritmo que aprende a reconhecer fotos de gatos. É treinado com imagens rotuladas como "gato" ou "não gato" e, após o treinamento, consegue identificar gatos em novas imagens.

    **Aprendizado Não Supervisionado**
    Um algoritmo que analisa dados de compras em um supermercado. Ele pode agrupar clientes com base em seus hábitos de compra, mesmo sem saber previamente quem são esses grupos, como "clientes que compram produtos orgânicos" ou "clientes que compram frequentemente lanches".

    **Aprendizado por Reforço**
    Um robô que aprende a jogar um jogo. Ele recebe pontos por movimentos que levam à vitória e perde pontos por movimentos que resultam em derrota. Com o tempo, o robô aprende a maximizar seus pontos, se tornando melhor no jogo.
            """)

    st.divider() ###########


    st.title("Dados")
    col1, col2 = st.columns(2)

    col1.write(
        """  
    A frase "dado é o novo petróleo" se tornou um clichê, destacando a importância dos dados em sistemas de aprendizado de máquina, especialmente no aprendizado supervisionado. Dados são cruciais para reconhecer padrões; sem eles, a eficácia dos algoritmos diminui. Um estudo de 2001 indicou que a quantidade de dados de treinamento é mais importante do que o algoritmo em si.

    A eficácia do aprendizado de máquina depende da quantidade e representatividade dos dados. Por exemplo, um pequeno conjunto de vendas de carros pode não incluir marcas de luxo, resultando em previsões falhas para esses veículos. Assim, conjuntos de dados maiores tendem a capturar melhor a realidade.

    A coleta de dados apresenta desafios, e empresas como Facebook, Google e Amazon se destacam por terem acesso a grandes quantidades de dados do consumidor. Após a coleta, os dados precisam ser organizados e armazenados, enfrentando obstáculos legais, especialmente relacionados à privacidade.

    Além da quantidade, a relevância dos dados para o problema é crucial. Dados irrelevantes, como informações sobre vendas de bicicletas para prever preços de carros, são de pouco valor. Sistemas de aprendizado de máquina precisam de dados específicos e relevantes para funcionar adequadamente.

    A precisão dos dados de treinamento também é importante. Dados tendenciosos podem levar a decisões injustas, como demonstrado por um sistema da Amazon que discriminava mulheres devido ao viés nos dados de contratação. Esses sistemas podem apresentar resultados tendenciosos como se fossem imparciais, o que pode levar a consequências indesejadas, como discriminação em análises de segurança.
    """
    )

    df = pd.read_csv("data/ai-performance-knowledge-tests-vs-dataset-size.csv")

    fig = px.scatter(
        df,
        x="Training dataset size",  # Tamanho do conjunto de dados de treinamento
        y="MMLU avg",               # Média do MMLU
        text="Entity",              # Entidade (modelo de IA)
        title="Desempenho da IA vs. Tamanho do Conjunto de Dados",  # Título do gráfico
        labels={
            "Training dataset size": "Tamanho do Conjunto de Dados de Treinamento (em bilhões)",  # Rótulo do eixo x
            "MMLU avg": "Pontuação Média do MMLU*",  # Rótulo do eixo y
        },
    )


    # Add markers and improve layout
    fig.update_traces(textposition="top center")
    fig.update_layout(xaxis_type="log")  # Use logarithmic scale for better visualization of size differences

    # Display the plot in Streamlit
    col2.plotly_chart(fig)
    col2.caption("Fonte: [Our world in data](https://ourworldindata.org/grapher/ai-performance-knowledge-tests-vs-dataset-size)")

    # with col2.expander("*MMLU"):
    col2.info("*O benchmark de Compreensão de Linguagem Multitarefa Maciça (MMLU) é um questionário de múltipla escolha que avalia a compreensão de sistemas de IA em diversos tópicos, com 57 seções específicas. O teste contém 15.908 perguntas, com pelo menos 100 questões sobre cada assunto, que variam em dificuldade, desde o nível do ensino fundamental até questões desafiadoras para profissionais. As pontuações dos humanos dependem do nível de especialização: não especialistas costumam ter uma taxa de acerto de cerca de 34,5%, enquanto especialistas, como médicos, podem alcançar até 89,8%.")


    st.divider() ######


    st.title("Poder Computacional")
    col1, col2 = st.columns(2)

    col1.markdown("""
    Atualmente, computadores se tornaram mercadorias comuns, com a maioria dos usuários sem conhecimento sobre os chips que utilizam. No entanto, ignorar o poder de computação é um erro grave no campo da IA, já que ele tem sido fundamental para o progresso nesta área. Rich Sutton, um dos fundadores da IA moderna, destacou que o poder computacional reduz o papel humano na construção de sistemas de IA, permitindo que eles aprendam por conta própria. 

    Evidências mostram que o *compute* (poder computacional) está fortemente correlacionado aos avanços em IA. Um [estudo da OpenAI](https://openai.com/index/ai-and-compute/) revelou que, entre 2012 e 2018, a quantidade de *compute* aplicada ao treinamento de projetos de IA aumentou em um fator de 300.000. Essa potência computacional tem possibilitado descobertas significativas e, em alguns casos, a falta de *compute* poderia atrasar projetos em anos. 

    Três fatores principais impulsionaram o aumento do *compute*: a Lei de Moore*, que prevê o dobro do poder computacional a cada 24 meses; a paralelização na computação, que permite que muitos chips trabalhem simultaneamente; e a eficiência de chips especializados em aprendizado de máquina. Apesar dos avanços, os custos de produção de novos chips aumentam, tornando o acesso ao *compute* um desafio para pesquisadores e formuladores de políticas de segurança nacional.
            """)

    col2.image("data/1000x-AI-inferrence-gain-in-10-years-scaled.jpg",
            caption='Em uma palestra recente no Hot Chips, o cientista-chefe da NVIDIA, Bill Dally, descreveu como o desempenho de uma única GPU na inferência de IA se expandiu 1.000 vezes na última década.')

    col2.markdown('Fonte: [blog da NVIDIA](https://blog.nvidia.com.br/blog/por-que-as-gpus-sao-ideais-para-ia/)')
    
    col2.info("Lei de Moore: o CEO e cofundador da Intel, Gordon Moore, sugeriu que o poder computacional dobraria a cada 24 meses como resultado de melhorias na engenharia dos processadores.")



