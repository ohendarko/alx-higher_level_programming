#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    ln = len(sentence)
    first_ch = sentence[0]
    return (ln, first_ch)
