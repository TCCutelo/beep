# BEEP

## 1. Project description

BEEP is a simple Python project for playing sounds on Windows with `winsound`.

This project is useful for practicing:
- code organization across files
- Object-Oriented Programming
- abstract classes and polymorphism
- command-line execution with Typer

The application flow is simple:
1. `main.py` receives the sound name.
2. It creates the view and the controller.
3. It selects the correct sound class.
4. It plays the selected sound.

## 2. Project structure

```text
Beep/
|-- main.py
|-- sound_controller.py
|-- console_view.py
|-- requirements.txt
|-- model/
|   |-- sound_base.py
|   |-- beep_sound.py
|   |-- hino_sound.py
|   |-- ode_sound.py
|   |-- modem_sound.py
|   `-- phone_sound.py
```

Main files:
- `main.py`: application entry point
- `sound_controller.py`: coordinates execution
- `console_view.py`: prints messages to the console
- `model/sound_base.py`: abstract base class for sounds
- `model/*.py`: concrete sound implementations
- `requirements.txt`: project dependencies

## 3. Requirements

- Windows
- Python 3.x
- `typer==0.21.1`

> Note: this project uses `winsound`, so it is Windows-only.

## 4. Quick start

```bat
py -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
py main.py beep
```

## 5. Create virtual environment

Create a virtual environment named `.venv` in the project folder:

```bat
py -m venv .venv
```

Activate the virtual environment:

```bat
.\.venv\Scripts\Activate
```

Check that the virtual environment is active:

```bat
where python
```

If everything is correct, you should see a path similar to:

```bat
...\Beep\.venv\Scripts\python.exe
```

To recreate the environment from `requirements.txt`, run:

```bat
py -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
```

To deactivate the virtual environment:

```bat
deactivate
```

## 6. Install dependencies

With the virtual environment active, install the project dependencies:

```bat
pip install -r requirements.txt
```

## 7. Run the project

The CLI uses Typer in `main.py`.

`sound_name` is an optional positional argument.
If no argument is provided, the program uses `beep` by default.

Run with the default sound:

```bat
py main.py
```

Run with a specific sound:

```bat
py main.py <som>
```

Real examples from this project:

```bat
py main.py
py main.py beep
py main.py hino
py main.py ode
py main.py modem
py main.py phone
```

Example output:

```bat
(.venv) ...\Beep> py main.py beep
Hello beep
A tocar som...
```

## 8. Available sounds

Confirmed in the current code:
- `beep`
- `hino`
- `ode`
- `modem`
- `phone`

If an invalid sound is used, `main.py` raises an error with the valid options.

## 9. Common errors

### `ModuleNotFoundError: No module named 'typer'`

Install the dependencies:

```bat
pip install -r requirements.txt
```

### `python` or `py` is not recognized

Check the Python installation:

```bat
py --version
```

### The virtual environment is not working

Recreate it:

```bat
py -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
```

### Error with `winsound`

This project must be run on Windows.
