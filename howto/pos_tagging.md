# Script para fazer o POS-tagging

Depois de pré-processar os tweets com o script de [pré-processamento](jtemporal/pre_process_tweets), vamos realizar o taggeamento de termos.

---
## Conteúdo
- [Como usar](#como-usar)
- [Resultados da execução do script](#resultados-da-execução-do-script)
- [Entenda o código](#entenda-o-código)

---

## Como usar
Caso seu terminal ainda não esteja aberto, abra o terminal e digite:

```
$ python -c "from jessie import pos_tagging as pt; pt.pos_tagging('tweets_list_dengue_tweets_json.txt')"
INFO reading tagged sentences
INFO simplifying tags
INFO training floresta taggers without backoff
INFO this may take a while...

INFO <DefaultTagger: tag=n>
accuracy score: 0.19987139015550098

INFO <UnigramTagger: size=26262>
accuracy score: 0.8632058926692389

INFO <BigramTagger: size=46481>
accuracy score: 0.19688998012393313

INFO <TrigramTagger: size=70355>
accuracy score: 0.11680112241318835

INFO training macmorpho taggers without backoff
INFO this may take a while...

INFO <DefaultTagger: tag=N>
accuracy score: 0.19553053448216676

INFO <UnigramTagger: size=63400>
accuracy score: 0.8063317428169304

INFO <BigramTagger: size=141774>
accuracy score: 0.20839483711510076

INFO <TrigramTagger: size=254874>
accuracy score: 0.11790704060965981

INFO training floresta taggers with backoff
INFO this may take a while...

INFO <DefaultTagger: tag=n>
accuracy score: 0.19987139015550098

INFO <UnigramTagger: size=18846>
accuracy score: 0.8858295334970185

INFO <BigramTagger: size=1880>
accuracy score: 0.8995089442300948

INFO <TrigramTagger: size=1582>
accuracy score: 0.8988658950075997

INFO saving floresta_bigram_tagger_backoff.pkl...

INFO training macmorpho taggers with backoff
INFO this may take a while...

INFO <DefaultTagger: tag=N>
accuracy score: 0.19553053448216676

INFO <UnigramTagger: size=48315>
accuracy score: 0.8172822766125434

INFO <BigramTagger: size=14309>
accuracy score: 0.8335879303834404

INFO <TrigramTagger: size=14838>
accuracy score: 0.8327211561566716

INFO saving macmorpho_bigram_tagger_backoff.pkl...

INFO 22956 lines were read from tweets_list_dengue_tweets_json.txt
INFO loading taggers...


writing nouns to file...
INFO saving data to file: floresta_nouns_tweets_list_dengue_tweets_json.txt

writing nouns to file...
INFO saving data to file: macmorpho_nouns_tweets_list_dengue_tweets_json.txt
```

Isso seria o mesmo que abrir o console python, importar o módulo Jessie e executar
o método pos_tagging, Note que, se você já possuir pelo menos um pos-tagger salvo no seu diretorio, o resultado impresso na tela será o seguinte:

```
$ python
>>> from jessie import pos_tagging as pt
>>> pt.pos_tagging(filename='tweets_list_dengue_tweets_json.txt')
INFO reading tagged sentences
INFO simplifying tags
INFO training floresta taggers without backoff
INFO this may take a while...

INFO <DefaultTagger: tag=n>
accuracy score: 0.19987139015550098

INFO <UnigramTagger: size=26262>
accuracy score: 0.8632058926692389

INFO <BigramTagger: size=46481>
accuracy score: 0.19688998012393313

INFO <TrigramTagger: size=70355>
accuracy score: 0.11680112241318835

INFO training macmorpho taggers without backoff
INFO this may take a while...

INFO <DefaultTagger: tag=N>
accuracy score: 0.19553053448216676

INFO <UnigramTagger: size=63400>
accuracy score: 0.8063317428169304

INFO <BigramTagger: size=141774>
accuracy score: 0.20839483711510076

INFO <TrigramTagger: size=254874>
accuracy score: 0.11790704060965981

INFO 22956 lines were read from tweets_list_dengue_tweets_json.txt
INFO loading taggers...


writing nouns to file...
INFO saving data to file: floresta_nouns_tweets_list_dengue_tweets_json.txt

writing nouns to file...
INFO saving data to file: macmorpho_nouns_tweets_list_dengue_tweets_json.txt
```

O argumento `filename` indica um dos arquivos que foram gerados pelo script de [pré-processamento](jessie/pre_process_tweets.py]. Esse arquivo contém o texto dos tweets baixados e salvos anteriormente.


###### *Lembrete: se você possuir mais de uma versão do Python instalada na sua máquina, e se o Python na versão 3 não for a sua versão default, os comandos acima precisam ser rodados utilizando `python3`no lugar de `python`*

## Resultados da execução do script
Executar o script, ou seja, rodar o comando da seção [Como usar](#como-usar), irá gerar quatro arquivos no diretório atual:

1) `floresta_nouns_tweets_list_dengue_tweets_json.txt`: *nesse arquivo você encontra todos os substantivos tagueados com os taggers treinados pelo corpus floresta*

2) `macmorpho_nouns_tweets_list_dengue_tweets_json.txt`: *nesse arquivo você encontra todos os substantivos tagueados com os taggers treinados pelo corpus mac morpho*

Esses proximos dois arquivos só são gerados caso ainda não exista nenhum tagger salvo na pasta

3) `floresta_bigram_tagger_backoff.pkl`: *esse arquivo irá conter o tagger com maior acurácia treinado com o corpus floresta, e pode variar de nome, uma vez que o dependendo do corpus utilizado o tagger com maior acurácia pode ser outro*

4) `macmorpho_bigram_tagger_backoff.pkl`: *esse arquivo irá conter o tagger com maior acurácia treinado com o corpus mac morpho, e pode variar de nome, uma vez que o dependendo do corpus utilizado o tagger com maior acurácia pode ser outro*

## Entenda o código

Para entender o códgio do [pos_tagging.py](jessie/pos_tagging.py) vá para
o markdown [endentendo pos tagging](entendendo/endentendo_pos_tagging.md)

