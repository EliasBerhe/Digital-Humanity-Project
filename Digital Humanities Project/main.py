#all necessary imports, downloads or funcitond
import nltk
from functions import *
from nltk.tokenize import *
nltk.download("punkt")
nltk.download('averaged_perceptron_tagger')

# used this function to plug in the text file (first) that the text we are examining came from (second)
print(Type_Token_Ratio1("compareTwo", "hope"))
print(avgSenLen1("compareTwo", "hope"))
print(nvaadRatio("compareTwo", "hope"))
print(avgPunkt1("compareTwo", "hope"))