package aula;

public class TestePolimorfismo {

	public static void main(String[] args) {
		Animal meuAnimal = new Cachorro();
		meuAnimal.fazerSom();
		meuAnimal = new Gato();
		meuAnimal.fazerSom();
		
	}

}
