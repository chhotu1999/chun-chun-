import spacy 
nlp = spacy.load("en_core_web_sm")
json_text = str(open("test.json").read())
doc = nlp(json_text)


# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
