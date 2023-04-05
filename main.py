from greet import greetings
from translate import Translator

translator = Translator(to_lang="pt") #initializing translator
for g in greetings:
    print(translator.translate(g).title())
# title will change the first letters in your list
#to capital letter
#changing the list to portugese on the console