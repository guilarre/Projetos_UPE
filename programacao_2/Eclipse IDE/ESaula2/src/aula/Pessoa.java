package aula;

public class Pessoa {
	String nome;
	int idade;
	double altura;
	boolean cabelo;
	
	void comer() {
		System.out.println("Nhac nhac");
	}
	void gritarPraCaramba() {
		System.out.println("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!");
	}
	String dobrar(double numero) {
		return ("Número dobrado: " + numero * 2);
	}
	
}
