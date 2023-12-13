#!/usr/bin/env python3

class MyString:
  def __init__(self, value = '') -> None:
      self.value = value

  @property
  def value(self):
      return self._value
  
  @value.setter
                #can usually set to anything butpeople ussually set to the same name
  def value(self, value):
      if type(value) == str:
          self._value = value
      else:
          print("The value must be a string.")
  
  def is_sentence(self):
      last_character = self.value[-1]

      # return last_character == '.'
      return self.value.endswith('.')
  
  def is_question(self):
      last_character = self.value[-1]

      # return last_character == '.'
      return self.value.endswith('?')

  def is_exclamation(self):
      last_character = self.value[-1]

      # return last_character == '.'
      return self.value.endswith('!')\
  
  def count_sentences(self):
      sentence = 0
      prev_character = ''
      for c in self.value:
          if c in ['.', '!', '?'] and prev_character.isalpha() :
              sentence += 1
          prev_character = c
      return sentence