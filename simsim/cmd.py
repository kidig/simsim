import operator
from argparse import ArgumentParser

from simsim import compare


def main():
    def get_file(value):
        return open(value, 'r')

    parser = ArgumentParser()
    parser.add_argument('file', type=get_file, nargs=2)

    args = parser.parse_args()
    file_a, file_b = [f for f in args.file]
    result = compare(file_a.read(), file_b.read())
    print('Similarity: {:.2f}'.format(result.get('ratio', 0)))

    for n, s in result.get('scopes', {}).items():
        label = f'\n{file_a.name}:{n}'
        print(label)
        print('-'*(len(label)-1))
        for func, sim in sorted(s, key=operator.itemgetter(1), reverse=True):
            print(f'{file_b.name}:{func}: {sim:.2f}')


if __name__ == '__main__':
    main()
