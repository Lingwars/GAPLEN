import nltk

sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
print(sentence)
tokens = nltk.word_tokenize(sentence)
print(tokens)
tagged = nltk.pos_tag(tokens)
print(tagged[0:6])
entities = nltk.chunk.ne_chunk(tagged)
print(entities)
