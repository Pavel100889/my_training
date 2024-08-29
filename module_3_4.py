def single_root_words(root_word, *oter_word):
    same_words = []
    root_word_up = root_word.upper()
    oter_word_up = [s.upper() for s in oter_word]
    for i in range(len(oter_word)):
        if root_word_up in oter_word_up[i] or oter_word_up[i] in root_word_up:
            same_words.append(oter_word[i])
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
