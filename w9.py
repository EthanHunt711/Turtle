import nltk
from nltk.corpus import stopwords
from itertools import islice

en_stop = list(stopwords.words('english'))
tokenizer = nltk.RegexpTokenizer(r"\w+")


def is_english_title(st_code):
    if st_code[0] in 'ADWS':
        return True


def get_words(title):
    new_title = ''
    for w in title.lower().split():
        if w not in en_stop:
            new_title = ''.join(w)
    return tokenizer.tokenize(new_title.lower())


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
with open('isv/inducks_herocharacter.isv', 'r', encoding='utf-8',
          errors='ignore') as f:
    for line in islice(f, 1, None):
        st_code, char_code, rest = line.split('^', 2)
        if is_english_title(st_code):
            story_to_hero[st_code] = char_code

hero_to_wordfreqs = {}
with open('isv/inducks_story.isv', 'r', encoding='utf-8', errors='ignore') \
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


def main():
    with open('isv/inducks_charactername.isv', 'r', encoding='utf-8', errors='ignore') as f:
        for line in islice(f, 1, None):
            char_code, lang_code, ch_name, pref, rest = line.split('^', 4)
            if lang_code == 'en':
                if pref == 'Y':
                    if char_code in hero_to_wordfreqs.keys():
                        if len(hero_to_wordfreqs.get(char_code).values()) > 10:
                            print(f'Top words for {ch_name} is:')
                            for value in sorted(hero_to_wordfreqs[char_code].items(), key=lambda x: x[1],
                                                reverse=True)[:5]:
                                print(f"{str(value[1]).rjust(5)}    {value[0]}")


if __name__ == "__main__":
    main()
