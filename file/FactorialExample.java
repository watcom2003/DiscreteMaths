public class FactorialExample{  
 public static long factorialLoop(int n) {
     long res = 1;
     if (n>1)
        for (int i=2;i<=n;i++) res *= i;
    return res;
 }    
 public static long factorialRecursive(int n) {
     if (n==1) return 1; /*basis case*/
     else return n * factorialRecursive(n-1); /*recursive case*/
 }
    
 public static void main(String args[]){  
  int number = 5;
  System.out.println("Factorial(Loop) of "+number+" is: "+factorialLoop(number));    
  try {
    System.out.println("Factorial(Recursive) of "+number+" is: "+factorialRecursive(number));
  }
  catch(Exception error) {
    System.out.println(error.getMessage());
  }
}
}  
