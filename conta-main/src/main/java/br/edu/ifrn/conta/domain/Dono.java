package br.edu.ifrn.conta.domain;

import java.io.Serializable;
import java.util.Set;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import jakarta.persistence.SequenceGenerator;

import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.experimental.SuperBuilder;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.Singular;
import lombok.ToString;

/**
 * Dono entity.
 */
@Getter
@Setter
@ToString(of = "descricao")
@EqualsAndHashCode(exclude = {"lancamentos", "valoresIniciaisNasContasPatrimonio"})
@SuperBuilder
@Entity
@SequenceGenerator(sequenceName = "seq_dono", name = "ID_SEQUENCE", allocationSize = 1)
@NoArgsConstructor(access = AccessLevel.PRIVATE)
@AllArgsConstructor(access = AccessLevel.PRIVATE)
public class Dono implements Serializable, Comparable<Dono> {

    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "ID_SEQUENCE")
    private Long id;

    @Column(nullable = false, unique = true)
    private String descricao;

    @Singular
    @OneToMany(mappedBy = "dono")
    private Set<Lancamento> lancamentos;

    @Singular("valorInicialNaContaPatrimonio")
    @OneToMany(mappedBy = "dono")
    private Set<ValorInicialDoDonoNaContaPatrimonio> valoresIniciaisNasContasPatrimonio;

    @Override
    public int compareTo(Dono o) {
        return this.descricao.compareTo(o.descricao);
    }

}
