# Write a program to Implement PoS tagging using HMM & Neural Model

import nltk

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('universal_tagset')

text = "NLTK provides support for both HMM and NN-based PoS tagging."

words = nltk.word_tokenize(text)

hmm_tagged = nltk.pos_tag(words)
print("PoS tagging using HMM:", hmm_tagged)

nn_tagged = nltk.pos_tag(words, tagset='universal')
print("PoS tagging using NN:", nn_tagged)