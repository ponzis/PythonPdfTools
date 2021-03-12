import argparse
from PyPDF2 import PdfFileWriter, PdfFileReader


def main(even, odd, out):
    print(even, odd, out)
    output = PdfFileWriter()
    inputeven = PdfFileReader(open(even, "rb"))
    inputodd = PdfFileReader(open(odd, "rb"))

    number_of_pages = inputeven.getNumPages()
    for i in range(number_of_pages):
        page_even = inputeven.getPage(i)
        page_odd = inputodd.getPage(i)

        output.addPage(page_even)
        output.addPage(page_odd)

    with open(out, "wb") as writer:
        output.write(writer)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('even', help='even pages')
    parser.add_argument('odd', help='odd pages')
    parser.add_argument('out', help='output')

    args = parser.parse_args()

    main(**vars(args))
