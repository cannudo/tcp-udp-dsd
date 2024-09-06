package br.edu.ifrn.conta.service;

import br.edu.ifrn.conta.domain.ContaPatrimonio;
import br.edu.ifrn.conta.domain.Dono;
import br.edu.ifrn.conta.domain.ValorInicialDoDonoNaContaPatrimonio;
import br.edu.ifrn.conta.persistence.ValorInicialDoDonoNaContaPatrimonioRepository;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * Service of ValorInicialDoDonoNaContaPatrimonio.
 */
@Service
public class ValorInicialDoDonoNaContaPatrimonioService extends CrudService<ValorInicialDoDonoNaContaPatrimonio, Long> {
    @Autowired
    private ValorInicialDoDonoNaContaPatrimonioRepository valorInicialDoDonoNaContaPatrimonioRepository;
    
    public Optional<ValorInicialDoDonoNaContaPatrimonio> findByDonoAndContaPatrimonio(Dono dono, ContaPatrimonio contaPatrimonio) {
        return valorInicialDoDonoNaContaPatrimonioRepository.findByDonoAndContaPatrimonio(dono, contaPatrimonio);
    }
}
