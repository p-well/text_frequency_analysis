import argparse
import re
import chardet


def create_arguments_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filepath')
    return parser


def define_file_encoding(filepath):
    with open(filepath, 'rb') as raw_filecontent:
        return chardet.detect(raw_filecontent.read()).get('encoding')


def load_data_from_file(filepath, encoding):
    with open(filepath, mode='r', encoding=encoding) as raw_filecontent:
        return raw_filecontent.read().split(' ')


# def load_data(loaded_text, encoding):
#     with open(loaded_text, encoding, mode='r') as text:
#         words_in_text = text.read().split(' ')
#     print(words_in_text)


def get_most_frequent_words(text):
    pass


if __name__ == '__main__':
    arguments = create_arguments_parser().parse_args()
    file_encoding = define_file_encoding(arguments.filepath)
    print(file_encoding)
    loaded_text = load_data_from_file(arguments.filepath, file_encoding)
    print(loaded_text)
