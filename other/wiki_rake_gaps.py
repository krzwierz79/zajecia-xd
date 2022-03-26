# https://wikipedia.readthedocs.io/en/latest/code.html
import wikipedia

# https://pypi.org/project/rake-nltk/
from rake_nltk import Rake

import re
import random


wiki = wikipedia.summary("github")
print(wiki)
def get_offline_sentences(text):
    # clean_book = open(file).read()
    sentences = re.split(r"(?<=[.?!])", text)  # keep punctuation
    if sentences[-1]:
        return sentences
    else:
        return sentences[:-1]


sentences = get_offline_sentences(wiki)


print(sentences)


# Uses stopwords for english from NLTK, and all puntuation characters by
# default
# r = Rake()
r = Rake()

# Extraction given the text.
r.extract_keywords_from_text(wiki)

# Extraction given the list of strings where each string is a sentence.
# r.extract_keywords_from_sentences(<list of sentences>)

# To get keyword phrases ranked highest to lowest.
ranked = r.get_ranked_phrases()
# ranked = ['use', 'typed', 'typed', 'typed', 'successor', 'small', 'released']
# print(ranked[:5])
by_set = list(set(ranked))
# print(by_set[:5])
by_dict = list(dict.fromkeys(ranked))
# print(by_dict[:5])

# To get keyword phrases ranked highest to lowest with scores.
# print(r.get_ranked_phrases_with_scores())


# words_to_check = ['seldom', 'mansion', 'untenanted', 'superstition', 'believe', 'extreme', 'scoffs']

phrases_to_replace = by_dict[:5]

# print(sentences)


def replace_letters(phrase):
    replacement = ''
    for char in phrase:
        if char.isspace():
            replacement += 2*char
        else: replacement += '_ '
    return replacement

# print(replace_letters(phrase_to_replace))
def gapped_text(phrases_to_replace, sentences):
    gap_num = 0
    replaced_phrases = []
    for count, sentence in enumerate(sentences):
        print(f"now checking '{sentence}'")
    # replace one phrase from each sentece
        for phrase in phrases_to_replace:
            print(f"checking if '{phrase}' is in '{sentence}'\n\n")
            # prioritize given list of phrases to replace
            if phrase in sentence:
                gap_num += 1
                sentences[count] = sentence.replace(phrase, f"({gap_num}) {replace_letters(phrase)}", 1)
                print(f"gap '{gap_num}' created")
                print(f"adding '{phrase}' to replaced_phrases")
                replaced_phrases.append(phrase)
                print(f"replaced_phrases is now {replaced_phrases}")
                phrases_to_replace.remove(phrase)
                break
            else:
                # replace random word in remaining sentences
                wordlist = sentence.split(' ')
                word = ""
                tries = 0
                while len(word) < 3 or not word.isalpha() or not word.islower():
                    word = wordlist[random.randint(0,len(wordlist) - 1)]
                    tries += 1
                    if tries > 30:
                        word = ""
                        break
                sentence = " ".join(wordlist)
                if word != "":
                    print(f"removing randomly choes '{word}' from {sentence}")
                    gap_num += 1
                    print(f"gap '{gap_num}' created")
                    sentences[count] = sentence.replace(word, f"({gap_num}) {replace_letters(word)}", 1)
                    print(f"adding '{word}' to replaced_phrases")
                    replaced_phrases.append(word)
                    print(replaced_phrases)
                    print(f"replaced_phrases is now {replaced_phrases}")
                else:
                    sentences[count] = sentence
                    # gap_num -= 1
    return sentences, replaced_phrases        

# gapped_sentence = sentence_1.replace(phrase_to_replace, replace_letters(phrase_to_replace), 1)
# print(gapped_sentence)
print("\n\n")
exercise, box = gapped_text(phrases_to_replace, sentences)
print(box)
print("=" * 10)
print(exercise)
