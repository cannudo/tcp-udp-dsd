package br.edu.ifrn.conta.domain;

import java.io.Serializable;
import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.Comparator;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.ForeignKey;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.SequenceGenerator;

import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.experimental.SuperBuilder;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

/**
 * Lancamento entity.
 */
@Getter
@Setter
@ToString
@EqualsAndHashCode(of = {"dono", "contaEntrada", "contaSaida", "valor", "data"})
@SuperBuilder
@Entity
@SequenceGenerator(sequenceName = "seq_lancamento", name = "ID_SEQUENCE", allocationSize = 1)
@NoArgsConstructor(access = AccessLevel.PRIVATE)
@AllArgsConstructor(access = AccessLevel.PRIVATE)
public class Lancamento implements Serializable, Comparable<Lancamento> {

    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "ID_SEQUENCE")
    private Long id;

    @ManyToOne
    @JoinColumn(nullable = false, foreignKey = @ForeignKey(name = "fk_lancamento_dono"))
    private Dono dono;

    @ManyToOne
    @JoinColumn(nullable = false, foreignKey = @ForeignKey(name = "fk_lancamento_contaEntrada"))
    private Conta contaEntrada;

    @ManyToOne
    @JoinColumn(nullable = false, foreignKey = @ForeignKey(name = "fk_lancamento_contaSaida"))
    private Conta contaSaida;

    @Column(nullable = false)
    private BigDecimal valor;

    @Column(nullable = false)
    private LocalDateTime data;

    private String descricao;

    @Override
    public int compareTo(Lancamento o) {
        return Comparator.comparing(Lancamento::getData)
                .thenComparing(Lancamento::getValor)
                .thenComparing(Lancamento::getDono)
                .compare(this, o);
    }

    public void verificarAtributos() {
        if (this.contaEntrada instanceof ContaCredito) {
            throw new IllegalArgumentException("Conta de entrada do lançamento não pode ser do tipo conta de crédito: " + this.contaEntrada);
        }
        if (this.contaSaida instanceof ContaDebito) {
            throw new IllegalArgumentException("Conta de saída do lançamento não pode ser do tipo conta de débito: " + this.contaSaida);
        }
    }
}
