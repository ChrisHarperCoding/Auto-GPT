## USER
Please fix - zsh: command not found: mkvirtualenv

## ASSISTANT
It looks like you're trying to use `mkvirtualenv` command in zsh shell, but it's not recognized. This is probably because virtualenvwrapper is not installed or not properly configured in your environment. To fix this issue, follow these steps:

1. Install `virtualenv` and `virtualenvwrapper` if you haven't already:

```sh
pip install virtualenv virtualenvwrapper
```

2. Add the following lines to your zsh configuration file (`.zshrc`). You can find this file in your home directory. If it doesn't exist, create one:

```sh
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=$(which python3)  # Set the Python interpreter you want to use
source $(which virtualenvwrapper.sh)
```

Replace `$(which python3)` with the path to your desired Python interpreter if it's not in your PATH.

3. Restart your zsh shell or run the following command to apply the changes:

```sh
source ~/.zshrc
```

Now, you should be able to use `mkvirtualenv` and other virtualenvwrapper commands in your zsh shell. To create a new virtual environment, run:

```sh
mkvirtualenv my_virtual_env_name
```