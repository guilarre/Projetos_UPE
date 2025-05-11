package exercicios;

// Classe
public class Carro {
	private String marcaModelo;
	private int ano;
	private float valor;
	
	/*
	//Construtor gerado pelo Eclipse (source > generate constructor using fields...)
	public Carro(String marcaModelo, int ano, float valor) {
		super();
		this.marcaModelo = marcaModelo;
		this.ano = ano;
		this.valor = valor;
	}	
	*/
	
	/*
	// Construtor padrão
	public Carro() {
		this.marcaModelo = "Hyundai Hb20 Branco";
		this.ano = 2015;
		this.valor = 35000f;
	}
	*/
	
	// Construtor parametrizado
	public Carro(String marcaModelo, int ano, float valor) {
		this.marcaModelo = marcaModelo;
		this.ano = ano;
		this.valor = valor;
	}
	
	// Getters e Setters
	public String getMarcaModelo() {
		return marcaModelo;
	}
	
	public void setMarcaModelo(String marcaModelo) {
		this.marcaModelo = marcaModelo;
	}
	
	public int getAno() {
		return ano;
	}
	
	public void setAno(int ano) {
		this.ano = ano;
	}
	
	public float getValor() {
		return valor;
	}
	
	public void setValor(float valor) {
		this.valor = valor;
	}
	
	public void buzinar() {
		System.out.println("Pibitiiiiii");
	}
	
	public void buzinar(boolean volume) {
		if(volume == true) {
			System.out.println("PIBITIIIIIIIIIIIIIIIIIII");
		}
	}
	
}
