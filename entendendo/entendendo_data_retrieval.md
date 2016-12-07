# Entendendo o data_retrival.py

Vimos como usar esse script no [markdown dele](data_retrieval.md) assim como também
os resultados esperados da sua execução. Agora vamos entender como as partes do
script funcionam.

---
## Conteúdo
- [Importando pacotes](#importando-pacotes)
- [Configuração de log](#configuração-de-log)
- [Recebendo tabela ou view por argumento](#recebendo-tabela-ou-view-por-argumento)
- [Buscando usuário e senha](#buscando-usuário-e-senha)
- [Interagindo com o banco de dados](#interagindo-com-o-banco-de-dados)
  - [Conectando](#conectando)
  - [Executando comandos SQL](#executando-comandos-SQL)
- [Função que salva os tweets em arquivos](#função-que-salva-os-tweets-em-arquivos)

---

### Importando pacotes
```{py}
import sys
from logging import INFO, basicConfig, error, info
from os import environ

import psycopg2
import simplejson as json
from tqdm import tqdm
```

### Configuração de log
O método `basicConfig` faz parte da biblioteca built-in do Python [`logging`][1]. Com esse método formatamos e definimos o nível dos eventos, neste caso o nível escolhido é `INFO`.

```{py}
basicConfig(format='%(levelname)s %(message)s', level=INFO)
```

Com essa configuração acima, o script irá mostrar na tela informações no formato abaixo:

`INFO mensagem de informação`

### Recendo tabela ou view por argumento
Como mostra a seção [Como usar](#como-usar), o script precisa receber o nome da tabela de interesse, ou uma view correspondente. Caso não o faça, você receberá o seguinte erro e o programa sairá:

`ERROR Usage: data_retrieval.py [table/view]`

Isso é alcançado pela definição do try-catch descrito a seguir:
```{py}
try:
    table = sys.argv[1]
except:
    error('Usage: data_retrieval.py [table/view]')
    sys.exit(1)
```

### Buscando usuário e senha
Caso você tenha passado uma tabela como indicado, o script irá continuar a rodar, então ele irá buscar as variáveis com o nome de *usuário* e *senha* que configuramos na seção [Variáveis de Ambiente](configuration.md) que permitem o acesso ao banco de dados.
```{py}
USER = environ.get('DB_USER')
PASSWORD = environ.get('DB_PASSWORD')
if not USER or not PASSWORD:
    error('no USER or PASSWORD for connection found')
    sys.exit(1)
```

Caso não sejam encontradas as variáveis, o programa irá terminar sua execução com o seguinte erro:

`ERROR no USER or PASSWORD for connection found`

### Interagindo com o banco de dados
Todas as interações com o banco de dados são feitas utilizando os métodos do pacote `psycopg2`, desde a conexão com o banco quanto a execução de comandos SQL. Caso queira, você pode ler a [documentação do psycopg2][2] para ter maiores informações sobre o funcionamento do pacote e seus métodos. Alguns métodos estão explicados abaixo.

#### Conectando
O método `connect`, utilizado para estabelecer conexão com o banco de dados, recebe os seguintes argumentos:
- **database**: o nome do banco
- **user**: o usuário de acesso ao banco
- **password**: senha de acesso ao banco
- **host**: endereço de IP da máquina servidora onde o banco está localizado

```{py}
info('Connecting to database...')
conn = psycopg2.connect(database='twitter', user=USER, password=PASSWORD,
                        host='143.107.137.90')
```

#### Executando comandos SQL
Depois de estabelecer a conexão com o banco, precisamos fazer uma consulta SQL para recuperar os tweets da tabela de interesse. Para executar um comando SQL no banco precisamos de um cursor. Um cursor, é um objeto da classe cursor e é criado usando o método `cursor()`. Se quiser aprender mais sobre eles pode conferir a [documentação][3] referente a classe.
Abaixo temos na sequencia:

1) criação do cursor;
2) definição da consulta SQL que busca o conteudo da coluna `json` para tabela passada por argumento;
3) execução do comando SQL definido.

```{py}
cur = conn.cursor()
sql = 'SELECT json FROM {};'.format(table)
info('Executing SQL command...')
cur.execute(sql)
info('Fetching and writing data...')
```

#### Função que salva os tweets em arquivos
```{py}
def fetch_and_save_data_to_file(db_cursor, file_options):
    file_options['samplefile'] = 'sample-' + file_options['filename']
    with open(file_options['filename'], 'w') as mainfile, \
         open(file_options['samplefile'], 'w') as samplefile:
        info('File: %s', file_options['filename'])
        i = 0
        samples = []
        for row in tqdm(db_cursor):
            mainfile.write(json.dumps(row[0], mainfile))
            mainfile.write('\n')
            if i < file_options['opt']:
                i += 1
                samples.append(row[0])

        info('File: %s', file_options['samplefile'])
        for sample in tqdm(samples):
            samplefile.write(json.dumps(sample, samplefile))
            samplefile.write('\n')
    info('Closing conection...')
    cur.close()
    conn.close()

file_opt = {
                'filename':'tweets-json',
                'opt': 50,
           }
fetch_and_save_data_to_file(cur, file_opt)
```

[1]: https://docs.python.org/3.4/library/logging.html
[2]: http://pythonhosted.org/psycopg2/
[3]: (http://initd.org/psycopg/docs/cursor.html#cursor)