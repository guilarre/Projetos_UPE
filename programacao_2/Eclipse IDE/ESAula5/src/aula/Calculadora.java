package aula;
import java.util.Scanner;
import java.util.InputMismatchException;

public class Calculadora {
	//TO DO: tentar ajeitar erro do nextLine
	public static Scanner sc = new Scanner(System.in);
	public static String somar() {
		try {
			System.out.println("Digite o primeiro número: ");
			double num1 = Calculadora.sc.nextDouble();
			System.out.println("Digite o segundo número: ");
			double num2 = Calculadora.sc.nextDouble();
			return String.format("O resultado é: %.2f", num1 + num2);
		} catch (InputMismatchException e) {
			return "ERRO: digite apenas números!";
		}
	}
	
	public static String subtrair() {
		try {
			System.out.println("Digite o primeiro número: ");
			double num1 = Calculadora.sc.nextDouble();
			System.out.println("Digite o segundo número: ");
			double num2 = Calculadora.sc.nextDouble();
			return String.format("O resultado é: %.2f", num1 - num2);
		} catch (InputMismatchException e) {
			return "ERRO: digite apenas números!";
		}
	}
	
	public static String multiplicar() {
		try {
			System.out.println("Digite o primeiro número: ");
			double num1 = Calculadora.sc.nextDouble();
			System.out.println("Digite o segundo número: ");
			double num2 = Calculadora.sc.nextDouble();
		
			return String.format("O resultado é: %.2f", num1 * num2);	
		} catch (InputMismatchException e) {
			return "ERRO: digite apenas números!";
		}
	}

	public static String dividir() {
		try {
			System.out.println("Digite o primeiro número: ");
			double num1 = Calculadora.sc.nextDouble();
			System.out.println("Digite o segundo número: ");
			double num2 = Calculadora.sc.nextDouble();
			if (num2 != 0) {
				return String.format("O resultado é: %f", num1 / num2);
			}
			else {
				return "ERRO: divisão por 0.";
			}
		} catch (InputMismatchException e) {
			return "ERRO: digite apenas números!";
		}
	}
	
	public static String elevar() {
		try {
			System.out.println("Digite o número a ser elevado: ");
			double num = Calculadora.sc.nextDouble();
			System.out.println("Digite a potência: ");
			int potencia = Calculadora.sc.nextInt();
			double resultado = num;
			for (int i = 1; i < potencia; i++) {
				resultado = resultado * num;
			}
			return String.format("O resultado é: %.2f", resultado);	
		} catch (InputMismatchException e) {
			return "ERRO: digite apenas números!";
		}
	}
	
	public static double raizQuadrada(double num) {
		double t, raizQuadrada;
		raizQuadrada = num / 2;
		do {
			t = raizQuadrada;
			raizQuadrada = (t + (num / t)) / 2;
		} while ((t - raizQuadrada) != 0);
		return raizQuadrada;
	}

	public static String retornarRaizQuadrada() {
		try {
			System.out.println("Digite um número: ");
			double num = Calculadora.sc.nextDouble();
			return String.format("A raiz quadrada de %.2f é: %.2f", num, raizQuadrada(num));
		} catch (InputMismatchException e) {
			return "ERRO: digite apenas números!";
		}
	}
	
	public static String raizesEquacaoQuadratica() {
		try {
			System.out.println("Digite o primeiro coeficiente da equação (a): ");
			double a = Calculadora.sc.nextDouble();
			System.out.println("Digite o segundo coeficiente da equação (b): ");
			double b = Calculadora.sc.nextDouble();
			System.out.println("Digite o terceiro coeficiente da equação (c): ");
			double c = Calculadora.sc.nextDouble();
			double delta = b * b - 4 * a * c;
			double raizDelta = raizQuadrada(delta);
			double x1 = (-b + raizDelta) / (2 * a);
			double x2 = (-b - raizDelta) / (2 * a);
			return String.format("As raízes da equação são: %.2f e %.2f.", x1, x2);
		} catch (InputMismatchException e) {
			return "ERRO: digite apenas números!";
		}
	}

	public static String retornarFatorial() {
		try {
			System.out.println("Digite um número natural: ");
			int num1 = Calculadora.sc.nextInt();
			int num2 = num1;
			int resultado = num1;
			for (int i = 1; i < num1; i++) {
				num2 -= 1;
				resultado *= num2;
			}
			return String.format("O fatorial de %d é: %d.", num1, resultado);	
		} catch (InputMismatchException e) {
			return "ERRO: digite apenas números!";
		}
	}

	public static String retornarPorcentagem() {
		try {
			System.out.println("Digite o valor percentual (por ex., para 10%, você deve digitar '10'): ");
			double num1 = Calculadora.sc.nextDouble();
			System.out.println("Digite o valor de entrada: ");
			double num2 = Calculadora.sc.nextDouble();
			double decimal = num1 / 100;
			double resultado = num2 * decimal;
			return String.format("%.2f%% de %.2f é: %.2f.", num1, num2, resultado);
		} catch (InputMismatchException e) {
			return "ERRO: digite apenas números!";
		}
	}

	public static String retornarInverso() {
		try {
			System.out.println("Digite um número: ");
			double num = Calculadora.sc.nextDouble();
			if (num != 0) {
				double resultado = 1 / num;
				return String.format("O inverso de %f é %f", num, resultado);
			} 
			else {
				return "ERRO: Não existe inverso de 0.";
			}	
		} catch (InputMismatchException e) {
			return "ERRO: digite apenas números!";
		}
	}

	// Main
	public static void main(String[] args) {
		loop: while(true) {
			System.out.println("""
###########################################

Bem-vindo à calculadora.

Escolha a função desejada:

[+] = Somar
[-] = Subtrair
[*] = Multiplicar
[/] = Dividir
[**] = Elevar a uma potência
[r] = Calcular a raiz quadrada de um número
[e] = Resolver uma equação de 2º grau
[f] = Retornar o fatorial de um número
[p] = Calcular a porcentagem de um valor
[i] = Retornar o inverso de um número

[s] = Sair""");

			String opcao = Calculadora.sc.next();
			
			switch (opcao) {
				case "+":
					System.out.println(Calculadora.somar());
					break;
				case "-":
					System.out.println(Calculadora.subtrair());
					break;
				case "*":
					System.out.println(Calculadora.multiplicar());
					break;
				case "/":
					System.out.println(Calculadora.dividir());
					break;
				case "**":
					System.out.println(Calculadora.elevar());
					break;
				case "r":
					System.out.println(Calculadora.retornarRaizQuadrada());
					break;
				case "e":
					System.out.println(Calculadora.raizesEquacaoQuadratica());
					break;
				case "f":
					System.out.println(Calculadora.retornarFatorial());
					break;
				case "p":
					System.out.println(Calculadora.retornarPorcentagem());
					break;
				case "i":
					System.out.println(Calculadora.retornarInverso());
					break;
				case "s":
					System.out.println("Até mais!");
					sc.close();
					break loop;
			}
		}
	}
}
