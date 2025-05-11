package aula;

public class Cachorro extends Animal {
	private String raca;
	
	public Cachorro(String nome, String raca) {
		super(nome);
		this.raca = raca;
	}

	public String getRaca() {
		return raca;
	}

	public void setRaca(String raca) {
		this.raca = raca;
	}
	
	@Override
	public void som() {
		System.out.println("Auuuuuuuu");
	}
	
	@Override
	public String toString() {
		return String.format("O nome do cachorro é %s da raça %s", getNome(), getRaca());
	}
	
}
