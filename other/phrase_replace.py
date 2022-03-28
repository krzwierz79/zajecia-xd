import random
sentence_1 = "We don't have to iterate over separate words."
sentence_2 = "We'd be better off replacing multi-word sub-strings."
sentence_3 = "Or something random if nothing's interesting."
sentence_4 = "Or is bad."
sentences = [sentence_1, sentence_4, sentence_2, sentence_3]
# print(sentences)

phrases_to_replace = ["have to", "be better", "multi-word"] #multi- not replaced (in same sentence as better off)
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
print(gapped_text(phrases_to_replace, sentences))