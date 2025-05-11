package aula;

public class PessoaTeste {

	public static void main(String[] args) {
		Aluno aluno1 = new Aluno("Lusga", 19, "123456", "Eng. Software");
		Funcionario funcionario1 = new Funcionario("Émerson", 33, "Professor", 15000);
		
		System.out.println(aluno1.getNome() + " " + aluno1.getIdade() + " " + aluno1.getMatricula() + " " + aluno1.getCurso());
		System.out.println(funcionario1.getNome() + " " + funcionario1.getIdade() + " " + funcionario1.getCargo() + " " + funcionario1.getSalario());
		System.out.println("\n###################\n");
		System.out.println(aluno1.toString());
		System.out.println("\n###################\n");
		System.out.println(funcionario1.toString());
	}

}
