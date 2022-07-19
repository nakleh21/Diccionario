import json
from difflib import get_close_matches

data = json.load(open("data.json"))
word = input('Ingresa la palabra: ')

class Dicc:
  def __init__(self, name):
    self.name = name

  def search(self):
      def getMeaning(w):
          w = w.lower()
          if w in data:
              return data[w]
          elif len(get_close_matches(w, data.keys())) > 0:
              close_match = get_close_matches(w, data.keys())[0]
              print("Querias decir %s ?  S/N: " % close_match)
              choice = input()
              choice = choice.lower()
              if choice == 's':
                  return data[close_match]
              elif choice == 'n':
                  return "No existe."
              else:
                  return "No entiendo lo que dices humano..."
          else:
              return "La palabra no existe en mis registros, intenta de nuevo"

      meaning = getMeaning(word)

      if type(meaning) == list:
          for item in meaning:
              print(item)
      else:
          print(meaning)

p1=Dicc('dicc')
p1.search()