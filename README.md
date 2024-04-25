# Desafio Prático: API REST para Acesso a Dados de Saúde 👨‍⚕️

Desenvolvi uma API REST em Python utilizando o framework Flask, que retorna os dados dos pacientes de forma organizada e fácil.

## Rodando localmente :

1. Faça o clone da do repósitorio e acesse a pasta clonada.

```shell
git clone https://github.com/brenofigueiredoo/desafio_painel_esus.git

cd desafio_painel_esus
```

2. Instale o ambiente virtual.

```
python -m venv venv
```

3. Entre no ambiente virtual.

```
.\venv\Scripts\activate
```

4. Instale todas as dependências.

```
pip install -r requirements.txt
```

5. Crie e configure o arquivo .env

```
FLASK_DEBUG=True
FLASK_APP=server.py
```

6. Rode o servidor.

```
flask run
```

ou

```
python .\server.py
```

Para acessar a aplicação utilize: [localhost:8001](http://localhost:8001)
&nbsp;

## Ferramentas utilizadas 🛠

- Python <img align="center" alt="python" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg">
- Flask <img align="center" alt="flask" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original-wordmark.svg">
- Insomnia <img align="center" alt="insomnia" height="30" width="40" src="https://www.svgrepo.com/show/353904/insomnia.svg">
- GitHub <img align="center" alt="github" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg">
- VsCode <img align="center" alt="vscode" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg">

&nbsp;

## Contribuintes ✨

| Função    | Membro                                                               |
| --------- | -------------------------------------------------------------------- |
| Developer | [Breno S. Figueiredo](https://www.linkedin.com/in/brenosfigueiredo/) |

&nbsp;

## Documentação 📚

#### 1 - Listar atendimentos

- Endpoint: `GET /api/v1/atendimentos`

Retorna os atendimentos de acordo com os filtros passados na query.
<br>
É possível adicionar um ou mais filtros na query da requisição com os seguintes campos:

- data_atendimento (str): Formato 'YYYY-mm-dd'.
- condicao_saude (str): hipertensao|diabetes|ferida vascular|dengue|tuberculose.
- unidade (str).

Exemplo de como ficaria a url da requisição:

```
http://localhost:8001/api/v1/atendimentos?data_atendimento=2024-01-01&condicao_saude=diabetes&unidade=saude
```
