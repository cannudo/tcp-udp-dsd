package br.edu.ifrn.conta.domain;

import java.io.Serializable;
import java.math.BigDecimal;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.ForeignKey;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.SequenceGenerator;
import java.util.Comparator;

import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.experimental.SuperBuilder;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

/**
 * Valor Inicial do Dono na Conta Patrimonio entity.
 */
@Getter
@Setter
@ToString
@EqualsAndHashCode(of = {"valorInicial", "dono", "contaPatrimonio"})
@SuperBuilder
@Entity
@SequenceGenerator(sequenceName = "seq_valorInicial", name = "ID_SEQUENCE", allocationSize = 1)
@NoArgsConstructor(access = AccessLevel.PRIVATE)
@AllArgsConstructor(access = AccessLevel.PRIVATE)
public class ValorInicialDoDonoNaContaPatrimonio implements Serializable, Comparable<ValorInicialDoDonoNaContaPatrimonio> {

    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "ID_SEQUENCE")
    private Long id;

    @Column(nullable = false)
    private BigDecimal valorInicial;

    @ManyToOne
    @JoinColumn(nullable = false, foreignKey = @ForeignKey(name = "fk_valorInicial_dono"))
    private Dono dono;

    @ManyToOne
    @JoinColumn(nullable = false, foreignKey = @ForeignKey(name = "fk_valorInicial_contaPatrimonio"))
    private ContaPatrimonio contaPatrimonio;

    @Override
    public int compareTo(ValorInicialDoDonoNaContaPatrimonio o) {
        return Comparator.comparing(ValorInicialDoDonoNaContaPatrimonio::getValorInicial)
                .thenComparing(ValorInicialDoDonoNaContaPatrimonio::getDono)
                .thenComparing(ValorInicialDoDonoNaContaPatrimonio::getContaPatrimonio)
                .compare(this, o);
    }

}
