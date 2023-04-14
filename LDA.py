import gensim
import spacy
from gensim import corpora, models, similarities

# Load the pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

# Load the LDA model and dictionary
lda_model = models.LdaModel.load('lda_model')
dictionary = corpora.Dictionary.load('dictionary')

# Tokenize and preprocess the input text
input_text = "This is an example input text"
input_doc = nlp(input_text)
input_tokens = [token.lemma_ for token in input_doc if not token.is_stop and token.is_alpha]
input_bow = dictionary.doc2bow(input_tokens)

# Get the topic distribution of the input
input_topic_dist = lda_model.get_document_topics(input_bow)

# Get the documents in the same topic as the input
topic_docs = [doc for doc in lda_model.get_document_topics(bow_corpus) if doc[0] == input_topic_dist[0][0]]

# Calculate the cosine similarity between the input and other documents in the same topic
index = similarities.MatrixSimilarity(lda_model[bow_corpus])
input_lda = lda_model[input_bow]
sims = index[input_lda]

# Sort the documents by similarity score in descending order
sorted_sims = sorted(enumerate(sims), key=lambda item: -item[1])

# Print the top 10 most similar documents
for i, sim in sorted_sims[:10]:
    print(f"Document {i}: similarity score = {sim}")
    print(documents[i])
