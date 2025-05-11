package aula;

public class Calculadora {
	public static void somar(double num1, double num2) {
		System.out.println(num1 + num2);
	}
	
	public static void somar(double num1, double num2, double num3) {
		System.out.println(num1 + num2 + num3);
	}
	
	public static void subtrair(double num1, double num2) {
		System.out.println(num1 - num2);
	}
	
	public static void subtrair(double num1, double num2, double num3) {
		System.out.println(num1 - num2 - num3);
	}
	
	public static void main(String args[]) {
		Calculadora.somar(1, 29);
		Calculadora.somar(1, 29, 1);
	}
}
