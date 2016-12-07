# Configurando seu ambiente

---
## Conteúdo
- [Configurações iniciais](#configurações-iniciais)
  - [Variáveis de Ambiente](#variáveis-de-ambiente)
  - [Instalação](#instalação)
    - [Ambiente virtual Python](#ambiente-virtual-python)
      - [virtualenv](#virtualenv)
      - [virtualenvwrapper](#virtualenvwrapper)
    - [Sem Ambiente virtual](Sem-Ambiente-virtual)
- [Próximos passos](#próximos-passos)

---

## Configurações iniciais

### Variáveis de Ambiente
Para o script funcionar corretamente é necessário criar duas variáveis de
ambiente, elas são:

- `DB_USER`: usuário
- `DB_PASSWORD`: senha

essas duas variáveis irão ser utilizadas para estabelecer a conexão com o banco. Você pode ler mais sobre variáveis de ambiente [aqui][2].

### Instalação
É recomendável o uso de ambientes virtuais, porém você não precisa necessariamente usá-los para rodar os seus scripts. O script `data_colector.py` possui compatibilidade testada com [Python 3.4.3][3]. Para instalar os pacotes
necessários para rodar o script você precisa ter o gerenciador de pacotes Python `pip` instalado. Você pode encontrar informações sobre como [instalar o pip aqui][4].

#### Ambiente virtual Python
Caso queira, você pode instalar o [virtualenvwrapper][5] ou o [virtualenv][6], ambos são ferramentas que dão suporte ao controle de ambientes virtuais Python.

##### virtualenv
1) Crie um ambiente com Python 3

`virtualenv --python=/usr/bin/python3 myenv`

2) Ative o ambiente virtual

`source myenv/bin/activate`

3) Rode o script de instalação das dependências

`pip install -r colector_requirements.txt`

###### *Importante: lembre que o caminho para instalação do Python 3 pode ser diferente na sua máquina*


##### virtualenvwrapper
1) Crie um ambiente com Python 3

`mkvirtualenv --python=/usr/bin/python3 myenv`

2) Ative o ambiente virtual

`workon myenv`

3) Rode o script de instalação das dependências

`pip install -r colector_requirements.txt`

###### *Importante: lembre que o caminho para instalação do Python 3 pode ser diferente na sua máquina*


#### Sem Ambiente virtual
Instale os pacotes listados em **colector_requirements.txt**. Você pode fazer isso usando:

`sudo pip install -r colector_requirements.txt`

## Próximos passos
Armazenar seus dados localmente.

[1]: dcm.ffclrp.usp.br/comptext
[2]: https://www.vivaolinux.com.br/artigo/Trabalhando-com-shell-e-variaveis-de-ambiente?pagina=2
[3]: https://www.python.org/downloads/release/python-343/
[4]: https://pip.pypa.io/en/stable/installing/
[5]: https://virtualenvwrapper.readthedocs.io/
[6]: https://virtualenv.pypa.io/
