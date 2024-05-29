import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import pandas as pd
import matplotlib.pyplot as plt


file_path = 'burgess-busterbrown.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Токенізація тексту
nltk.download('punkt')
words = nltk.word_tokenize(text)

# Визначення кількості слів у тексті
word_count = len(words)
print(f"Кількість слів у тексті: {word_count}")

# Визначення 10 найбільш вживаних слів
fdist = FreqDist(words)
most_common_words = fdist.most_common(10)
print("10 найбільш вживаних слів:")
for word, frequency in most_common_words:
    print(f"{word}: {frequency}")

# Побудова стовпчастої діаграми для 10 найбільш вживаних слів
plt.figure(figsize=(10, 6))
most_common_words_df = pd.DataFrame(most_common_words, columns=['Word', 'Frequency'])
plt.bar(most_common_words_df['Word'], most_common_words_df['Frequency'])
plt.title('10 найбільш вживаних слів у тексті')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.show()

# Видалення стоп-слів та пунктуації
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
words_filtered = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

# Визначення 10 найбільш вживаних слів після видалення стоп-слів та пунктуації
fdist_filtered = FreqDist(words_filtered)
most_common_words_filtered = fdist_filtered.most_common(10)
print("10 найбільш вживаних слів після видалення стоп-слів та пунктуації:")
for word, frequency in most_common_words_filtered:
    print(f"{word}: {frequency}")

# Побудова стовпчастої діаграми для 10 найбільш вживаних слів після видалення стоп-слів та пунктуації
plt.figure(figsize=(10, 6))
most_common_words_filtered_df = pd.DataFrame(most_common_words_filtered, columns=['Word', 'Frequency'])
plt.bar(most_common_words_filtered_df['Word'], most_common_words_filtered_df['Frequency'])
plt.title('10 найбільш вживаних слів у тексті після видалення стоп-слів та пунктуації')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.show()


