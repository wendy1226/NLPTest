# -*- coding: utf-8 -*-

#抓取Symptom
import nltk
import string
import re
from nltk.tokenize import sent_tokenize , word_tokenize

from nltk.corpus import stopwords
from collections import Counter
stop_words = set(stopwords.words('english')) #設定英文停用詞表

#文本內容
text = "After purchasing this computer, it glitched anytime i tried to have a video call (the database was being hit and the system would rapidly run out of memory.  I spent $500 having a tech try to decipher what was going on and we realized it was only happening when the system was plugged in.  So, i was left having to do video calls with my computer unplugged.  I am on video calls all day.  Recognizing it was going to take me a LONG time to re-review this with a person from DELL and having a job where i cannot afford to take time to troubleshoot these things, i have purchased a replacement system."

#step1:文本預處理
sentences = sent_tokenize(text) #斷句
words = word_tokenize(text) #斷詞
#去除停用詞
filtered_words = [] #存去除停用詞後的字詞
for word in words:
  lowercase_word = word.lower() #轉成小寫比對
  if lowercase_word not in stop_words:
    filtered_words.append(word)
#去除標點符號
words_without_punctuation = [] #存去除標點符號後的字詞
for word in filtered_words:
  if word not in string.punctuation:
    words_without_punctuation.append(word)

#step2:取得symptom關鍵字
word_freq = Counter(words_without_punctuation) #計算詞頻
most_common_words = word_freq.most_common(10) #根據詞頻找出最常見的詞
symptom_keywords = [] #存關鍵字
for word,freq in most_common_words:
  symptom_keywords.append(word)

#step3:找出與關鍵字匹配的句子
relevant_sentences = [] #存匹配的句子
for sentence in sentences:
  for keyword in symptom_keywords:
    if keyword in sentence:
      relevant_sentences.append(sentence)

#step4:將句子進行排序
sentence_counts = Counter(relevant_sentences) #計算次數
sort_sentences = sentence_counts.most_common() #降序排序
print("有symptom關鍵字出現的句子:")
for sentence , count in sort_sentences:
  print(f"'{sentence}' : 出現 {count} 次")

#判斷症狀數量(辨識有無編號作為是否有多個症狀的判斷依據)
pattern = r'\d+\.' #定義編號正則表示式
matches = re.findall(pattern , text)
num_symptoms = 1
for match in matches:
  num_symptoms = num_symptoms + 1 #計算匹配的數量
print("symptom數量:" , num_symptoms)