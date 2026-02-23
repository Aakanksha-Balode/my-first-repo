# step 1 - importing the required library
from spellchecker import SpellChecker


# setp 2 - creating the app class
class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

        def correct_text(self, text):
            words = text.split() # hello world
            corrected_words = []

            for word in words:
                corrected_word = self.spell.correction(word)
                if corrected_word != word.lower():
                    print(f'Correcting "{word}" to "{corrected_word}"')
                    corrected_word.append(corrected_word)

            return ' '.join(corrected_word)
        def run(self):
            print("\n ---Spell Checker---")

            while True:
                text = input('Enter text to check (or type "exit" to quit):')

                if text.lower() == 'exit':
                    print('Closing the program....')
                    break

                corrected_text = self.correct_text(text)
                print(f'Corrected Text : {corrected_text}')


if __name__ == " __main__":
    SpellCheckerApp().run()
