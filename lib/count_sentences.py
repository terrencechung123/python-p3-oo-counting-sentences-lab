#!/usr/bin/env python3
# import ipdb


class MyString:
    print("Hello!")

    # ipdb.set_trace()
    def __init__(self, value=''):
        self.value = value
        print("The value must be a string.")
    # ipdb.set_trace()
    def is_sentence(self):
  # returns True if value ends with a period and False otherwise.
        last_char = self.value[len(self.value)-1]
        if last_char == '.':
            return True
        return False


    def is_question(self):
        last_char = self.value[len(self.value)-1]
        if last_char == '?':
            return True
        return False

    def is_exclamation(self):
        last_char = self.value[len(self.value)-1]
        if last_char == '!':
            return True
        return False

    def count_sentences(self):
        value = self.value
        # count_sentences = self.value.count('.')+self.value.count('?')+self.value.count('!')
        for punctuation in ['!','?']:
            value = value.replace(punctuation,'.')
        count_sentences = [s for s in value.split('.') if s]
        return len(count_sentences)
