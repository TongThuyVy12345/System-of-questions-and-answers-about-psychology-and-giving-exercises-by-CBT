# import googletrans
# from googletrans import Translator
# text="subscribe"
# translator=Translator()
# print(translator.detect(text))
# print("Translated from English:",translator.translate(text))
# # print(googletrans.LANGUAGES)
# from googletrans import Translator
# import pandas as pd
# import time
# import random
# # Create a translator object
# translator = Translator()
#
# # Read xlsx file and select column to translate
# df = pd.read_excel('D:/Data AI/Exercises.xlsx')
# # print(df.head())
# column_to_translate = 'Tittle'
# print("Loading....")
#
# df[column_to_translate] = df[column_to_translate].apply(lambda x: translator.translate(x, dest='en').text)
# time.sleep(random.random() + 1)
# print(df[column_to_translate])
# Write the translated data to a new xlsx file
