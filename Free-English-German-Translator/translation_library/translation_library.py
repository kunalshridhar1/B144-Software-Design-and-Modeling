from deep_translator import GoogleTranslator, LibreTranslator, MyMemoryTranslator

class Translator:
    """
    English→German CLI Translator using three free APIs with fallback:
    Google Translator, LibreTranslate, MyMemory.
    """
    def __init__(self):
        self.last_used_api = None

    def translate(self, text, target_lang="de"):
        # Try Google Translator
        try:
            result = GoogleTranslator(source='auto', target=target_lang).translate(text)
            self.last_used_api = "Google Translator"
            return result
        except:
            pass

        # Try LibreTranslate
        try:
            result = LibreTranslator(source='auto', target=target_lang).translate(text)
            self.last_used_api = "LibreTranslate"
            return result
        except:
            pass

        # Try MyMemory
        try:
            result = MyMemoryTranslator(source='auto', target=target_lang).translate(text)
            self.last_used_api = "MyMemory"
            return result
        except:
            pass

        raise Exception("All translation APIs failed.")
