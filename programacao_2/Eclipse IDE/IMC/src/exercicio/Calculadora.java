package exercicio;

import java.util.Scanner;

public class Calculadora {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		
		System.out.println("1 - Adição");
		System.out.println("2 - Subtração");
		System.out.println("Digite a opção desejada: ");
		
		int opcao = keyboard.nextInt();
		
		System.out.println("Digite o primeiro número: ");
		int num1 = keyboard.nextInt();
		
		System.out.println("Digite o segundo número: ");
		int num2 = keyboard.nextInt();
		keyboard.close();
		
		if(opcao == 1) {
			System.out.println("O resultado da adição é: " + (num1+num2));
		}
		else if(opcao == 2) {
			System.out.println("O resultado da subtração é: " + (num1-num2));
		}
	}

}
