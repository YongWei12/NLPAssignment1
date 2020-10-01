from nltk.tokenize import sent_tokenize, word_tokenize
import os

# function to convert the tokenizer output style
def convert(lst):   
    return '\n'.join(lst) 

# declare the directory
directory = "./data/sigbovik/"
outputTokenizer = "./output/sigbovik/Tokenizer"
outputStemming= "./output/sigbovik/Stemming"

# function to read files in directory and tokenize it
def tokenizeFile (input, output=0,combine=False ):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            f = open(os.path.join(directory, filename), "r",  encoding="utf8") 
            text = f.read()
            if combine == False:
                file_out =open(os.path.join(output, filename), "w", encoding="utf8")
                tokenize_list =list(dict.fromkeys(word_tokenize(text)))
                file_out.write(convert(tokenize_list)+"\n")
            else:
                file_out =open(os.path.join(output, "combined_files.txt"), "a+", encoding="utf8")
                tokenize_list =list(dict.fromkeys(word_tokenize(text)))
                file_out.write(convert(tokenize_list)+"\n") 
            continue
        else:
            continue

#Function to stem the files 



#calling the tokenizer function
tokenizeFile(directory,outputTokenizer,True )



# try out code
# print(os.listdir())
# my_file = "./scripts/demo.txt"
# f = open(my_file, "r",  encoding="utf8")
# Lines = f.readlines()
# print(f.read())
# file_out =open(os.path.join(output, "demo.txt"), "w", encoding="utf8")
# for line in Lines:
#     file_out.write(convert(word_tokenize(line))+"\n")


# for i in word_tokenize(example_text):
#     print(i)
