def get_word_count(text):
    words = text.split()
    count = len(words)
    return count

def get_character_count(text):
    words = text.split()
    letter_count = {}
    report_list = []
    for word in words:
        for letter in word:
            lower_letter = letter.lower()
            if lower_letter not in letter_count:
                letter_count[lower_letter] = 1
            else:
                letter_count[lower_letter] += 1
    for letter, num in letter_count.items():
        letter_stats = {}
        letter_stats["char"] = letter
        letter_stats["num"] = num
        report_list.append(letter_stats)


    return report_list
