import java.util.Scanner;

public class print_transpose {
    static Scanner sc = new Scanner(System.in);
    void print_matrix(char[][] matrix){
        for (char[] C: matrix){
            for (char c: C){
                System.out.print(c + "\t");
            }
            System.out.println();
        }
    }

    void print_matrix(char[][] matrix, int r, int c){
        for (int i=0; i<c; i++){
            for (int j=0; j<r; j++){
                if (i<matrix[j].length)
                    System.out.print(matrix[j][i] + "  ");
                else
                    System.out.print("    ");
            }
            System.out.println();
        }
    }
    int find_longestWord(String sentence){
        int max_len = 0;
        for (String word : sentence.split(" ")) {
            if (word.length() > max_len) {
                max_len = word.length();
            }
        }
        return max_len;
    }

    char[][] str_to_matrix(String sentence, char[][] matrix){
        int row=0, col=0;
        for (String word : sentence.split(" ")){
            col = 0;
            for (char c : word.toCharArray()){
                matrix[row][col] = c;
                col++;
            }
            row ++;
        }
        return matrix;
    }

    public static void main(String[] args) {
        String ip_sent;
        System.out.print("Enter the input string:");
        ip_sent = sc.nextLine();
        print_transpose ob = new print_transpose();

        // STEP 1. Start creating the matrix

        int nr_words = ip_sent.split(" ").length;  // number of words in the input sentence
        int longest_word_len = ob.find_longestWord(ip_sent);
        System.out.printf("Longest word length: %d\n", longest_word_len);
        char[][] matrix = new char[nr_words][longest_word_len];
//        ob.print_matrix(matrix);
        matrix = ob.str_to_matrix(ip_sent, matrix);

        // STEP 2: Print the matrix in the transposed form
        ob.print_matrix(matrix, nr_words, longest_word_len);

        System.out.println("\n----------Done---------");
    }
}
