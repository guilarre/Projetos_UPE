package aula;

public class TesteVeiculo {

	public static void main(String[] args) {
		Carro carro1 = new Carro("Fiat", "Uno Mille", 2005, 2);
		System.out.println(carro1.toString());
		System.out.println("\n");
		
		Motocicleta motocicleta1 = new Motocicleta("Honda", "Pop 125", 2020, "Tronxo");
		System.out.println(motocicleta1.toString());
	}

}
