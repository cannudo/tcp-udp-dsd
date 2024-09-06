package br.edu.ifrn.conta.service;

import br.edu.ifrn.conta.domain.ContaCredito;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * Service of ContaCredito.
 */
@Service
public class ContaCreditoService extends ContaService<ContaCredito, Long> {
    @Autowired
    private CategoriaService categoriaService;
    
    public ContaCredito receitaTransferencia() {
        Optional<ContaCredito> findByDescricao = findByDescricao(ContaCredito.RECEITA_DE_TRANSFERENCIA);
        if (findByDescricao.isEmpty()) {
            ContaCredito result = ContaCredito.builder()
                    .descricao(ContaCredito.RECEITA_DE_TRANSFERENCIA)
                    .categoria(categoriaService.despesaTransferencia())
                    .build();
            return save(result);
        } else {
            return findByDescricao.get();
        }
    }
}
