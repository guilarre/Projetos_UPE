package aula;
/*import aula.Pessoa;*/ //redundante pq a classe Pessoa já tá visível por ser public

public class TestarClasse {

	public static void main(String[] args) {
		// Teste Pessoa
		/*Pessoa jose;
		jose = new Pessoa();
		
		jose.altura = 1.5;
		jose.nome = "José da Silva Sauro";
		jose.idade = 27;
		jose.cabelo = false;
		
		jose.comer();
		jose.gritarPraCaramba();
		
		Pessoa maria = new Pessoa();
		
		maria.altura = 1.9;
		maria.nome = "Maria José";
		maria.idade = 15;
		maria.cabelo = false;
		
		maria.comer();
		maria.gritarPraCaramba();
		System.out.println(maria.dobrar(23));*/
		
		// Teste Conta
		/*Conta conta1;
		conta1 = new Conta();
		
		conta1.cpf = "123.456.789-10";
		conta1.nome = "José da Silva Sauro";
		conta1.saldo = 1000000000;
		
		System.out.println("A conta de " + conta1.nome + ", de CPF número " + conta1.cpf + ", possui saldo de: " + conta1.saldo + ".");*/
		
		// Teste Alunos
		/*Alunos aluno1 = new Alunos();
		
		aluno1.nome = "Lusga";
		aluno1.cpf = "111.222.333-44";
		aluno1.idade = 19;
		aluno1.serie = "2º período";
		
		System.out.println("O aluno de nome " + aluno1.nome + ", de CPF " + aluno1.cpf + " tem " + aluno1.idade + " anos de idade e está atualmente no " + aluno1.serie + ".");
		
		aluno1.reclamar();*/
		
		// Teste Automovel
		Automovel carro1 = new Automovel();
		
		carro1.marcaModelo = "Honda Fit";
		carro1.tipo = "Hatchback";
		carro1.valor = 52000;
		carro1.consumo = "15km/l";
		
		System.out.println("O carro " + carro1.marcaModelo + " de tipo " + carro1.tipo + " e preço R$" + carro1.valor + " faz " + carro1.consumo + ".");
		carro1.buzinar();
	}

}
