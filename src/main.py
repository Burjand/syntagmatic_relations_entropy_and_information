import os
import config
from Preprocessing import Preprocessing
from Syntagmatic_relation_conditional_entropy import Syntagmatic_relation_conditional_entropy
import pandas as pd


if __name__ == "__main__":

    # Paths
    raw_files_path = config.raw_files_path
    processed_files_path = config.processed_files_path

    corpus_file = config.corpus_file
    stopwords_file = config.stopwords_file
    encoding = config.encoding

    vocabulary_file = config.vocabulary_file
    lemmatized_sentences_file = config.lemmatized_sentences_file

    tdm_file = config.tdm_file
    tdm_normalized_file = config.tdm_normalized_file

    # Preprocess

    if (os.path.exists(processed_files_path + vocabulary_file) and os.path.exists(processed_files_path + lemmatized_sentences_file)):

        f = open(processed_files_path + vocabulary_file, "r")
        vocabulary = [word.replace("\n","") for word in f.readlines()]
        f.close()

        f = open(processed_files_path + lemmatized_sentences_file, "r")
        lemmatized_sentences = [(sentence.replace("\n","")).split() for sentence in f.readlines()]
        f.close


    else:

        preprocessed_text = Preprocessing(raw_files_path + corpus_file, raw_files_path + stopwords_file, encoding)

        vocabulary = preprocessed_text.vocabulary
        lemmatized_sentences = preprocessed_text.lemmatized_sentences

        f = open(processed_files_path + vocabulary_file, "w")
        f.writelines([f'{word}\n' for word in vocabulary])
        f.close()

        f = open(processed_files_path + lemmatized_sentences_file, "w")
        f.writelines([f'{" ".join(sentence)}\n' for sentence in lemmatized_sentences])
        f.close()    


    # Syntagmatic relation through conditional entropy

    sr_ce_organizacion_object = Syntagmatic_relation_conditional_entropy()
    sr_ce_organizacion = sr_ce_organizacion_object.word_syntagmatic_relations
