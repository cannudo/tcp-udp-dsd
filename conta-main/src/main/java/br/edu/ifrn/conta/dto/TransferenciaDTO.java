package br.edu.ifrn.conta.dto;

import java.io.Serializable;
import java.math.BigDecimal;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;
import lombok.ToString;
import lombok.experimental.SuperBuilder;

/**
 * Transferencia DTO.
 */
@SuperBuilder
@Data
@EqualsAndHashCode
@ToString
@NoArgsConstructor
public class TransferenciaDTO implements Serializable {
    private BigDecimal valor;
    private String donoDebito;
    private String contaDebito;
    private String donoCredito;
    private String contaCredito;
}
