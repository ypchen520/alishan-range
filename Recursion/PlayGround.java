public class PlayGround{
    public static void main(String[] args){
        System.out.println("Hello world");
        char[] charArray = new char[]{'H','e','l','l','o'};
        // printReverse(charArray);
        System.out.println(calculatePascalsTriangle(100, 4));
    }

    private static int calculatePascalsTriangle(int r, int c){
        if(c > r) return -1;
        return helper(r,c);
    }

    private static int helper(int r, int c){
        if(c == 1 || r == c) return 1;
        return helper(r-1, c-1) + helper(r-1, c);
    }

    // private static void printReverse(char[] str){
    //     helper(0,str);
    // }
    // private static void helper(int index, char[] str){
    //     if(str == null || index >= str.length){
    //         return;
    //     }
    //     helper(index + 1, str);
    //     System.out.println(str[index]);
    // }
}
