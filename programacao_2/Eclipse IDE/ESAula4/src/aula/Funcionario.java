package aula;

public class Funcionario extends Pessoa {
	private String cargo;
	private double salario;
	
	public Funcionario(String nome, int idade, String cargo, double salario) {
		super(nome, idade);
		this.cargo = cargo;
		this.salario = salario;
	}

	public String getCargo() {
		return cargo;
	}

	public void setCargo(String cargo) {
		this.cargo = cargo;
	}

	public double getSalario() {
		return salario;
	}

	public void setSalario(double salario) {
		this.salario = salario;
	}
	
	@Override
	public String toString() {
		return String.format("O funcionário %s, que tem %d anos de idade e cargo de %s, recebe %f por mês.", this.getNome(), this.getIdade(), this.getCargo(), this.getSalario());
	}
	
}
