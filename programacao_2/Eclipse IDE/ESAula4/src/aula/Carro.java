package aula;

public class Carro extends Veiculo {
	private int numeroDePortas;

	public Carro(String marca, String modelo, int ano, int numeroDePortas) {
		super(marca, modelo, ano);
		this.numeroDePortas = numeroDePortas;
	}
	
	public int getNumeroDePortas() {
		return numeroDePortas;
	}

	public void setNumeroDePortas(int numeroDePortas) {
		this.numeroDePortas = numeroDePortas;
	}
	
	public void abrirPorta() {
		System.out.println("Inheeeeen");
	}
	
	@Override
	public String toString() {
		return String.format("Marca: %s\nModelo: %s\nAno: %d\nTipo de Guidão: %s", this.getMarca(), this.getModelo(), this.getAno(), this.getNumeroDePortas());
	}
}
