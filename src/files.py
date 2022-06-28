from abc import ABC, abstractmethod
from os import path

from exception.file_exception import FileWriteError
from formats import RegexFormat
from utils.payment import total_pay_calculation


class File(ABC):

    @abstractmethod
    def read_file(self, filename):
        pass

    @abstractmethod
    def write_file(self, filename, content):
        pass


class RegexFile(File):

    def read_file(self, filename):
        if not filename:
            raise ValueError("Filename should not be empty")
        else:
            if not path.exists(filename):
                raise FileExistsError("Filename is not valid")
            else:
                regex_format = RegexFormat()
                with open(filename, mode="r") as reader:
                    try:
                        lines = [line for line in reader.readlines() if not line.isspace()]
                        regex_format.validate(lines)
                        return total_pay_calculation(lines)
                    finally:
                        reader.close()

    def write_file(self, filename, content):
        if not filename:
            raise ValueError("Filename should not be empty")
        else:
            if type(content) is dict:
                with open(filename, mode="w") as writer:
                    try:
                        writer.writelines(["{}={}\n".format(k, v) for k, v in content.items()])
                    finally:
                        writer.close()
            else:
                raise FileWriteError("A dict was expected")


class JsonFile(File):

    def write_file(self, filename, content):
        pass

    def read_file(self, filename):
        pass


class XmlFile(File):

    def read_file(self, filename):
        pass

    def write_file(self, filename, content):
        pass


class FileFactory(object):

    @staticmethod
    def create(format_file):
        if format_file == "xml":
            return XmlFile()
        elif format_file == "json":
            return JsonFile()
        else:
            return RegexFile()
