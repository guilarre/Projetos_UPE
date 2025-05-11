package aula;

public class Aluno extends Pessoa {
	private String matricula;
	private String curso;
	
	public Aluno(String nome, int idade, String matricula, String curso) {
		super(nome, idade);
		this.matricula = matricula;
		this.curso = curso;
	}

	public String getMatricula() {
		return matricula;
	}

	public void setMatricula(String matricula) {
		this.matricula = matricula;
	}

	public String getCurso() {
		return curso;
	}

	public void setCurso(String curso) {
		this.curso = curso;
	}
	
	@Override
	public String toString() {
		return String.format("O aluno %s, que tem %d anos de idade e matrícula %s, está no curso de %s.", this.getNome(), this.getIdade(), this.getMatricula(), this.getCurso());
	}
	
}
