import argparse
import re
import chardet
from os.path import exists
from collections import Counter


def create_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filepath', required=True)
    parser.add_argument('-m', '--most_common', default=10)
    return parser


def check_arguments(parser, args):
    if not exists(args.filepath):
        parser.error('File not found.')
    if not isinstance(args.most_common, int):
        parser.error('Integer expected')


def define_file_encoding(filepath):
    with open(filepath, 'rb') as raw_filecontent:
        return chardet.detect(raw_filecontent.read()).get('encoding')


def load_raw_content(filepath, encoding):
    with open(filepath, mode='r', encoding=encoding) as raw_content:
        return raw_content.read()


def strip_punctuation_and_digits(raw_content):
    stripped_text = re.sub(r'\d+', '', (re.sub(r'[^\w\s]', '', raw_content)))
    separated_words_list = re.findall(r'\w+', stripped_text)
    return separated_words_list


def count_most_common(separated_words_list, most_common_count):
    return Counter(separated_words_list).most_common(most_common_count)


def print_summary(counted_words):
    print("\nMost common words in text - descending order.\n")
    for number, word in enumerate(counted_words, start=1):
            print('{}. "{}" - {} inclusions'.format(
                number,
                word[0].capitalize(),
                word[1]))


def main():
    parser = create_args_parser()
    args = parser.parse_args()
    check_arguments(parser, args)
    file_encoding = define_file_encoding(args.filepath)
    raw_data = load_raw_content(args.filepath, file_encoding)
    prepared_data = strip_punctuation_and_digits(raw_data)
    counted_words = count_most_common(prepared_data, arguments.most_common)
    print_summary(counted_words)


if __name__ == '__main__':
    main()
