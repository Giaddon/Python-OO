

from random import choice 


class WordFinder:
    """ Word Finder: finds random words from a text file."""

    def __init__(self, file_path):
        """ creates a new word finder and calls the function __createList__ to create a list attribute """
        self.file_path = file_path
        self.words = self.__createList__()

    def __createList__(self):
        """ builds a new list from the input file """
        file_content = open(self.file_path)
        words_list = []
        for line in file_content:
            clean_line = line[:-1]
            words_list.append(clean_line)
        return words_list

    def random(self):
        """ randomply picks a word from the list"""
        return choice(self.words)
        
