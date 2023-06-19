import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

from Levenshtein import distance

# set nltk folder
nltk.data.path.append('./nltk_data')
nltk.download('punkt', download_dir='./nltk_data', quiet=True)
nltk.download('stopwords', download_dir='./nltk_data', quiet=True)

# stop_words = set(stopwords.words('english'))
# stop words indonesia
stop_words = set(stopwords.words('indonesian'))

def preprocess_text(text):
    # Tokenize the text into words
    tokens = word_tokenize(text.lower())

    # Remove stopwords
    filtered_tokens = [token for token in tokens if token not in stop_words]

    # Join the filtered tokens back into a single text
    preprocessed_text = ' '.join(filtered_tokens)

    return preprocessed_text

def calculate_jaccard_similarity(text1, text2):
    # Preprocess the texts
    preprocessed_text1 = preprocess_text(text1)
    preprocessed_text2 = preprocess_text(text2)

    # Create sets of word n-grams
    n = 2  # Adjust the n-gram value as needed
    grams1 = set(ngrams(preprocessed_text1.split(), n))
    grams2 = set(ngrams(preprocessed_text2.split(), n))

    # Calculate the Jaccard similarity
    jaccard_similarity = len(grams1.intersection(grams2)) / len(grams1.union(grams2))

    return jaccard_similarity

def calculate_cosine_similarity(text1, text2):
    # Preprocess the texts
    preprocessed_text1 = preprocess_text(text1)
    preprocessed_text2 = preprocess_text(text2)

    # Vectorize the texts using TF-IDF
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([preprocessed_text1, preprocessed_text2])

    # Calculate the cosine similarity
    rcosine_similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    return rcosine_similarity

def calculate_levenshtein_distance(text1, text2):
    # Preprocess the texts
    preprocessed_text1 = preprocess_text(text1)
    preprocessed_text2 = preprocess_text(text2)

    # Calculate the Levenshtein distance
    levenshtein_distance = distance(preprocessed_text1, preprocessed_text2)

    # Normalize the distance between 0 and 1
    max_length = max(len(preprocessed_text1), len(preprocessed_text2))
    levenshtein_similarity = 1 - (levenshtein_distance / max_length)

    return levenshtein_similarity

def calculate_similarity(text1, text2):
    # Calculate the similarity scores using different measures
    jaccard_similarity = calculate_jaccard_similarity(text1, text2)
    cosine_similarity = calculate_cosine_similarity(text1, text2)
    levenshtein_similarity = calculate_levenshtein_distance(text1, text2)

    # Adjust the weights of each similarity measure as needed
    weight_jaccard = 0.4
    weight_cosine = 0.4
    weight_levenshtein = 0.2

    # Combine the similarity scores using weighted average
    similarity_score = (weight_jaccard * jaccard_similarity +
                        weight_cosine * cosine_similarity +
                        weight_levenshtein * levenshtein_similarity)

    return similarity_score
