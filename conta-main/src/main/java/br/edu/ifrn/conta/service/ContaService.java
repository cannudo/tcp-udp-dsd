package br.edu.ifrn.conta.service;

import br.edu.ifrn.conta.domain.Conta;
import br.edu.ifrn.conta.persistence.ContaRepository;
import java.io.Serializable;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * Service of Conta.
 */
@Service
public class ContaService<T extends Conta, ID extends Serializable> extends CrudService<T, ID> {
    @Autowired
    private ContaRepository<T, ID> contaRepository;
    
    public Optional<T> findByDescricao(String descricao) {
        return contaRepository.findByDescricao(descricao);
    }
}
