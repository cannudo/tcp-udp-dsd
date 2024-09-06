package br.edu.ifrn.conta.service;

import br.edu.ifrn.conta.domain.ContaDebito;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * Service of ContaDebito.
 */
@Service
public class ContaDebitoService extends ContaService<ContaDebito, Long> {
    @Autowired
    private CategoriaService categoriaService;
    
    public ContaDebito despesaTransferencia() {
        Optional<ContaDebito> findByDescricao = findByDescricao(ContaDebito.DESPESA_TRANSFERENCIA);
        if (findByDescricao.isEmpty()) {
            ContaDebito result = ContaDebito.builder()
                    .descricao(ContaDebito.DESPESA_TRANSFERENCIA)
                    .categoria(categoriaService.despesaTransferencia())
                    .build();
            return save(result);
        } else {
            return findByDescricao.get();
        }
    }
}
