import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt(); // Number of test cases

        for (int t = 0; t < T; t++) {
            int n = scanner.nextInt(); // Length of the array
            int[] A = new int[n]; // Array elements

            for (int i = 0; i < n; i++) {
                A[i] = scanner.nextInt();
            }

            int[] result = findNextGreaterElements(A);
            for (int i = 0; i < n; i++) {
                System.out.print(result[i] + " ");
            }
            System.out.println();
        }
    }

    public static int[] findNextGreaterElements(int[] A) {
        int n = A.length;
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>();

        // Iterate through the array from right to left
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && A[i] >= stack.peek()) {
                stack.pop();
            }

            if (!stack.isEmpty()) {
                result[i] = stack.peek();
            } else {
                result[i] = -1;
            }

            stack.push(A[i]);
        }

        return result;
    }
}
