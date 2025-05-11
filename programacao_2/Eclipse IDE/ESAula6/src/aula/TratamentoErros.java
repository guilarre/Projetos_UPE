package aula;

public class TratamentoErros {

	public static void main(String[] args) {
		try {
			double num1 = 13;
			double num2 = 0;
			double resultado = num1 / num2;
			System.out.println(resultado);
		} catch (ArithmeticException e) {
			System.out.println("ERRO: Divisão por zero.");
		} finally {
			System.out.println("vai tomar no cu");
		}

	}

}
