package aula;

public class CalculadoraAula {
	public static int operacoesRealizadas;
	
	public static String multiplicar(double num1, double num2) {
		operacoesRealizadas++;
		return String.format("O resultado é: %f", num1 * num2);
	}
	
	public static void main(String[] args) {
		// static faz com que algo seja atributo/método/bloco da CLASSE, o que permite não precisar criar um objeto Calculadora para executar os métodos:
		System.out.println(CalculadoraAula.multiplicar(3, 3));
		System.out.println(CalculadoraAula.multiplicar(3, 9));
		System.out.println(CalculadoraAula.operacoesRealizadas);
	}
}
