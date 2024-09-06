package br.edu.ifrn.conta.service;

import br.edu.ifrn.conta.domain.Dono;
import br.edu.ifrn.conta.persistence.DonoRepository;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

/**
 * Service of Dono.
 */
@Service
public class DonoService extends CrudService<Dono, Long> {
    
    @Autowired
    private DonoRepository donoRepository;
    
    public Optional<Dono> findByDescricao(String descricao) {
        return donoRepository.findByDescricao(descricao);
    }
    
    @Transactional
    public void deleteByDescricao(String descricao) {
        donoRepository.deleteByDescricao(descricao);
    }
}
