# xscience-eindopdracht
import re
import random

patterns = {
   "Weet je nog (.*)":"Natuurlijk weet ik nog {}.",
   "Ik voel me (.*)":"Waarom voel jij je {}?",
   "Ik wil graag (.*)": "Ik snap dat jij graag wilt{}."

}

responses = {
  "Hallo": ["Hoi, hoe gaat het?", "Hallo!"],
  "Het gaat goed": ["Goed om te horen!", "Geweldig!"]

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