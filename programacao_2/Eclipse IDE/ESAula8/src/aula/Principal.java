package aula;

public class Principal {

	public static void main(String[] args) {
//		Cachorro dog = new Cachorro();
//		dog.dormir();
//		dog.som();
//		
//		Caramelo caramelow = new Caramelo();
//		caramelow.carinho();
		
		Explorador exp = new Explorador();
		exp.coordenadas("norte");
		exp.movimento();
		exp.pontos();
	}
}