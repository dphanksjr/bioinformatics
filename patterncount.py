### the PatternCount function prints out how many times a pattern is found in a string of code ###
### Example: text = 'ACTGTACGATGATGTGTGTCAAAG' pattern = 'TGT' | The pattern is found 4 times. ###
### written by Daniel Hanks Jr ###

def PatternCount(text, pattern):
    count = 0
    sub_len = len(pattern)
    for i in range(len(text)):
        if text[i:i+sub_len] == pattern:
            count += 1
    print("Input \n"+ text)
    print("Output \n"+str(count))

text = 'ACTGTACGATGATGTGTGTCAAAG'
pattern = 'TGT'
PatternCount(text, pattern)