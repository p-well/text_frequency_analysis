import argparse
import re
import chardet
from os.path import exists
from collections import Counter


def create_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filepath', required=True)
    parser.add_argument('-t', '--top_numb', default=10)
    return parser


def check_args(parser, args):
    if not exists(args.filepath):
        parser.error('File not found.')
    if not args.top_numb.isdigit():
        parser.error('Integer expected.')


def define_file_encoding(filepath):
    with open(filepath, 'rb') as raw_content:
        return chardet.detect(raw_content.read()).get('encoding')


def load_raw_content(filepath, encoding):
    with open(filepath, mode='r', encoding=encoding) as raw_content:
        return raw_content.read()


def strip_punctuation_and_digits(loaded_content):
    stripped_text = re.sub(r'\d+',
                           '',
                           (re.sub(r'[^\w\s]', '', loaded_content)))
    separated_words_list = re.findall(r'\w+', stripped_text)
    return separated_words_list


def count_most_common(separated_words_list, top_numb):
    return Counter(separated_words_list).most_common(top_numb)


def print_summary(most_common_words_data):
    print("\nMost common words in text - descending order.\n")
    for number, word in enumerate(most_common_words_data, start=1):
            print('{}. "{}" - {} inclusions'.format(
                number,
                word[0].capitalize(),
                word[1]))


def main():
    parser = create_args_parser()
    args = parser.parse_args()
    check_args(parser, args)
    file_encoding = define_file_encoding(args.filepath)
    raw_data = load_raw_content(args.filepath, file_encoding)
    prepared_data = strip_punctuation_and_digits(raw_data)
    most_common_words_data = count_most_common(prepared_data,
                                               int(args.top_numb))
    print_summary(most_common_words_data)


if __name__ == '__main__':
    main()
