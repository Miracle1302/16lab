import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

# Завантаження необхідних ресурсів
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Вихідний текст
text = ("It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. "
        "It is rather for us to be here dedicated to the great task remaining before us; that from these honored dead we take increased devotion to that cause for which they here gave the last full measure of devotion; "
        "that we here highly resolve that these dead shall not have died in vain; that this nation, under God, shall have a new birth of freedom, and that government of the people, by the people, for the people, shall not perish from the Earth")

# Токенізація тексту
tokens = word_tokenize(text)

# Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
stemmed_tokens = [stemmer.stem(token) for token in tokens]

# Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in stemmed_tokens if token.lower() not in stop_words]

# Видалення пунктуації
filtered_tokens = [token for token in filtered_tokens if token not in string.punctuation]

# Об'єднання оброблених токенів у текст
processed_text = ' '.join(filtered_tokens)

# Запис обробленого тексту у інший файл
output_file_path = 'text.txt'  # Змініть цей шлях на шлях до вашого файлу
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(processed_text)

print("Оброблений текст записано у файл:", output_file_path)
