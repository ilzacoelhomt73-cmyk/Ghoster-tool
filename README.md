# Ghoster-tool

# instalação

# para debian

```bash
sudo apt update -y && sudo apt upgrade -y && sudo apt install -y python3 python3-pip git curl build-essential make libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libncurses-dev xz-utils tk-dev libffi-dev && curl https://pyenv.run | bash && export PYENV_ROOT="$HOME/.pyenv" && export PATH="$PYENV_ROOT/bin:$PATH" && eval "$(pyenv init - bash)" && pyenv install 2.7.18 && pyenv local 2.7.18 && git clone https://github.com/ilzacoelhomt73-cmyk/Ghoster-tool.git && cd Ghoster-tool && python3 -m pip install -r requirements.txt --break-system-packages && python3 ghoster.py
```
# para termux

```bash
pkg update -y && pkg upgrade -y && pkg install python2 python git -y && git clone https://github.com/ilzacoelhomt73-cmyk/Ghoster-tool.git && cd Ghoster-tool && pip install -r requirements.txt && python ghoster.py
```
