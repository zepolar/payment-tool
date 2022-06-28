import argparse

from files import FileFactory

if __name__ == "__main__":
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
    parser.add_argument("-i", "--input", help="Input file to process", required=True)
    parser.add_argument("-o", "--output", help="Result of file", required=True)
    parser.add_argument("-f", "--format", help="It is possible to use: regex, json, xml", required=True)

    args = parser.parse_args()
    file_output = args.output
    file_input = args.input
    file_format = args.format

    file_instance = FileFactory.create(file_format.lower())

    result = file_instance.read_file(file_input)

    file_instance.write_file(file_output, result)
