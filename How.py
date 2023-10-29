# -*- coding: utf-8 -*-

#抓取How
import nltk
import string
from nltk.tokenize import sent_tokenize , word_tokenize

#文本內容
text = "After purchasing this computer, it glitched anytime i tried to have a video call (the database was being hit and the system would rapidly run out of memory.  I spent $500 having a tech try to decipher what was going on and we realized it was only happening when the system was plugged in.  So, i was left having to do video calls with my computer unplugged.  I am on video calls all day.  Recognizing it was going to take me a LONG time to re-review this with a person from DELL and having a job where i cannot afford to take time to troubleshoot these things, i have purchased a replacement system."

#step1:取得關鍵字
context_keywords = ["When", "in" , "issue" , "If" , "Whenever",  "While", "During", "As", "Due to", "Because of", "In the event of", "In case of",
                    "Under the circumstances", "Considering that", "Given that", "In light of", "On the condition that", "Assuming that"]

#step2:找出與關鍵字匹配的句子
#step3:提取包含關鍵字與關鍵字後的內容
#先將文本與關鍵字轉成小寫，以便比對
text = text.lower() #文本轉成小寫
sentences = sent_tokenize(text) #斷句
lowercase_keywords = [] #存小寫的關鍵字
for keyword in context_keywords:
  lowercase_keyword = keyword.lower()
  lowercase_keywords.append(lowercase_keyword)

#搜尋每個句子進行比對
found_keyword = False
for sentence in sentences:
  words = word_tokenize(sentence)
  for keyword in lowercase_keywords:
    if keyword in words:
      found_keyword = True
      index = words.index(keyword) + 1 #找keyword與後面內容的index
      extracted_content = " ".join(words[index:]).strip() #取出keyword後的內容
      print("keyword:", keyword) #印出keyword
      print("context:", keyword , extracted_content) #印出keyword及後面內容
if not found_keyword: #沒找到keyword
  print("not found any keywords!")
