import re

from base_extractor import BaseExtractor


class PythonExtractor(BaseExtractor):

    def __init__(self):
        super().__init__()
        self.multi_line_start = None

    def is_single_line_comment(self, line):
        return re.compile(r'#.*$').match(line) or re.compile(r'^""".*"""$').match(line.strip())

    def has_multiline_comment_start(self, line):
        if re.compile(r'"""(.*)$').match(line):
            self.multi_line_start = '"'
            return True
        elif re.compile(r"'''(.*)$").match(line):
            self.multi_line_start = "'"
            return True
        return False

    def has_multiline_comment_end(self, line):
        if self.multi_line_start == '"':
            return re.compile(r'(.*?)"""$').match(line)
        elif self.multi_line_start == "'":
            return re.compile(r"(.*?)'''$").match(line)
        return False
