"""
This is a multiline comment
spanning multiple lines.
'''-> This is not the end of multiline
"""
""""""


class Example:

    # This is a single-line comment
    def __init__(self, x):
        self.x = x  # This is an inline comment

    """
    Another multiline comment
    that contains more details.
    """

    def my_method(self):
        print("Hello, World!")

        # Inline comment within a method
        # TODO: Add more functionality here

    def add_numbers(self, a, b):
        # Blank line above
        return a + b

    # This is another single-line comment
    def main(self):
        example = Example(42)
        example.my_method()

        # Single-line comment at the end


# Create an instance of the class and call the main method
example_instance = Example(10)
example_instance.main()
