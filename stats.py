from collections import Counter

def get_num_words(contents):
    return len(contents.split())


def get_char_counts(contents):
    return Counter(contents)


def transform_dict(dictionary):
    def sort_on(dict):
        return dict["count"]

    stats = []
    for key, value in dictionary.items():
        char_count = {}
        char_count["char"] = key
        char_count["count"] = value
        stats.append(char_count)
    
    stats.sort(reverse=True, key=sort_on)
    return stats
