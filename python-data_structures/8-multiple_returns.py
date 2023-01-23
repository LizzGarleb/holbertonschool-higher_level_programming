#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sentence = None
    tu_len = len(sentence)
    return(tu_len, sentence[0][0])
