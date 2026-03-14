## Criar um novo ambiente virtual

Cria um ambiente virtual chamado `.venv` na pasta do projeto:

```bat
py -m venv .venv
```


## Ativar o ambiente virtual
```bat
.\.venv\Scripts\Activate
```

## Confirmar que o ambiente está ativo

```bat
where python
```

## Guardar dependências com o ambiente ativo
```bat
pip freeze > requirements.txt
```py

## Recriar o ambiente a partir de requirements.txt

Executa os seguintes comandos **pela ordem indicada**:

```bat
py -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
```
O requirements.txt deve listar apenas dependências DIRETAS do projeto
pip freeze é bruto

## Desativar o ambiente virtual

```bat
deactivate
```
O prefixo (.venv) desaparecerá do terminal


## Instalar novos pacotes

com o ambiente ativo

```bat
pip install typer
```

## Instalar versões específicas

Exemplo

```bat
pip install typer ==0.21.1
```

## Confirmar que o pacote foi instalado
```bat
pip show nome_do_pacote

ou

pip list
```

## Atualizar um pacote especifico

```bat
pip install --upgrade typer
```

## Atualizar tudo
```bat
pip list --outdated
pip install --upgrade nome_do_pacote
```

## Remover pacotes do ambiente
```bat
pip uninstall nome_do_pacote
```

e depois fazer

```bat
pip freeze > requirements.txt
```

