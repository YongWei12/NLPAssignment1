from nltk.tokenize import sent_tokenize, word_tokenize
import cv2
import os

# example_text = "Hi here, I am a boy.  Mr. Smith says you are a loser \n asdsasdsasda"

def convert(lst):   
    return '|'.join(lst) 

# iterating through the whole dataset
directory = "./data/sigbovik/"
output = "./output/sigbovik"

# function to read files in directory and tokenize it
def tokenizeFile (input, output=0):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            f = open(os.path.join(directory, filename), "r",  encoding="utf8") 
            Lines = f.readlines()
            file_out =open(os.path.join(output, filename), "w", encoding="utf8")
            for line in Lines:
                file_out.write(convert(word_tokenize(line))+"\n")
            continue
        else:
            continue



tokenizeFile(directory,output )



# try out code
# print(os.listdir())
# my_file = "./scripts/demo.txt"
# f = open(my_file, "r",  encoding="utf8")
# Lines = f.readlines()
# file_out =open(os.path.join(output, "demo.txt"), "w", encoding="utf8")
# for line in Lines:
#     file_out.write(convert(word_tokenize(line))+"\n")


# for i in word_tokenize(example_text):
#     print(i)
