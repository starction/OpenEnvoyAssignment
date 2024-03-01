class BaseExtractor:

    def __init__(self):
        self.blank_lines = 0
        self.comment_lines = 0
        self.code_lines = 0
        self.total_lines = 0

    def is_blank_line(self, line):
        return len(line) == 0

    def is_single_line_comment(self, line):
        raise NotImplementedError()

    def has_multiline_comment_start(self, line):
        return False

    def has_multiline_comment_end(self, line):
        return False

    def parse_source(self, file_path:str) -> dict:
        try:
            with open(file_path, 'r') as file:
                multiline_comment_detected = False
                for line in file:
                    line = line.strip()
                    if multiline_comment_detected:
                        self.comment_lines += 1
                        # multiline comment is considered as ended once the ending syntax is encountered
                        multiline_comment_detected = not self.has_multiline_comment_end(line)
                    else:
                        if self.is_blank_line(line):
                            self.blank_lines += 1
                        elif self.is_single_line_comment(line):
                            self.comment_lines += 1
                        elif self.has_multiline_comment_start(line):
                            self.comment_lines += 1
                            # if not self.has_multiline_comment_end(line):
                            multiline_comment_detected = True
                        else:
                            self.code_lines += 1
                    self.total_lines += 1
                return {'Blank': self.blank_lines, 'Comments': self.comment_lines, 'Code': self.code_lines,
                        'Total': self.total_lines}
        except FileNotFoundError:
            return f"Error: File '{file_path}' not found."
        except Exception as e:
            return f"Error: {e}"
