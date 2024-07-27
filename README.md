# Python Bot for Managing Linux Servers

Welcome to the **Python Bot for Managing Linux Servers** project! This bot is designed to streamline and automate various tasks associated with managing Linux servers. Whether you're monitoring system resources, managing services and processes, or performing routine maintenance tasks, this bot has you covered.

## Features

- **System Monitoring**: Keep an eye on CPU usage, memory, and disk space.
- **Power Management**: Remotely power off or reboot your machine.
- **Services and Process Management**: Take control of your systemd services and processes with ease.

## Installation

To get started with the Python Bot, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/RageGen/linux-python-bot
   cd linux-python-bot
2. **Create a virtual environment:**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Also configure the environment variables in /etc/environment:**
   ```bash
   TOKEN="your_token_bot"
   SUDO_PASSWORD="your_password"
5. **Update the array and enter your User id there, which you can get through other bots in Telegram or in any other way convenient for you.**
   ```python
   allowed_user_ids = []
## Usage
To start the bot, simply run:
```bash
python3 run.py
```
## Lisence
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.
