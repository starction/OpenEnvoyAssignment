/*
 * This is a multiline comment
 * spanning multiple lines.
 */
public class Example {

    // This is a single-line comment
    private int x; // This is an inline comment

    /*
     * Another multiline comment
     * that contains more details.
     */
    public void myMethod() {
        System.out.println("Hello, World!");

        // Inline comment within a method
        // TODO: Add more functionality here
    }

    /**
     * This method adds two numbers.
     *
     * @param a The first number
     * @param b The second number
     * @return The sum of a and b
     */
    public int addNumbers(int a, int b) {
        /* Blank line above*/
        return a + b;
    }

    // This is another single-line comment
    public static void main(String[] args) {
        Example example = new Example();
        example.myMethod();

        // Single-line comment at the end
    }
}
