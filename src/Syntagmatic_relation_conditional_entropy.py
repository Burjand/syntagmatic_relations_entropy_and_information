import math

class Syntagmatic_relation_conditional_entropy():

    def __init__(self, target_word, individual_words_probabilities, target_word_probabilities_with_others, vocabulary):

        self.target_word = target_word

        self.individual_words_probabilities = individual_words_probabilities

        self.target_word_and_word_frequency = target_word_probabilities_with_others[0]

        self.target_word_and_not_word_frequency = target_word_probabilities_with_others[1]

        self.not_target_word_and_word_frequency = target_word_probabilities_with_others[2]

        self.vocabulary = vocabulary

        self.word_syntagmatic_relations = self.compute_syntagmatic_relations()

    
    def compute_syntagmatic_relations(self):

        syntagmatic_relations = {}

        for word in self.vocabulary:

            syntagmatic_relations[word] = self.H(word)

        return syntagmatic_relations

    
    def H(self, w2):

        pw2 = self.individual_words_probabilities[w2]

        try:

            Hw1w2 = (
                
                        (((1-self.target_word_and_word_frequency[w2]) / (1-pw2)) * math.log(((1-self.target_word_and_word_frequency[w2])))
                    +  (self.target_word_and_not_word_frequency[w2] / (1-pw2) * math.log(self.target_word_and_not_word_frequency[w2] / (1-pw2)))) * (1-pw2)
                    +  (((self.not_target_word_and_word_frequency[w2] / (pw2)) * math.log(self.not_target_word_and_word_frequency[w2] / (pw2)))
                    +  ((self.target_word_and_word_frequency[w2] / (pw2)) * math.log(self.target_word_and_word_frequency[w2] / (pw2)))) * (pw2)
                    
                    ) *(-1)
            
        except(ValueError):

            Hw1w2 = 1000

        return Hw1w2