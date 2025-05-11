package aula;

public class Cachorro extends Animal {
	// Somos forçados a implementar o método abstrato
	// O método concreto é herdado
	public void som() {
		System.out.println("Au au au au!");
	}
}