package aula;

public class Motocicleta extends Veiculo {
	private String tipoDeGuidao;
	
	public Motocicleta(String marca, String modelo, int ano, String tipoDeGuidao) {
		super(marca, modelo, ano);
		this.tipoDeGuidao = tipoDeGuidao;
	}
	
	public boolean empinar() {
		return true;
	}
	
	public String getTipoDeGuidao() {
		return tipoDeGuidao;
	}

	public void setTipoDeGuidao(String tipoDeGuidao) {
		this.tipoDeGuidao = tipoDeGuidao;
	}
	
	@Override
	public String toString() {
		return String.format("Marca: %s\nModelo: %s\nAno: %d\nTipo de Guidão: %s", this.getMarca(), this.getModelo(), this.getAno(), this.getTipoDeGuidao());
	}
}
