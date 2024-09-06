package br.edu.ifrn.conta.service;

import br.edu.ifrn.conta.domain.ContaPatrimonio;
import br.edu.ifrn.conta.domain.Dono;
import br.edu.ifrn.conta.domain.Lancamento;
import br.edu.ifrn.conta.persistence.LancamentoRepository;
import java.math.BigDecimal;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import org.springframework.transaction.annotation.Transactional;

/**
 * Service of Lancamento.
 */
@Service
public class LancamentoService extends CrudService<Lancamento, Long> {

    @Autowired
    private LancamentoRepository lancamentoRepository;
    
    @Override
    @Transactional
    public Lancamento save(Lancamento objeto) {
        objeto.verificarAtributos();

        return super.save(objeto);
    }
    
    public BigDecimal creditosSum(Dono dono, ContaPatrimonio contaPatrimonio) {
        return lancamentoRepository.creditosSum(dono, contaPatrimonio).getValor();
    }
    
    public BigDecimal debitosSum(Dono dono, ContaPatrimonio contaPatrimonio) {
        return lancamentoRepository.debitosSum(dono, contaPatrimonio).getValor();
    }
}
