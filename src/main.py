import os
import config
from Preprocessing import Preprocessing
from Words__frequencies import Words_frequencies
from Syntagmatic_relation_conditional_entropy import Syntagmatic_relation_conditional_entropy
from Syntagmatic_relation_mutual_information import Syntagmatic_relation_mutual_information

if __name__ == "__main__":

    # Paths
    raw_files_path = config.raw_files_path
    processed_files_path = config.processed_files_path

    corpus_file = config.corpus_file
    stopwords_file = config.stopwords_file
    encoding = config.encoding

    vocabulary_file = config.vocabulary_file
    lemmatized_sentences_file = config.lemmatized_sentences_file

    syntagmatic_relations_conditional_entropy_file = config.syntagmatic_relations_conditional_entropy_file
    syntagmatic_relations_mutual_information_file = config.syntagmatic_relations_mutual_information_file

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


    target_word = "organización"

    # Obtain relative frequencies of words

    individual_words_probabilities = Words_frequencies.compute_relative_frequencies(lemmatized_sentences, vocabulary)
    target_word_probabilities_with_others = Words_frequencies.compute_relative_frequencies_in_pairs(target_word, lemmatized_sentences, vocabulary)


    # Syntagmatic relation through conditional entropy

    if (os.path.exists(processed_files_path + syntagmatic_relations_conditional_entropy_file)):

        f = open(processed_files_path + syntagmatic_relations_conditional_entropy_file, "r")
        entropies_list = [word.replace("\n","") for word in f.readlines()]
        f.close()


    else:

        sr_ce_target_word_object = Syntagmatic_relation_conditional_entropy(target_word, individual_words_probabilities, target_word_probabilities_with_others, vocabulary)
        sr_ce_target_word = sr_ce_target_word_object.word_syntagmatic_relations

        entropies_list = []

        for word in sr_ce_target_word.keys():

            entropies_list.append([word, sr_ce_target_word[word]])

        entropies_list.sort(key=lambda x: x[1])

        f = open(processed_files_path + syntagmatic_relations_conditional_entropy_file, "w")    
        f.writelines([f'H({target_word}|{word}) = {entropy}\n' for word, entropy in entropies_list])
        f.close()

    
    # Syntagmatic relation through mutual information

    if (os.path.exists(processed_files_path + syntagmatic_relations_mutual_information_file)):

        f = open(processed_files_path + syntagmatic_relations_mutual_information_file, "r")
        informations_list = [word.replace("\n","") for word in f.readlines()]
        f.close()


    else:

        sr_mi_target_word_object = Syntagmatic_relation_mutual_information(target_word, individual_words_probabilities, target_word_probabilities_with_others, vocabulary)
        sr_mi_target_word = sr_mi_target_word_object.word_syntagmatic_relations

        informations_list = []

        for word in sr_mi_target_word.keys():

            informations_list.append([word, sr_mi_target_word[word]])

        informations_list.sort(key=lambda x: x[1], reverse=True)

        f = open(processed_files_path + syntagmatic_relations_mutual_information_file, "w")    
        f.writelines([f'I({target_word}|{word}) = {information}\n' for word, information in informations_list])
        f.close()
