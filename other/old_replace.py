def splitting_sentences(sentence, split_by):
    word_list = [word.strip() for word in sentence.split(split_by) if word]
    return word_list


def replace_str(word_list, sentence_num):
    chosen_word = ""
    for word in word_list:
        # randomize again if shorter than 2 chars or not alphanumeric
        # or any(not char.isalnum() for char in chosen_word):
        while len(chosen_word) < 2:
            chosen_word = word_list[random.randint(0, len(word_list)-1)]
        # replace random choice with fixed words_to_check if possible
        # TODO: pop() already used elements to avoid duplicated removals
        for word in words_to_check:
            if word in word_list:
                chosen_word = word
    # build gap
    char_count = len(chosen_word)
    replacement = f"({sentence_num}){' _' * char_count}"
    return [chosen_word, replacement]


def build_wiki_kw_gaps():
    removed_words = []
    gapped_passage = []

    for count, sentence in enumerate(sentences):
        # print(f"{count} zdanie: {sentence}")
        removed, replacement = replace_str(
            splitting_sentences(sentence, " "), count + 1)
        gapped_sentence = f"{sentence.replace(removed, replacement, 1)} "
        removed_words.append(removed)
        random.shuffle(removed_words)
        gapped_passage.append(gapped_sentence)

        print(f"zdanie z luką: {gapped_sentence}")
    print(
        f"usunięto {len(removed_words)} słów: {removed_words} z {len(gapped_passage)} zdań.")
    random_words = list(set(removed_words) - set(words_to_check))
    unchecked_words = list(set(words_to_check) - set(removed_words))
    print(f"losowe słowa: {random_words}")
    print(f"niesprawdzone słowa: {unchecked_words}")
    return [removed_words, gapped_passage]


build_wiki_kw_gaps()
