
import re
import random

patterns = {
   "Weet je nog (.*)":"Natuurlijk weet ik nog {}.",
   "Ik voel me (.*)":"Waarom voel jij je {}?",
   
}

responses = {
  "Hallo": ["Hoi, hoe gaat het?", "Hallo!"],
  "Het gaat goed": ["Goed om te horen!", "Geweldig!"]
  "Wat kost een gemiddelde vlucht": ["De gemiddelde vlucht kost €354  "]
  "wat kost een gemiddelde vlucht": ["De gemiddelde vlucht kost €354  "]
  "Wanneer gaat de meesten vluchten":
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
  print("Bot: " + response)- 
  Ik ben Abel en ik ben gay