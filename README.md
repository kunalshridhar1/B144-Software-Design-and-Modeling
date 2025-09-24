# Free English-German Translator CLI

A command-line translator that translates text from English to German using three free translation APIs with automatic fallback:

- **Google Translator**
- **LibreTranslate**
- **MyMemory Translator**

No API keys are required.


## Features

- CLI-based, easy to use
- Automatic fallback between multiple APIs
- Displays the translation along with which API was used
- Reusable translation library (`translation_library`)



## Installation

1. Clone or download the project.
2. Navigate to the project root in terminal/PowerShell.
3. Install dependencies:

```bash
pip install -r requirements.txt
```
## Usage
```bash
python translator_cli\main.py "Hello world"
```
## Example Output
```bash
Original Text: Hello world
Translated Text: Hallo Welt
API Used: Google Translator
```
## Project Structure
```bash
Free-English-German-Translator/
├── translator_cli/
│   ├── __init__.py
│   └── main.py
├── translation_library/
│   ├── __init__.py
│   └── translation_library.py
├── requirements.txt
├── README.md
└── LICENSE
```
# License

    This project is licensed under the MIT License.


👨‍💻 Author
Kunal Shridhar
📧 shridharkunal2005@gmail.com
🔗 GitHub: https://github.com/kunalshridhar1





