package br.edu.ifrn.conta.service;

import java.math.BigDecimal;
import java.time.LocalDateTime;

import br.edu.ifrn.conta.domain.ContaCredito;
import br.edu.ifrn.conta.domain.ContaDebito;
import br.edu.ifrn.conta.domain.ContaPatrimonio;
import br.edu.ifrn.conta.domain.Dono;
import br.edu.ifrn.conta.domain.Lancamento;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import org.springframework.transaction.annotation.Transactional;

/**
 * Service of transferencia.
 */
@Service
public class TransferenciaService {

    private LancamentoService lancamentoService;

    private ContaDebitoService contaDebitoService;

    private ContaCreditoService contaCreditoService;
    
    @Autowired
    public TransferenciaService(LancamentoService lancamentoService,
            ContaDebitoService contaDebitoService, ContaCreditoService contaCreditoService) {
        super();
        this.lancamentoService = lancamentoService;
        this.contaDebitoService = contaDebitoService;
        this.contaCreditoService = contaCreditoService;
    }
    
    @Transactional
    public void transferir(BigDecimal valor, 
            Dono donoDebito, ContaPatrimonio contaPatrimonioADebitar, 
            Dono donoCredito, ContaPatrimonio contaPatrimonioACreditar) {

        ContaDebito contaDebito = contaDebitoService.despesaTransferencia();
        ContaCredito contaCredito = contaCreditoService.receitaTransferencia();
        
        if (donoCredito.equals(donoDebito)) {
            throw new IllegalArgumentException("Donos das contas devem ser diferentes: "
                    + donoDebito + " = " + donoCredito);
        }

        LocalDateTime data = LocalDateTime.now();

        Lancamento lancamentoComDespesa = Lancamento.builder()
                .contaEntrada(contaDebito)
                .contaSaida(contaPatrimonioADebitar)
                .dono(donoDebito)
                .valor(valor)
                .data(data)
                .descricao("Lançamento de débito de uma transferência")
                .build();
        lancamentoService.save(lancamentoComDespesa);

        Lancamento lancamentoComReceita = Lancamento.builder()
                .contaEntrada(contaPatrimonioACreditar)
                .contaSaida(contaCredito)
                .dono(donoCredito)
                .valor(valor)
                .data(data)
                .descricao("Lançamento de crédito de uma transferência")
                .build();
        lancamentoService.save(lancamentoComReceita);
    }
}
