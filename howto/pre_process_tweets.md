# Script para pré-processar tweets

Agora que você já tem os seus tweets chegou a hora de fazer o pré-processamento deles.

---
## Conteúdo
- [Como usar](#como-usar)
- [Resultados da execução do script](#resultados-da-execução-do-script)
- [Entenda o código](#entenda-o-código)


---

## Como usar
Abra o terminal e digite o comando abaixo, lembre-se: se você não estiver na raiz do Jessie, é necessário
instalar o Jessie ou clonar o repo para usá-lo.

```
$ python -c "from jessie import pre_process_tweets as pp; pp.pre_process(filename='dengue_tweets_json')"
copiando dengue_tweets_json
replacing links, user names and hashtags
appending stopwords
writing words to file
writing tweets to file
```

Isso seria o mesmo que abrir o console python, importar o módulo Jessie e executar
o método demo:

```
$ python
>>> from jessie import pre_process_tweets as pp
>>> pp.pre_process(filename='zika_tweets_json')
```

O argumento `filename` deve conter o nome do arquivo de tweets que você quer usar. Esse arquivo contém os textos dos tweets e foi gerado utilizando o script [data_retrieval](jessie/data_retrieval.py)


###### *Lembrete: se você possuir mais de uma versão do Python instalada na sua máquina, e se o Python na versão 3 não for a sua versão default, os comandos acima precisam ser rodados utilizando `python3`no lugar de `python`*

## Resultados da execução do script
Executar o script, ou seja, rodar os comandos da seção [Como usar](#como-usar), irá gerar dois arquivos no diretório atual:

1) `tweets_list_dengue_tweets_json.txt`: *nesse arquivo você encontra todos tweets lidos*

2) `words_list_dengue_tweets_json.txt `: *nesse arquivo você encontra uma lista de palavras do tweets lidos, esta lista não contém nem stopwords, nem pontuação, nem tão pouco palavras com menos de quatro caracteres*

## Entenda o código

Para entender o códgio do [pre_process_tweets.py](jessie/pre_process_tweets.py) vá para
o markdown [endentendo pre process tweets](entendendo/endentendo_pre_process_tweets.md)

