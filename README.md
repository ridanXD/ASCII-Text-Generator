# ASCII Text Generator

Convert your text into stylish ASCII art in the terminal! This project lets you create 3D-style text using `/|\_` characters or standard ASCII fonts, with python file output. Perfect for fun scripts, terminal banners, or adding a retro touch to your projects.

## Features

- Generate ASCII art from any input text.
- Display output in the terminal with optional colors.
- 3D-style effect using `/|\_`.
- Save generated ASCII art into Python files automatically.
- Easy setup with virtual environment.
- Cross-platform: Linux, macOS, Windows (PowerShell or CMD).

## Installation

Clone the repository:

For Linux/MacOS

```bash
git clone https://github.com/your-username/ascii-text-generator.git
cd ascii-text-generator
chmod +x setup.sh
./setup.sh
```
For Windows (PowerShell)
```bash
git clone https://github.com/your-username/ascii-text-generator.git
cd ascii-text-generator
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.\setup.ps1
```

For Termux
```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/your-username/ascii-text-generator.git
cd ascii-text-generator
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python generator.py
```

# If your terminal say ' externally-managed-environment' 
Try
```bash
python -m venv env
source env/bin/activate
```
For Windows:
```bash
python -m venv env
& "env\Scripts\Activate.ps1"
```
