# Interview Question 1.1 & 1.2, Alg to determine if a string has all unique characters
import re
from linked_list import Node, LinkedList

# Question 1.3 ###########################################################
# URLify: Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold
# the additional characters, and that you are given the "true" length of
# the string. (Note: If implementing in Java, please use a character array
# so that you can perform this operation in place.)
def replace_spaces(str):
    new = re.sub(r'\s','%20',str)
    return new

# Question 1.4 ###########################################################
# Palindrome Permutation: Given a string, write a function to check if it is
# a permutation of a palindrome. A palindrome is a word or phrase that is the
# same forwards and backwards. A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.
def palindrome(str):
    for i in range(len(str)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

# Question 2.1 ###########################################################
# Write code to remoce duplicates from an unsorted linked list.
def deleteDups(n):
    pass

# Question 2.2 ###########################################################
# Return Kth to Last: Implement an algorithm to find the kth to last
# element of a singly linked list
def kthElement(n, k):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(replace_spaces("Mr 3ohn Smith"))
    print(palindrome("tacocat"))
    print(palindrome("unique"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
