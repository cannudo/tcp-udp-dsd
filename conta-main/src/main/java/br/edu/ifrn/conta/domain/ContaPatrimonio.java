package br.edu.ifrn.conta.domain;

import java.util.Set;

import jakarta.persistence.Entity;
import jakarta.persistence.OneToMany;

import lombok.AccessLevel;
import lombok.experimental.SuperBuilder;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.Singular;
import lombok.ToString;

/**
 * Conta Patrimonio entity.
 */
@SuperBuilder
@Getter
@Setter
@ToString(callSuper = true, exclude = "valoresIniciaisDosDonos")
@EqualsAndHashCode(callSuper = true, exclude = "valoresIniciaisDosDonos")
@Entity
@NoArgsConstructor(access = AccessLevel.PRIVATE)
public class ContaPatrimonio extends Conta {

    private static final long serialVersionUID = 1L;

    @Singular
    @OneToMany(mappedBy = "contaPatrimonio")
    private Set<ValorInicialDoDonoNaContaPatrimonio> valoresIniciaisDosDonos;

}
