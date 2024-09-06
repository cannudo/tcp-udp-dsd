package br.edu.ifrn.conta.dto;

import java.io.Serializable;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;
import lombok.experimental.SuperBuilder;

/**
 * DTO interface.
 */
@SuperBuilder
@Data
@ToString
@NoArgsConstructor
public class ContaDTO implements Serializable {
    private String descricao;
    private CategoriaDTO categoria;
}
