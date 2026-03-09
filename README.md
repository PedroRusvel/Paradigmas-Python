# Implementa-o-de-algoritmos-b-sicos-em-paradigmas-diferentes

Dentre os três paradigmas estudados, o Funcional mostrou-se o mais elegante e conciso para o
problema de processamento de folha de pagamento. A natureza do problema — filtrar, transformar e
agregar uma coleção de registros — mapeia-se diretamente nas operações filter, map e reduce,
eliminando a necessidade de variáveis de controle ou estruturas auxiliares. A imutabilidade dos
dados também garante que nenhum registro original seja acidentalmente modificado, tornando o
código mais seguro e fácil de testar. O paradigma Orientado a Objetos torna-se mais vantajoso à
medida que o sistema cresce: se precisarmos adicionar tipos diferentes de funcionários, regras de
bônus específicas por cargo ou integração com banco de dados, a modelagem por classes oferece o
melhor arcabouço de expansão através de herança e polimorfismo. Já o paradigma Imperativo,
embora seja o mais intuitivo para quem está aprendendo a programar — pois replica o raciocínio
humano passo a passo —, apresenta as maiores dificuldades de manutenção em sistemas de maior
escala, pois o estado muda em vários pontos do código, dificultando a localização de bugs. Em
suma, para este problema específico e em escala pequena, o funcional vence em expressividade;
para um sistema real de RH, a abordagem OOP seria a escolha profissional mais sustentável.
