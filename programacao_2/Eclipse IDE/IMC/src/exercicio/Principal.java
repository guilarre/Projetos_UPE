package exercicio;

public class Principal {

	public static void main(String[] args) {
		double peso, altura, imc;
		
		peso = 80;
		altura = 1.73;
		
		imc = peso / (altura * altura);
		System.out.println(imc);
		
		if(imc < 18.5) {
			System.out.println("Magreza");
		}
		else if(imc >= 18.5 && imc < 24.9) {
			System.out.println("Peso normal");
		}
		else if(imc >= 24.9 && imc < 29.9) {
			System.out.println("Excesso de peso");
		}
		else {
			System.out.println("Obesidade Classe 1");
		}
	}

}
