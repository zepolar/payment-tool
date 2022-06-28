import re
from abc import ABC, abstractmethod

from exception.file_exception import FormatError, EmptyError


class Format(ABC):

    @abstractmethod
    def validate(self, content):
        pass


class JsonFormat(Format):

    def validate(self, content):
        pass


class XmlFormat(Format):

    def validate(self, content):
        pass


class RegexFormat(Format):
    _fmt_regex = r"\w+=(((MO|TU|WE|TH|FR|SA|SU)\d\d:\d\d-\d\d:\d\d)[,|\n]+)+"

    def validate(self, lines):
        if not lines:
            raise EmptyError()
        else:
            pair = re.compile(self._fmt_regex)
            invalid = [line for line in lines if len(line) > 1 and not pair.fullmatch(line)]
            if len(invalid) > 0:
                raise FormatError("There exist a problem with the format in the file. Check out the follow lines",
                                  invalid)


class FormatFactory(ABC):

    @staticmethod
    def create(type_format):
        if type_format == "xml":
            return XmlFormat()
        elif type_format == "json":
            return JsonFormat()
        else:
            return RegexFormat()
