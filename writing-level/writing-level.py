def get_grade():
    text = input("Text: ")
    sentence_count = len([i for i in text if i in ['.', '?', '!']])
    word_count = len(text.split(' '))
    letter_count = len([i for i in text if i.isalpha()])
    L = (letter_count / word_count) * 100
    S = (sentence_count / word_count) * 100
    grade = round(0.0588 * L - 0.296 * S - 15.8)
    if 1 <= grade < 16:
        print(f'Grade {grade}')
    elif grade < 1:
        print('Before Grade 1')
    else:
        print('Grade 16+')

get_grade()