# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

from languages import LANGUAGES

def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    # implement your solution here
    #for each word in a language, check how many words in there occur in 
    #the users text
    
    #split string of text into a list of words
    new_text = text.lower().split()
    
    #we will store a language and how many times a word from this language
    #occur in user text
    word_occurence_in_languages = {}
    
    #loop through each language
    for language in languages:
        single_language = language['name']  # name of language we are dealing with right now
        word_occurence_in_languages[single_language] = 0  # initialize the counter for this language we are dealing with right now
        common_words = language['common_words']  #list of common words in each language
        
        #in each language, loop through every common_word
        for word in common_words:
            single_common_word = word
            
            #when a match is found from this language,
            if single_common_word in new_text:
                
                #add one to the count of this language
                word_occurence_in_languages[single_language] += 1
                
    #return the language with the highest count
    maxcount=0
    maxlanguage=""
    
    #find one with the greatest count
    maxcount=(max(word_occurence_in_languages.values()))
    
    #find name of language with maxcount
    maxlanguage=[key for key,value in word_occurence_in_languages.items()if value==maxcount][0]
  
    return maxlanguage
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# def detect_language(text, languages=LANGUAGES):
#     """Returns the detected language of given text."""
#     # implement your solution here
#     new_text = text.split()
#     language = LANGUAGES[0]['common_words']
#     new_language = language
#     for word in new_language:
#         b= word in new_text
#         if(b):
#             return "spanish"
#         else:
#             return "german"


