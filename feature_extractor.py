from sklearn.feature_extraction.text import CountVectorizer

def extract_features(codes):
    vectorizer = CountVectorizer(tokenizer=lambda x: x, preprocessor=lambda x: x)
    return vectorizer.fit_transform(codes)
