package exercicios;

public class InvestimentoTeste {
    public static void main(String[] args) {
        Investimento investimento = new Investimento(0.1f, 10000.0f, 5);

        System.out.println("Valor investido: " + investimento.getValor() + "\nTaxa de juros: " + investimento.getTaxaDeJuros() + "\nTempo de investimento: " + investimento.getTempoEmAnos());

        System.out.println(investimento.retornarRendimento());

        investimento.setValor(20000.0f);
        investimento.setTaxaDeJuros(0.15f);
        investimento.setTempoEmAnos(10);

        System.out.println("Valor investido: " + investimento.getValor() + "\nTaxa de juros: " + investimento.getTaxaDeJuros() + "\nTempo de investimento: " + investimento.getTempoEmAnos());

        System.out.println(investimento.retornarRendimento());
    }
}
