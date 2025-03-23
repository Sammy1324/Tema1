class Words:
    def __init__(self, list_of_words):
        self.words = list_of_words
        
    def common_words(self, other):
        return set(self.words).intersection(other.words)