import nltk
from nltk.stem import PorterStemmer
w=PorterStemmer()
print("SHOWING ROOT WORD")
print(w.stem("eating"))
from nltk.corpus import stopwords
nltk.download("stopwords")
print(stopwords.words("English"))
print("To Remove Whitespaces")
def remove_whitespace(text):
    return  " ".join(text.split())
input_str = "   we don't need   the given questions"
remove_whitespace(input_str)
