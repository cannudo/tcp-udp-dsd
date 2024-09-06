package br.edu.ifrn.conta.service;

import java.math.BigDecimal;
import br.edu.ifrn.conta.domain.ContaPatrimonio;
import br.edu.ifrn.conta.domain.Dono;
import br.edu.ifrn.conta.persistence.LancamentoRepository;
import br.edu.ifrn.conta.persistence.ValorInicialDoDonoNaContaPatrimonioRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


/**
 * Service of saldo.
 */
@Service
public class SaldoService {

    private LancamentoRepository lancamentoRepository;
    private ValorInicialDoDonoNaContaPatrimonioRepository valorInicialDoDonoNaContaPatrimonioRepository;

    @Autowired
    public SaldoService(LancamentoRepository lancamentoRepository, ValorInicialDoDonoNaContaPatrimonioRepository valorInicialDoDonoNaContaPatrimonioRepository) {
        super();
        this.lancamentoRepository = lancamentoRepository;
        this.valorInicialDoDonoNaContaPatrimonioRepository = valorInicialDoDonoNaContaPatrimonioRepository;
    }

    public BigDecimal saldo(Dono dono, ContaPatrimonio contaPatrimonio) {
        // recupera o valor inicial do dono na conta patrimonio
        BigDecimal result = this.valorInicialDoDonoNaContaPatrimonioRepository
            .findByDonoAndContaPatrimonio(dono, contaPatrimonio)
            .get().getValorInicial();

        // soma todos os lancamentos de credito do dono na conta patrimonio
        BigDecimal creditos = this.lancamentoRepository.creditosSum(dono, contaPatrimonio).getValor();

        // subtrai todos os lancamentos de debito do dono na conta patrimonio
        BigDecimal debitos = this.lancamentoRepository.debitosSum(dono, contaPatrimonio).getValor();

        return result.add(creditos).subtract(debitos);
    }
}
