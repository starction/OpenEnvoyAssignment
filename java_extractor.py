import re

from base_extractor import BaseExtractor


class JavaExtractor(BaseExtractor):

    def is_single_line_comment(self, line):
        return re.compile(r'//.*$').match(line) or re.compile(r'^/\*(.*)\*/$').match(line.strip())

    def has_multiline_comment_start(self, line):
        if re.compile(r'/\*(.*)\*/.*$').match(line):
            return False
        return re.compile(r'/\*(.*)$').match(line)

    def has_multiline_comment_end(self, line):
        return re.compile(r'(.*?)\*/$').match(line)
