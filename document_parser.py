# # This function will make some updates to the underlying text that we have to ensure that it is more in line with
    # # expectations.  It will do the following 1) make everything lowercase, the underlying assumption here is that we
    # # only care about the actual word that we are getting and do not care about case. In other words, the words "The" and
    # # "the" will be counted as the same 2) it will remove punctuation marks as we are utilizing spaces as the delimiter.
    # # We would not want to count "dog" and "dog," as separate things 3) There are other markup language pieces that we
    # # would want to clean up, such as \n, etc.
def clean_text(text: str) -> list[str]:
    if text == '':
        return []

    text = text.lower()

    char_to_replace = ['!', '.', ',', '?', ')', '(', '\n', '*', '"', '#', '/', '_']

    for cur_char in char_to_replace:
        text = text.replace(cur_char, ' ')

    result = [t.strip() for t in text.split()]

    return result


class DocumentParser:

    def __init__(self):
        self.text_counts = {}

    def parse_text(self, text: str) -> dict:
        if text not in self.text_counts:
            self.add_text(text)

        return self.text_counts.get(text, [])

    def add_text(self, text:str) -> None:
        freq_dict = {}

        text_list = clean_text(text)

        for item in text_list:
            if item != ' ' and item != '' and item != "'" and item != '"':
                freq_dict[item] = freq_dict.get(item, 0) + 1

        self.text_counts[text] = freq_dict

