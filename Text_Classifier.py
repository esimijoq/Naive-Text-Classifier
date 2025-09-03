from os import link
import requests

text_1 = "What a truly wonderful day! The sun is shining, birds are singing, and everything feels absolutely perfect. I'm filled with immense joy and gratitude. Life is beautiful."

text_2 = "This new restaurant is simply fantastic! The food was delicious, the service impeccable, and the atmosphere delightful. I highly recommend it; a truly enjoyable experience overall."

text_3 = "Today has been utterly miserable. The rain poured incessantly, my internet kept crashing, and I felt completely overwhelmed. A truly frustrating and disappointing day."

text_4 = "I'm so incredibly upset with this product. It broke almost immediately, the support was unhelpful, and I feel completely ripped off. A terrible purchase, I regret it."

texts = ["What a truly wonderful day! The sun is shining, birds are singing, and everything feels absolutely perfect. I'm filled with immense joy and gratitude. Life is beautiful.", "This new restaurant is simply fantastic! The food was delicious, the service impeccable, and the atmosphere delightful. I highly recommend it; a truly enjoyable experience overall.", "Today has been utterly miserable. The rain poured incessantly, my internet kept crashing, and I felt completely overwhelmed. A truly frustrating and disappointing day.", "I'm so incredibly upset with this product. It broke almost immediately, the support was unhelpful, and I feel completely ripped off. A terrible purchase, I regret it."]

texts_new = []
for text in texts:
  text_new = text.replace(".", "").replace("!","").replace(",","").replace("'","")
  texts_new.append(text_new)

with open("ADD_THE_LINK_OF_THE_FILE", 'r') as file:
  f = file.read()
  text_txt = f.split("\n\n")

texts_from_txt = []
for text in text_txt:
  text_new = text.replace(".", "").replace("!","").replace(",","").replace("'","").replace(";", "").replace("\n", "")
  texts_from_txt.append(text_new)

for text in texts_from_txt:
  texts_new.append(text)

texts_new_split = []
for text in texts_new:
  txt = text.split(" ")
  texts_new_split.append(txt)

def get_synonyms(word):
  link_vocabulary = requests.get(f"https://api.api-ninjas.com/v1/thesaurus?word={word}", headers= {"X-Api-Key": "ADD_YOUR_KEY"})
  return link_vocabulary.json()["synonyms"][:2]

positive_new = []
positive = ["wonderful", "perfect", "joy", "beautiful", "fantastic", "delicious", "delightful", "enjoyable", "grateful"]
for word in positive:
  positive_vocabulary = get_synonyms(word)
  for word in positive_vocabulary:
    positive_new.append(word)

for word in positive:
  positive_new.append(word)

def positive (text, positive_new):
  count_positive = 0
  for a in positive_new:
    for b in text:
      if a == b:
        count_positive += 1
  return count_positive

negative_new = []
negative = ["miserable", "overwhelmed", "frustrating", "disappointing", "upset", "unhelpful", "terrible", "crashes"]
for word in negative:
  negative_vocabulary = get_synonyms(word)
  for word in negative_vocabulary:
    negative_new.append(word)

for word in negative:
  negative_new.append(word)

def negative(text, negative_new):
  count_negative = 0
  for a in negative_new:
    for b in text:
      if a == b:
        count_negative += 1
  return count_negative

def compare (text, positive_new, negative_new):
  if positive(text, positive_new) > negative(text, negative_new):
    print("Positive: ", positive(text, positive_new))
  elif negative(text, negative_new) > positive(text, positive_new):
    print("Negative: ", negative(text, negative_new))
  else:
    print("Neutral")
  return None

for text in texts_new_split:
  compare(text, positive_new, negative_new)

dictionary = {}
for text in texts_new_split:
  for word in text:
    dictionary[word]= 0
print(dictionary)


for text in texts_new_split:
  for word in text:
      dictionary[word] += 1

print(dictionary)

max_values = max(dictionary.values())
max_keys = []
for key in dictionary:
    if dictionary[key] == max_values:
        max_keys.append(key)

print(max_keys, max_values)

pos_neg_vocabulary = positive_new + negative_new
print(pos_neg_vocabulary)

pos_neg_dictionary = {}
for word in pos_neg_vocabulary:
  pos_neg_dictionary[word]= 0
print(pos_neg_dictionary)

for text in texts_new_split:
  for word in text:
    if word in pos_neg_dictionary:
      pos_neg_dictionary[word] += 1
print(pos_neg_dictionary)

max_pos_neg_values = max(pos_neg_dictionary.values())
max_pos_neg_keys = []
for key in pos_neg_dictionary:
    if pos_neg_dictionary[key] == max_pos_neg_values:
        max_pos_neg_keys.append(key)

print(max_pos_neg_keys, max_pos_neg_values)

token_dictionary = {}
for text in texts_new_split:
  for word in text:
    token_dictionary[word] = 0

for text in texts_new_split:
  for word in text:
    for word in token_dictionary:
      token_dictionary[word]

print(token_dictionary)
