# BEEP

## Como executar rapidamente

```bat
py -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
py main.py beep
```

Projeto simples em Python para reproduzir sons no Windows com `winsound`.

Este projeto serve para praticar:
- organizacao de codigo por ficheiros
- Programacao Orientada a Objetos
- classes abstratas e polimorfismo
- execucao de programas pela linha de comandos

## O que faz

A aplicacao permite tocar diferentes sons:
- `beep`
- `hino`
- `ode`
- `modem`
- `phone`

O fluxo e simples:
1. `main.py` recebe o nome do som
2. cria a view e o controller
3. escolhe a classe de som correta
4. manda tocar o som

## Estrutura do projeto

```text
Beep/
|-- main.py
|-- sound_controller.py
|-- console_view.py
|-- requirements.txt
|-- criar_amb_virtual.md
|-- model/
|   |-- sound_base.py
|   |-- beep_sound.py
|   |-- hino_sound.py
|   |-- ode_sound.py
|   |-- modem_sound.py
|   `-- phone_sound.py
```

### Ficheiros principais

- `main.py`: ponto de entrada da aplicacao
- `sound_controller.py`: coordena a execucao
- `console_view.py`: mostra mensagens na consola
- `model/sound_base.py`: classe base abstrata para os sons
- `model/*.py`: implementacoes concretas dos sons
- `requirements.txt`: dependencias do projeto

## Requisitos

- Windows
- Python 3.x
- `typer==0.21.1`

> Nota: o projeto usa `winsound`, por isso e especifico de Windows.

## Criar ambiente virtual no Windows

Na pasta do projeto:

```bat
py -m venv .venv
```

Ativar o ambiente virtual:

```bat
.\.venv\Scripts\Activate
```

Confirmar que esta ativo:

```bat
where python
```

Se estiver correto, devera aparecer um caminho semelhante a:

```bat
C:\Users\Utilizador\TesteSoPython\Beep\.venv\Scripts\python.exe
```

## Instalar dependencias

Com o ambiente virtual ativo:

```bat
pip install -r requirements.txt
```

## Executar o projeto

Executar com o som por defeito:

```bat
py main.py
```

Executar um som especifico:

```bat
py main.py <som>
```

Sons confirmados no codigo:
- `beep`
- `hino`
- `ode`
- `modem`
- `phone`

## Exemplos de comandos

```bat
py main.py
py main.py beep
py main.py hino
py main.py ode
py main.py modem
py main.py phone
```

Exemplo de execucao:

```bat
(.venv) C:\Users\Utilizador\TesteSoPython\Beep> py main.py beep
Hello beep
A tocar som...
```

## Typer

O projeto usa `Typer` em `main.py`, atraves de `typer.run(main)`.

O parametro `sound_name` e um argumento posicional opcional.
Se nenhum som for indicado, o programa usa `beep` por defeito.

Exemplos validos:

```bat
py main.py
py main.py <som>
py main.py ode
py main.py phone
```

O comando abaixo e **provavel**, mas nao foi confirmado por execucao real neste ambiente:

```bat
py main.py --help
```

## Erros comuns

### `ModuleNotFoundError: No module named 'typer'`
Instalar as dependencias:

```bat
pip install -r requirements.txt
```

### `python` ou `py` nao e reconhecido
Confirmar a instalacao do Python:

```bat
py --version
```

### O ambiente virtual nao funciona
Recriar o ambiente virtual:

```bat
py -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
```

### Erro com `winsound`
O projeto deve ser executado em Windows.

---

Projeto indicado para iniciantes que querem praticar Python, POO e uma pequena aplicacao de consola.
