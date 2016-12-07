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
$ python -c "from jessie import freq_baseline as fb; fb.freq_baseline()"
INFO 141897 lines were read from macmorpho_nouns_tweets_list_dengue_tweets_json.txt
INFO replacing accetuation...
INFO saving data to file: aspect_terms_macmorpho_nouns_tweets_list_dengue_tweets_json.txt
INFO 151203 lines were read from floresta_nouns_tweets_list_dengue_tweets_json.txt
INFO replacing accetuation...
INFO saving data to file: aspect_terms_floresta_nouns_tweets_list_dengue_tweets_json.txt

```

Isso seria o mesmo que abrir o console python, importar o módulo Jessie e executar
o método `freq_baseline`. Note que, o `freq_baseline` possui dois parametros opicionais chamados: `wordcloud` e `venn`, ambos são boleanos e são utilizados para gerar arquivos necessários para fazer uma wordcloud e um diagrama de venn respectivamente:

```
$ python
>>> from jessie import freq_baseline as fb
>>> fb.freq_baseline(wordcloud=True, venn=True)
INFO 141897 lines were read from macmorpho_nouns_tweets_list_dengue_tweets_json.txt
INFO replacing accetuation...
INFO saving data to file: aspect_terms_macmorpho_nouns_tweets_list_dengue_tweets_json.txt
INFO saving data to file: venn_macmorpho_nouns_tweets_list_dengue_tweets_json.txt
INFO saving data to file: wordcloud_macmorpho.txt
INFO 151203 lines were read from floresta_nouns_tweets_list_dengue_tweets_json.txt
INFO replacing accetuation...
INFO saving data to file: aspect_terms_floresta_nouns_tweets_list_dengue_tweets_json.txt
INFO saving data to file: venn_floresta_nouns_tweets_list_dengue_tweets_json.txt
INFO saving data to file: wordcloud_floresta.txt
```


###### *Lembrete: se você possuir mais de uma versão do Python instalada na sua máquina, e se o Python na versão 3 não for a sua versão default, os comandos acima precisam ser rodados utilizando `python3`no lugar de `python`*

## Resultados da execução do script
Executar o script, ou seja, rodar o comando da seção [Como usar](#como-usar), irá gerar os seguintes arquivos no diretório atual:

1) `aspect_terms_floresta_nouns_tweets_list_dengue_tweets_json.txt`: *nesse arquivo você encontra todos os substantivos com frequencia maior que 10 e as suas respectivas frequencias*

2) `aspect_terms_macmorpho_nouns_tweets_list_dengue_tweets_json.txt`: *nesse arquivo você encontra todos os substantivos com frequencia maior que 10 e as suas respectivas frequencias*

Esses próximos dois arquivos só são gerados caso você tenha definido o parametro `wordcloud = True`

3) `wordcloud_floresta.txt`: *esse arquivo irá conter todos os substantivos em suas quantidades de repetições para geração de um wordcloud*

4) `wordcloud_macmorpho.txt`: *esse arquivo irá conter todos os substantivos em suas quantidades de repetições para geração de um wordcloud*

Esses próximos dois arquivos só são gerados caso você tenha definido o parametro `venn = True`

3) `venn_floresta_nouns_tweets_list_dengue_tweets_json.txt`: *esse arquivo irá conter todos os substantivos em suas quantidades de repetições para geração de um wordcloud*

4) `venn_macmorpho_nouns_tweets_list_dengue_tweets_json.txt`: *esse arquivo irá conter todos os substantivos em suas quantidades de repetições para geração de um wordcloud*
## Entenda o código

Para entender o códgio do [freq_baseline.py](jessie/freq_baseline.py) vá para
o markdown [endentendo pos tagging](entendendo/endentendo_freq_baseline.md)

