""" Translator """
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """translator"""
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    """translator"""
    english_text = MyMemoryTranslator(source='en', target='fr').translate(french_text)
    print(english_text)
    return english_text

english_to_french("hello how are you")
french_to_english("bonjour comment allez-vous")
