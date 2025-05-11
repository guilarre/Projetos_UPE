package exercicioAula;
import java.util.ArrayList;

public class Professor extends Pessoa {
	public double salario;
	private static ArrayList<Professor> professores = new ArrayList<>();
	
	public Professor(String nome, String cpf, int idade, double salario) {
		super(nome, cpf, idade);
		this.salario = salario;
		professores.add(this);
	}
	
	public double getSalario() {
		return salario;
	}
	public void setSalario(double salario) {
		this.salario = salario;
	}
	
	public void deleteProfessor(String cpf) {
		for (int i = 0; i < professores.size(); i++) {
			if (this.cpf == cpf) {
				professores.remove(i);
				System.out.println("Professor deletado!");
			}
			else {
				System.out.println("ERRO: Professor não encontrado!");
			}
		}
	}
	
	@Override
	public String toString() {
		return String.format("Professor: %s;\nCpf: %s;\nIdade: %d;\nSalário: %s.\n", getNome(), getCpf(), getIdade(), getSalario());
	}
	
	public void listarProfessores() {
		for (Professor p : professores) {
			System.out.println(p);
		}
	}
}
