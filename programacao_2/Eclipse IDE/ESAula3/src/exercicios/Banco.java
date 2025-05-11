package exercicios;

public class Banco {

	public static void main(String[] args) {
		/*System.out.println("##################");
		System.out.println("\n[c] - ");
		System.out.println("##################");
		*/
		
		System.out.println("Criando conta...");
		Conta conta1 = new Conta("123.321.123-33", "Ugu");
		
		System.out.println("Conta criada com sucesso!");
		System.out.println(conta1.getNome() + ", a sua conta de CPF número " + conta1.getCpf() + " possui o saldo de: R$" + conta1.consultar());
		
		System.out.println("Realizando um depósito...");
		conta1.depositar(20f);
		System.out.println("Você possui o saldo de: R$" + conta1.consultar());
		System.out.println("Realizando um saque...");
		conta1.sacar(12f);
		System.out.println("Você possui o saldo de: R$" + conta1.consultar());
		System.out.println("Você é pobre :(");
	}

}
