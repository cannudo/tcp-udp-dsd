package br.edu.ifrn.conta.dto;

import java.io.Serializable;
import java.math.BigDecimal;
import java.time.LocalDateTime;
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
public class LancamentoDTO implements Serializable {
    private LocalDateTime data;
    private BigDecimal valor;
    private ContaDTO contaEntrada;
    private ContaDTO contaSaida;
    private DonoDTO dono;
    private String descricao;
}
