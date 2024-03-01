import sys
from pathlib import Path

from java_extractor import JavaExtractor
from python_extractor import PythonExtractor

"""
Configuration of Extractor class for each file extensions
using Java extractor for extensions '.js, .c, .cpp' as present functionality is same. 
New classes can be extended during future developments
"""
config = {
    '.py': PythonExtractor,
    '.java': JavaExtractor,
    '.js': JavaExtractor,
    '.c': JavaExtractor,
    '.cpp': JavaExtractor,
}


def count_code_lines(file_path):
    file_ext = Path(file_path).suffix.lower()
    parser = config[file_ext]()
    return parser.parse_source(file_path)


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python code_lines_counter.py <file_path>")
        sys.exit(1)

    # Get file input from the args
    file_path = sys.argv[1]
    result = count_code_lines(file_path)
    for k, v in result.items():
        print(k, v)
