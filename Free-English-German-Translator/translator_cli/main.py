import sys
import os

# Add the project root to sys.path so sibling packages can be found
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from translation_library import Translator

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <text to translate>")
        return

    text_to_translate = " ".join(sys.argv[1:])
    translator = Translator()
    try:
        translated = translator.translate(text_to_translate)
        print(f"\nOriginal Text: {text_to_translate}")
        print(f"Translated Text: {translated}")
        print(f"API Used: {translator.last_used_api}\n")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
