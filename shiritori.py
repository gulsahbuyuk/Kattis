"""
Author : Gülşah Büyük
Date : 6.08.2020
"""
def main() :
    used_words, last = set(), ''
    vocab = int(input())
    for i in range(vocab):
        word = input()
        if last and (word[0] != last[-1] or word in used_words):
            print(f'Player {2 - (i + 1) % 2} lost')
            return

        else:
            last= word
            used_words.add(word)
    print('Fair Game')

if  __name__ == '__main__':
    main()










