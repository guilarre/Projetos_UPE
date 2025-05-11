package exercicios;

public class AlunosTeste {

	public static void main(String[] args) {
		Alunos joana = new Alunos("Joana Maria", "111.222.333-44", 19, 4);
		System.out.println("Aluno(a): " + joana.getNome() + "\nCPF: " + joana.getCpf() + "\nIdade: " + joana.getIdade() + "\nSérie: " + joana.getSerie());
		
		joana.atualizarDados("juanna da silva sauro", "222.222.222-22");
		System.out.println("Aluno(a): " + joana.getNome() + "\nCPF: " + joana.getCpf() + "\nIdade: " + joana.getIdade() + "\nSérie: " + joana.getSerie());
	}
}
