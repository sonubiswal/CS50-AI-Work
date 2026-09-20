import nltk
import sys
import re

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never" | "quietly"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "the" | "times" | "watson" | "wave" | "we" | "word"
N -> "walk" | "thursday"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "come" | "felt" | "frowned" | "hear" | "looked" | "remember"
V -> "sat" | "saw" | "said" | "served" | "stared" | "watch"
V -> "had" | "came"
"""

NONTERMINALS = """
S -> NP VP
NP -> N
NP -> Det N
NP -> Det Adj N
NP -> Det N PP
NP -> Det Adj N PP
NP -> NP PP
NP -> NP Conj NP
VP -> V
VP -> V NP
VP -> V NP PP
VP -> VP Adv
VP -> VP PP
VP -> VP Conj VP
PP -> P NP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    # Lowercase the sentence
    sentence = sentence.lower()

    # Tokenize using nltk
    tokens = nltk.word_tokenize(sentence)

    # Keep only tokens that contain at least one letter
    return [token for token in tokens if re.search(r"[a-z]", token)]


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    chunks = []
    for subtree in tree.subtrees():
        if subtree.label() == "NP":
            # Check if this NP has any other NP as a descendant
            has_np_descendant = False
            for descendant in subtree.subtrees():
                if descendant is subtree:
                    continue
                if descendant.label() == "NP":
                    has_np_descendant = True
                    break
            if not has_np_descendant:
                chunks.append(subtree)
    return chunks


if __name__ == "__main__":
    main()