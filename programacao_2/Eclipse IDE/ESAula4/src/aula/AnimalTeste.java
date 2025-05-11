package aula;

public class AnimalTeste {

	public static void main(String[] args) {
		Cachorro dog1 = new Cachorro("Dobby", "Viralatinha");
		System.out.println(dog1.getNome() + " " + dog1.getRaca());

		dog1.setNome("Lusca");
		System.out.println(dog1.getNome() + " " + dog1.getRaca());
		dog1.som();
		System.out.println(dog1.toString());
	}
}
