class Words_frequencies():

    def compute_relative_frequencies(lemmatized_sentences, vocabulary):

        words_relative_frequencies = {}

        for word in vocabulary:

            words_relative_frequencies[word] = 0

            for sentence in lemmatized_sentences:

                if word in sentence:

                    words_relative_frequencies[word] += 1

        number_of_sentences = len(lemmatized_sentences)

        for word in vocabulary:

            words_relative_frequencies[word] /= number_of_sentences

        return words_relative_frequencies
    

    def compute_relative_frequencies_in_pairs(target_word, lemmatized_sentences, vocabulary):

        target_word_and_word_frequency = {}

        target_word_and_not_word_frequency = {}

        not_target_word_and_word_frequency = {}

        for word in vocabulary:

            target_word_and_word_frequency[word] = 0

            target_word_and_not_word_frequency[word] = 0

            not_target_word_and_word_frequency[word] = 0

            for sentence in lemmatized_sentences:

                if target_word in sentence and word in sentence:

                   target_word_and_word_frequency[word] += 1

                if target_word in sentence and word not in sentence:

                    target_word_and_not_word_frequency[word] += 1

                if target_word not in sentence and word in sentence:

                    not_target_word_and_word_frequency[word] += 1


        number_of_sentences = len(lemmatized_sentences)

        for word in vocabulary:

            target_word_and_word_frequency[word] /= number_of_sentences

            target_word_and_not_word_frequency[word] /= number_of_sentences

            not_target_word_and_word_frequency[word] /= number_of_sentences


        return [target_word_and_word_frequency, target_word_and_not_word_frequency, not_target_word_and_word_frequency]

