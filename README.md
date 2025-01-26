# Transfermarkt Scraping API

Esta é uma API desenvolvida em Django que realiza o scraping de dados do site [Transfermarkt](https://www.transfermarkt.com) para obter informações sobre os jogadores dos times que estão na Série A do Campeonato Brasileiro de Futebol. A API fornece o elenco completo de cada time, incluindo o nome dos jogadores e seus respectivos números de camisa.

## Funcionalidades

- Realiza o scraping dos dados diretamente do site Transfermarkt.
- Retorna o elenco completo de cada time da Série A do Campeonato Brasileiro.
- Para cada jogador, é fornecido:
  - Nome.
  - Número da camisa.

## Tecnologias Utilizadas

- **Django**: Framework principal para o desenvolvimento da API.
- **BeautifulSoup**: Biblioteca utilizada para realizar o scraping dos dados.
- **Requests**: Biblioteca para realizar requisições HTTP.
- **Poetry**: Gerenciador de dependências e ambiente virtual.

## Requisitos

- Python 3.12.0

## Instalação e Configuração

Siga os passos abaixo para clonar e configurar o projeto em sua máquina local:

1. Clone o repositório:

```bash
https://github.com/felipeandersonr/campinho.git
cd campinho
```

2. Instale o Poetry, caso ainda não tenha:

```bash
pip install poetry
```

3. Instale as dependências do projeto:

```bash
poetry install
```

4. Ative o ambiente virtual gerenciado pelo Poetry:

```bash
poetry shell
```

5. Configure as variáveis de ambiente, como as credenciais ou URLs necessárias para o scraping. Você pode usar um arquivo `.env` para isso:

```
SCRAPING_BASE_URL="https://www.transfermarkt.com/campeonato-brasileiro-serie-a/startseite/wettbewerb/BRA1"
```

6. Rode as migrações do banco de dados:

```bash
python manage.py migrate
```

7. Antes de rodar a aplicação, execute o arquivo responsável pelo scraping inicial dos dados:

```bash
python manage.py runscript transfermarkt_scraping
```

8. Inicie o servidor:

```bash
python manage.py runserver
```

A API estará acessível em `http://127.0.0.1:8000/`.

## Endpoints

### `GET /clubs/`

Retorna a lista de todos os times da Série A do Campeonato Brasileiro.

Exemplo de resposta:

```json
[
{
    "id": 1,
    "name": "Sociedade Esportiva Palmeiras",
    "image": "https://tmssl.akamaized.net//images/wappen/head/1023.png?lm=1411204983",
    "transfermarkt_url": "https://www.transfermarkt.com/se-palmeiras-sao-paulo/startseite/verein/1023/saison_id/2024"
  },
  {
    "id": 2,
    "name": "CR Flamengo",
    "image": "https://tmssl.akamaized.net//images/wappen/head/614.png?lm=1551023331",
    "transfermarkt_url": "https://www.transfermarkt.com/flamengo-rio-de-janeiro/startseite/verein/614/saison_id/2024"
  },
  {
    "id": 3,
    "name": "Sport Club Corinthians Paulista",
    "image": "https://tmssl.akamaized.net//images/wappen/head/199.png?lm=1649430398",
    "transfermarkt_url": "https://www.transfermarkt.com/corinthians-sao-paulo/startseite/verein/199/saison_id/2024"
  },
]
```

### `GET /lineup/{team_id}`/

Retorna o elenco de jogadores de um time específico.

Parâmetros:

- `team_id`: ID do time.

Exemplo de resposta:

```json
[
  {
    "name": "Hugo Souza",
    "shirt_number": "-"
  },
  {
    "name": "Matheus Donelli",
    "shirt_number": "32"
  },
]
```

##
