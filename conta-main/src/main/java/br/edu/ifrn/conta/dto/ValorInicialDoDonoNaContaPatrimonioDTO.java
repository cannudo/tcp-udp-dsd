package br.edu.ifrn.conta.dto;

import java.io.Serializable;
import java.math.BigDecimal;
import lombok.experimental.SuperBuilder;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

/**
 * DTO interface.
 */
@SuperBuilder
@Data
@ToString
@NoArgsConstructor
public class ValorInicialDoDonoNaContaPatrimonioDTO implements Serializable {
    private DonoDTO dono;
    private ContaPatrimonioDTO contaPatrimonio;
    private BigDecimal valorInicial;
}
