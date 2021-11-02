from itertools import islice


def is_english_title(st_code):
    if st_code[0] in 'ADWS':
        return True


def get_words(title):
    return title.lower().split()


def words_in_title_count_dict(title):
    st_code_title_words = {}
    for word in get_words(title):
        if word.isalpha() is True:
            if word in st_code_title_words:
                st_code_title_words[word] += 1
            else:
                st_code_title_words[word] = 1
    return st_code_title_words


story_to_hero = {}
with open('C:/Users/alies/PycharmProjects/Turtle/isv/inducks_herocharacter.isv', 'r', encoding='utf-8',
          errors='ignore') as f:
    for line in islice(f, 1, None):
        st_code, char_code, rest = line.split('^', 2)
        if is_english_title(st_code) is True:
            story_to_hero[st_code] = char_code

hero_to_wordfreqs = {}
with open('C:/Users/alies/PycharmProjects/Turtle/isv/inducks_story.isv', 'r', encoding='utf-8', errors='ignore') \
        as f:
    for line in islice(f, 1, None):
        st_code, osvc, cd, fpd, epd, title, rest = line.split('^', 6)
        if st_code in story_to_hero:
            if story_to_hero[st_code] in hero_to_wordfreqs:
                for word in get_words(title):
                    if word in hero_to_wordfreqs.get(story_to_hero[st_code]):
                        hero_to_wordfreqs.get(story_to_hero[st_code])[word] += 1
                    else:
                        hero_to_wordfreqs.get(story_to_hero[st_code])[word] = 1
            else:
                hero_to_wordfreqs[story_to_hero[st_code]] = words_in_title_count_dict(title)


# def main():
with open('C:/Users/alies/PycharmProjects/Turtle/isv/inducks_charactername.isv', 'r', encoding='utf-8', errors='ignore')as f:
    for line in islice(f, 1, None):
        char_code, lang_code, ch_name, pref, rest = line.split('^', 4)
        if lang_code == 'en':
            if pref == 'Y':
                if char_code in hero_to_wordfreqs.keys():
                    print(f'Top words for {ch_name} is:')
                    print(f"{hero_to_wordfreqs[char_code]}")





# if __name__ == "__main__":
#     main()
