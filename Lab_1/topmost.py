import sys 
import urllib.request

import wordfreq


def main():
    st_file = sys.argv[1]
    in_file = sys.argv[2]
    n = int(sys.argv[3])

    with open(st_file, 'r', encoding='utf-8') as stop_file:
        stop_words = [word.strip() for word in stop_file]

    if 'http' in in_file: 
        response = urllib.request.urlopen(in_file)
        lines = response.read().decode('utf8').splitlines()

    else:
        with open(in_file, 'r', encoding='utf-8') as in_file:
            lines = [line.strip() for line in in_file]

    # print(lines)

    wordfreq.printTopMost(wordfreq.countWords(wordfreq.tokenize(lines), stop_words), n)


if __name__ == '__main__':
    main()