package br.edu.ifrn.conta;

import org.springframework.boot.builder.SpringApplicationBuilder;

/**
 * Main Class.
 */
public class ContaApplicationMain {

	protected ContaApplicationMain() {
	}

	public static void main(String[] args) {
		new SpringApplicationBuilder()
			.sources(ContaApplication.class)
			.run(args);
	}

}
