# Jessie, a case of study

Jessie was developed as a tool to help students and data analists from Brasil that want to
process data from [Twitter](https://twitter.com/). It is meant to work as a
step by step guide to the use of [NLKT](http://nltk.org/) to tag tweet text.

In this source repository you will find a guideline in portuguese (I intend to add
English translations later) to the steps I used in my course final project.


## Identificação de entidades mencionadas para análise de sentimentos em microblogs
---

Discente: Jessica Caroline Alves Nunes Temporal
Número USP: 7547611
jessicatemporal@usp.br

Orientador: Evandro Eduardo Seron Ruiz
evandro@usp.br

Co-Orientador: Mateus Tarcinalli Machado
mateusmachado@usp.br

---

### Tese de Conclusão de Curso

O meu TCC pode ser encontrado [aqui](https://drive.google.com/open?id=0BxeG4Yg1C3hHOXZ1T1JSazY1VGs).

E os slides da minha defesa estarão [aqui](http://jtemporal.github.io/jessie/).

### Pipeline de processamento

A pipeline segue os seguintes passos:

 - Preparar o seu ambiente
 - Buscar dados no servidor da faculdade e armazená-los localment
 - Pré-processar esses dados
 - POS-Tagging
 - Anotar as frequências de termos candidatos usando o algoritmo FREQ Baseline
 - Anotar as frequências de termos candidatos usando o algoritmo de Hu e Liu

#### Como Usar

Cada script dentro no módulo Jessie, pode ser importado a partir do console
Python. Cada script possui dois arquivos markdown. O primeiro deles trás
as informações sobre como aquele script funciona e qual o resultado esperado
ao fim dele. E o segundo, trás informações sobre como funciona o código escrito
naquele script. Assim você poderá também entender o que cada função e cada objeto
fazem.

Como mencionado anteriormente, o primeiro passo é preparar o seu ambiente. Vá para
o [markdown configuration](https://github.com/jtemporal/jessie/blob/master/configuration.md),
e siga os passos descritos lá =)

### Dúvidas, sugestões, discussões e contribuições

O canal oficial para issues, dúvidas e sugestões são o sistema de issues aqui
desta plataforma.

#### Contribuições
Caso queira contribuir, faça um fork do projeto e depois um pull request.
Se tiver dúvidas quanto à isso, pode abrir uma issue ficarei feliz em ajudar =)

Eventualmente o projeto será integrado com uma ferramente de CI e um dos
checkpoints será o falke8, então fique atento a isso para agilizar o processo
de aceitar PRs.
