package exercicioAula;
import java.util.ArrayList;

public class Aluno extends Pessoa {
	public String matricula;
	private static ArrayList<Aluno> alunos = new ArrayList<>();

	public Aluno(String nome, String cpf, int idade, String matricula) {
		super(nome, cpf, idade);
		this.matricula = matricula;
		alunos.add(this);
	}
	
	public String getMatricula() {
		return matricula;
	}
	public void setMatricula(String matricula) {
		this.matricula = matricula;
	}
	
	public void deleteAluno(String cpf) {
		for (int i = 0; i < alunos.size(); i++) {
			if (this.cpf == cpf) {
				alunos.remove(i);
				System.out.println("Aluno deletado!");
			}
			else {
				System.out.println("ERRO: Aluno não encontrado!");
			}
		}
	}
	
	@Override
	public String toString() {
		return String.format("Aluno: %s;\nCpf: %s;\nIdade: %d;\nMatrícula: %s.\n", getNome(), getCpf(), getIdade(), getMatricula());
	}
	
	public void listarAlunos() {
		for (Aluno a : alunos) {
			System.out.println(a);
		}
	}
}