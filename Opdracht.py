
import re
import random
import json
import urllib.request


patterns = {
   "Weet je nog (.*)":"Natuurlijk weet ik nog {}.",
   "Ik voel me (.*)":"Waarom voel jij je {}?",
   
}

def get_cat_fact():
  url = 'https://meowfacts.herokuapp.com/'
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())

  single_cat = result["data"]
  single_cat = single_cat[0]

  return single_cat

  print(result)

responses = {
  "Hallo": ["Hoi, hoe gaat het?", "Hallo!"],
  "hallo": ["Hoi, hoe gaat het?", "Hallo!"],
  "Het gaat goed": ["Goed om te horen!", "Geweldig!"],
  "het gaat goed": ["Goed om te horen!", "Geweldig!"],
  "Wat kost een gemiddelde vlucht": ["De gemiddelde vlucht kost €354  "],
  "wat kost een gemiddelde vlucht": ["De gemiddelde vlucht kost €354  "],
  "Wat kost een gemiddelde vlucht?": ["De gemiddelde vlucht kost €354  "],
  "wat kost een gemiddelde vlucht?": ["De gemiddelde vlucht kost €354  "],
  "Wanneer gaan de meesten vluchten": ["De meesten vluchten gaan tussen 15:00 en 20:00."],
  "wanneer gaan de meesten vluchten": ["De meesten vluchten gaan tussen 15:00 en 20:00."],
  "Wanneer gaan de meesten vluchten?": ["De meesten vluchten gaan tussen 15:00 en 20:00."],
  "wanneer gaan de meesten vluchten?": ["De meesten vluchten gaan tussen 15:00 en 20:00."],
  "Hoelang duurt het om een vlucht te boeken":["Een vlucht boeken duurt tussen de 2-3 minuten"],
  "hoelang duurt het om een vlucht te boeken":["Een vlucht boeken duurt tussen de 2-3 minuten"],
  "Hoelang duurt het om een vlucht te boeken?":["Een vlucht boeken duurt tussen de 2-3 minuten"],
  "hoelang duurt het om een vlucht te boeken?":["Een vlucht boeken duurt tussen de 2-3 minuten"],
  "noem een kattenfeitje": [get_cat_fact()]
}


def get_response(message):
  for pattern in patterns:
    match = re.search(pattern, message)
    if match:
      return patterns[pattern].format(match.group(1))

  if message in responses:
    return random.choice(responses[message])
  else:
    return "Ik begrijp je niet."

while True:
  message = input("YOU: ")
  response = get_response(message)
  print("Bot: " + response) 
  