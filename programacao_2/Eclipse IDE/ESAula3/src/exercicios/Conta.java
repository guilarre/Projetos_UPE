package exercicios;

public class Conta {
	private String cpf;
	private String nome;
	private float saldo;
	
	public Conta(String cpf, String nome) {
		this.cpf = cpf;
		this.nome = nome;
		this.saldo = 0f;
	}
	
	public String getCpf() {
		return cpf;
	}
	
	public void setCpf(String cpf) {
		this.cpf = cpf;
	}
	
	public String getNome() {
		return nome;
	}
	
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public void sacar(float valor) {
		this.saldo -= valor;
	}
	
	public void depositar(float valor) {
		this.saldo += valor;
	}
	
	public float consultar() {
		return saldo;
	}
	
}
