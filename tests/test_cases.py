import os
import sys
import unittest

from code_lines_counter import count_code_lines

script_directory = os.path.dirname(os.path.realpath(sys.argv[0]))


class TestMultilineCommentIdentification(unittest.TestCase):

    def test_java_file(self):
        java_file_path = f'{script_directory}/source.java'

        # Find all blanks, comments and code lines in the Java file
        source_summary = count_code_lines(java_file_path)

        # Assert that the multiline comment was correctly identified
        self.assertEqual(source_summary['Blank'], 6)
        self.assertEqual(source_summary['Comments'], 21)
        self.assertEqual(source_summary['Code'], 13)
        self.assertEqual(source_summary['Total'], 40)

    def test_python_file(self):
        java_file_path = f'{script_directory}/source.py'

        # Find all blanks, comments and code lines in the Java file
        source_summary = count_code_lines(java_file_path)

        # Assert that the multiline comment was correctly identified
        self.assertEqual(source_summary['Blank'], 11)
        self.assertEqual(source_summary['Comments'], 17)
        self.assertEqual(source_summary['Code'], 12)
        self.assertEqual(source_summary['Total'], 40)


if __name__ == '__main__':
    unittest.main()
