from nltk.tokenize import sent_tokenize, word_tokenize
import cv2
import os

# example_text = "Hi here, I am a boy.  Mr. Smith says you are a loser \n asdsasdsasda"


# iterating through the whole dataset
directory = "./data/sigbovik/"
def readFiles (input, output):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"): 
            # do tokenisation here

            continue
        else:
            continue


# print(os.listdir())
# my_file = "./data/sigbovik/2017_batch_norm_my_ass.txt"
# f = open(my_file, "r",  encoding="utf8")
# Lines = f.readlines()
# for line in Lines:
#     print(line)


# for i in word_tokenize(example_text):
#     print(i)
