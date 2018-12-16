### the PatternMatching function finds all occurrences of a pattern in a string ###
### Input: Pattern and Genome ###
### written by Daniel Hanks Jr ###

def PatternMatching(Pattern, Genome):
    index = 0
    while index < len(Genome):
        index = Genome.find(Pattern, index)
        if index == -1:
            break
        print('Starting Position found at', index)
        index += 1 

Pattern = 'AA'
Genome = 'AAACATAGGATCAAC '

PatternMatching(Pattern, Genome)
