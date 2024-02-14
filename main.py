import re


def replace_spam_words(text, spam_words):
    for word in spam_words:
        print(text)
        text = re.sub(word, "*" * len(word), text, flags=re.IGNORECASE)
        print(text)
    return text
