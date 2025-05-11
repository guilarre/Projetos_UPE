package exercicios;

public class Investimento {
    private float taxaDeJuros;
    private float valor;
    private int tempoEmAnos;

    public Investimento(float taxaDeJuros, float valor, int tempoEmAnos) {
        this.taxaDeJuros = taxaDeJuros;
        this.valor = valor;
        this.tempoEmAnos = tempoEmAnos;
    }

    public float getTaxaDeJuros() {
        return taxaDeJuros;
    }

    public void setTaxaDeJuros(float taxaDeJuros) {
        this.taxaDeJuros = taxaDeJuros;
    }

    public float getValor() {
        return valor;
    }

    public void setValor(float valor) {
        this.valor = valor;
    }

    public int getTempoEmAnos() {
        return tempoEmAnos;
    }

    public void setTempoEmAnos(int tempoEmAnos) {
        this.tempoEmAnos = tempoEmAnos;
    }
    
    public double retornarRendimento() {
        double valorComRendimento = valor * (Math.pow((1 + taxaDeJuros), tempoEmAnos));
        return valorComRendimento;
    }
}
