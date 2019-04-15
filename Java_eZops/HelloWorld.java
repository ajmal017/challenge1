
class HelloWorld {
    public static void main(String[] args) {
        // exceptionForDividing();
        try {
            throw new RuntimeException("Throwing Exception!");
        } catch (RuntimeException ex) {
            ex.printStackTrace();
        }
    }
    public static int divideInts(int x, int y) {
        if (y == 0) {
            throw new IllegalArgumentException("Not Allowed! Dividing by Zero");
        }
        return x / y;
    }
    public static void exceptionForDividing() {
        System.out.println("Hello, World.");
        System.out.println("Now, let's do some division!\n");
        try{
            int ans = divideInts(100,10);
            System.out.format("100 divided by 10 is: %d%n \n", ans);
            System.out.println("100 divided by 0 is: \n\n");
            divideInts(100,0);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}