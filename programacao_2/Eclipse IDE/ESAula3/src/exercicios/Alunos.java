package exercicios;

public class Alunos {
	private String nome;
	private String cpf;
	private int idade;
	private int serie;
	
	public Alunos(String nome, String cpf, int idade, int serie) {
		this.nome = nome;
		this.cpf = cpf;
		this.idade = idade;
		this.serie = serie;
	}
	
	public String getNome() {
		return nome;
	}
	
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public String getCpf() {
		return cpf;
	}
	
	public void setCpf(String cpf) {
		this.cpf = cpf;
	}
	
	public int getIdade() {
		return idade;
	}
	
	public void setIdade(int idade) {
		this.idade = idade;
	}
	
	public int getSerie() {
		return serie;
	}
	
	public void setSerie(int serie) {
		this.serie = serie;
	}
	
	public void atualizarDados(String nome, String cpf, int idade, int serie) {
		this.nome = nome;
		this.cpf = cpf;
		this.idade = idade;
		this.serie = serie;
	}
	
	//Method overload
	
	public void atualizarDados(String nome, String cpf) {
		this.nome = nome;
		this.cpf = cpf;
	}
	
	public void atualizarDados(int serie) {
		this.serie = serie;
	}
}
