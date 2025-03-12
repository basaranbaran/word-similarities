# Required Libraries
import gensim.downloader as api
from gensim.models import KeyedVectors

# Download the Word2Vec model
word_vectors = api.load("word2vec-google-news-300")

while True:
    print("if you want to exit, please write 'exit'\n")
    word1 = str(input("First word: "))
    if word1 == "exit":
        break
    word2 = str(input("Second word: "))

# Calculate the similarity between the words
    similarity_word1_word2 = word_vectors.similarity(f"{word1}", f"{word2}")
    similarity_word1_car = word_vectors.similarity(f"{word1}", "car")
    similarity_word2_car = word_vectors.similarity(f"{word2}", "car")
    similarity_word1_apple = word_vectors.similarity(f"{word1}", "apple")

# Write the results
    print(f"{word1} and {word2} similarity: {similarity_word1_word2}")
    print(f"{word1} ve car similarity: {similarity_word1_car}")
    print(f"{word2} ve car similarity: {similarity_word2_car}")
    print(f"{word1} ve apple similarity: {similarity_word1_apple}")

# Most similar words to the given words
    most_similar_word1 = word_vectors.most_similar(f"{word1}", topn=5)
    # similar words to "word1"
    print(f"\nSimilar words to {word1}':")
    for word, similarity in most_similar_word1:
        print(f"{word}: {similarity}")

    most_similar_word2 = word_vectors.most_similar(f"{word2}", topn=5)
    # similar words to "word2"
    print(f"\nSimilar words to {word2}':")
    for word, similarity in most_similar_word2:
        print(f"{word}: {similarity}")


    word3= str(input("word to be extracted from word1:"))
    # "word1" - "word3" + "word2" = ?
    result = word_vectors.most_similar(positive=[f"{word1}", f"{word2}"], negative=[f"{word3}"], topn=1)
    print(f"\n{word1} - {word3} + {word2} = ?")
    print(result+"\n")