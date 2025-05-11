package aula;

public class Animal {
	// protected para os atributos/métodos da classe pai (superclasse)
	protected String nome;
	
	protected Animal(String nome) {
		this.nome = nome;
	}
	
	protected String getNome() {
		return nome;
	}
	
	protected void setNome(String nome) {
		this.nome = nome;
	}
	
	public void som() {
		System.out.println("Barulho de despertador");
	}
}
