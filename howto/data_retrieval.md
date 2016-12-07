# Script para coletar tweets no Banco de Dados

Uma vez que coletados os tweets ficam armazenados em um banco de dados no
servidor do [LSCC][1]. Então é necessário buscar esses tweets de interesse para
trabalhar com eles localmente. Caso você já tenha seus dados localmente você não
precisa rodar esse script.

---
## Conteúdo
- [Como usar](#como-usar)
- [Resultados da execução do script](#resultados-da-execução-do-script)
- [Entenda o código](#entenda-o-código)


---

## Como usar
Depois de configurar sua máquina criando as variáveis de ambiente necessárias e também instalando as dependencias, abra o terminal e vá para o diretório no qual se encontra o script e digite:

```
$ python -c "from jessie import data_retrieval as dr; dr.demo(table='saude', term='dengue', limit=1000)"
INFO Connecting to database...
INFO Executing SQL command...
INFO Fetching and writing data...
INFO File: dengue_tweets_json
INFO File: sample_dengue_tweets_json
INFO Closing conection...
```

Isso seria o mesmo que abrir o console python, importar o módulo Jessie e executar
o método demo:

```
$ python
>>> from jessie import data_retrieval as dr
>>> dr.data_retrieval(table='saude', term='dengue', limit=1000)
INFO Connecting to database...
INFO Executing SQL command...
INFO Fetching and writing data...
INFO File: dengue_tweets_json
INFO File: sample_dengue_tweets_json
INFO Closing conection...
```

Você pode dessa forma indicar o nome da tabela usando o argumento `table`, o termo que está procurando no texto do tweet usando o argumento `term` e e quantos tweets dessa tabela você quer recuperar usando o argumento `limit`.


###### *Lembrete: se você possuir mais de uma versão do Python instalada na sua máquina, e se o Python na versão 3 não for a sua versão default, os comandos acima precisam ser rodados utilizando `python3`no lugar de `python`*

## Resultados da execução do script
Executar o script, ou seja, rodar o comando da seção [Como usar](#como-usar), irá gerar dois arquivos no diretório atual:

1) `sample_dengue_tweets_json`: *nesse arquivo você encontra os 50 primeiros tweets da tabela que você passou como argumento para o script.*

2) `dengue_tweets_json`: *nesse arquivo você tem a quantidade de tweets da tabela que você passou com o argumento `limit` para o para o método `data_retrieval()`.*

## Entenda o código

Para entender o códgio do [data_retrieval.py](jessie/data_retrieval.py) vá para
o markdown [endentendo data retrieval](entendendo/endentendo_data_retrieval.md)

[1]: dcm.ffclrp.usp.br/comptext

