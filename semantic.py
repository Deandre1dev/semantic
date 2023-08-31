import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
# What I found intresting about the similarity between cat, monkey and banana is that :
# Cat and Monkey has the highest similarity as a result that they are both animals.
# Banana and Monkey is the second highest similarity as a result that Banana is a food source for a Monkey.
# Banana and Cat has the lowest similarity as a Cat is not usually associated with a Banana 

# My own example
word1 = nlp("dog")
word2 = nlp("bone")
word3 = nlp("water")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
# What I found intresting about the similarity between dog, bone and water is that :
# Dog and Bone has the second highest similarity which is intresting as a dog should be associated with a dog.
# Water and Bone has the highest similarity which is strange as you would not usually associate water with a bone.
# Water and Dog has the lowest similarity which is strange as a dog drinks water to prevent hydration.

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)