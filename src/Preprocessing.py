from bs4 import BeautifulSoup
import nltk
import spacy
import re

class Preprocessing():

    def __init__(self, corpus_file, stopwords_file, encoding="UTF-8"):

        # Extract raw text
        self.raw_text = self.extract_text_from_file(corpus_file, encoding)

        # Extract text without HTML
        self.no_html_text = self.clean_text_from_html_tags(self.raw_text)

        #Lower case
        self.lower_cased_text = self.lower_case(self.no_html_text)

        # Tokenize
        self.tokenized_text = self.tokenize(self.lower_cased_text)

        # Build sentence-based contexts
        self.raw_sentences = self.build_sentences(self.tokenized_text)        

        # Clean text from punctuation marks
        self.sentences_no_punctuation = self.remove_punctuation_marks_and_blanks(self.raw_sentences)

        # Clean text from stopwords
        self.sentences_no_stopwords_no_punctuation = self.remove_stopwords(self.sentences_no_punctuation, stopwords_file, encoding)

        # Create spacy document and lemmatize
        self.raw_lemmatized_sentences = self.create_spacy_document(self.sentences_no_stopwords_no_punctuation)

        #Clean lemmatized sentences from error caused by lemmatization process ("uniformar él", "interesar yo", etc)
        self.lemmatized_sentences = self.clean_lemmatized_sentences(self.raw_lemmatized_sentences)

        # Vocabulary
        self.vocabulary = self.obtain_vocabulary(self.lemmatized_sentences)
    


    def extract_text_from_file(self, file, encoding):

        file = open(file, "r", encoding=encoding)
        raw_text = file.read()
        file.close()

        return raw_text

    

    def clean_text_from_html_tags(self, raw_text):

        soup = BeautifulSoup(raw_text)
        
        return soup.get_text()

    
        
    def lower_case(self, text_to_lower):

        return text_to_lower.lower()


    
    def tokenize(self, text_to_tokenize):

        tokenized_text = nltk.word_tokenize(text_to_tokenize)

        return(tokenized_text)

    

    def build_sentences(self, tokenized_text):

        raw_sentences = []

        temp_sentence = []

        for item in tokenized_text:            

            if (item == '.'):

                raw_sentences.append(temp_sentence)
                temp_sentence = []

            else:

                temp_sentence.append(item)

        return raw_sentences



    def remove_punctuation_marks_and_blanks(self, raw_sentences):

        sentences_no_punctuation = []

        for sentence in raw_sentences:

            temp_sentence = []

            for item in sentence:

                cleaned_item = ""
                for character in item:

                    if (character.isalpha()):

                        cleaned_item += character

                if cleaned_item != "":

                    temp_sentence.append(cleaned_item)

            sentences_no_punctuation.append(temp_sentence)

        return sentences_no_punctuation



    def remove_stopwords(self, sentences_no_punctuation, stopwords_file, encoding):

        file = open(stopwords_file, "r", encoding=encoding)
        stopwords_raw = file.readlines()
        file.close()

        stopwords_list = [word.replace("\n","") for word in stopwords_raw]

        sentences_no_stopwords = []

        for sentence in sentences_no_punctuation:

            temp_sentence = []

            for item in sentence:

                if item not in stopwords_list:

                    temp_sentence.append(item)
            
            sentences_no_stopwords.append(temp_sentence)

        return sentences_no_stopwords   

    
    
    def create_spacy_document(self, sentences_no_stopwords_no_punctuation):

        lemmatized_sentences = []

        nlp = spacy.load('es_core_news_md')
        
        for sentence in sentences_no_stopwords_no_punctuation:

            text_to_lemmatize = " ".join([word for word in sentence])            

            doc = nlp(text_to_lemmatize)

            lemmatized_sentences.append([token.lemma_ for token in doc])

        print(lemmatized_sentences)

        return lemmatized_sentences



    def clean_lemmatized_sentences(self, raw_lemmatized_sentences):

        for i in range(len(raw_lemmatized_sentences)):

            for j in range(len(raw_lemmatized_sentences[i])):

                raw_lemmatized_sentences[i][j] = re.sub(r"\s.*","",raw_lemmatized_sentences[i][j])

        return raw_lemmatized_sentences
    


    def obtain_vocabulary(self, lemmatized_sentences):

        # Obtain vocabulary
        lemmatized_text = []

        for sentence in lemmatized_sentences:

            for token in sentence:

                lemmatized_text.append(token)
        

        vocabulary = sorted(list(set(lemmatized_text)))
                

        return vocabulary

