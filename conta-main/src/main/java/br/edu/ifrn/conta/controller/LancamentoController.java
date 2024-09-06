package br.edu.ifrn.conta.controller;

import br.edu.ifrn.conta.dto.ContaDTO;
import br.edu.ifrn.conta.dto.DonoDTO;
import br.edu.ifrn.conta.dto.LancamentoDTO;
import br.edu.ifrn.conta.dto.CategoriaDTO;
import br.edu.ifrn.conta.domain.Conta;
import br.edu.ifrn.conta.domain.Lancamento;
import br.edu.ifrn.conta.service.ContaPatrimonioService;
import br.edu.ifrn.conta.service.ContaService;
import br.edu.ifrn.conta.service.DonoService;
import br.edu.ifrn.conta.service.LancamentoService;
import java.math.BigDecimal;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Lancamento controller.
 */
@RestController
@RequestMapping("/lancamento")
public class LancamentoController extends CrudController<LancamentoDTO, Lancamento, Long> {

    @Autowired
    private LancamentoService lancamentoService;
    @Autowired
    private DonoService donoService;
    @Autowired
    private ContaPatrimonioService contaPatrimonioService;
    @Autowired
    private ContaService<Conta, Long> contaService;

    @Override
    protected Lancamento toEntity(LancamentoDTO dto) {
        return Lancamento.builder()
            .contaEntrada(contaService.findByDescricao(
        dto.getContaEntrada().getDescricao()).get())
            .contaSaida(contaService.findByDescricao(
        dto.getContaSaida().getDescricao()).get())
            .dono(donoService.findByDescricao(dto.getDono().getDescricao()).get())
            .data(dto.getData())
            .valor(dto.getValor())
            .descricao(dto.getDescricao())
            .build();
    }
    
    @Override
    protected LancamentoDTO toDTO(Lancamento entity) {
        return LancamentoDTO.builder()
            .contaEntrada(ContaDTO.builder()
                .descricao(entity.getContaEntrada().getDescricao())
                .categoria(CategoriaDTO.builder().descricao(
            entity.getContaEntrada().getCategoria().getDescricao()).build())
                .build())
            .contaSaida(ContaDTO.builder()
                .descricao(entity.getContaSaida().getDescricao())
                .categoria(CategoriaDTO.builder().descricao(
            entity.getContaSaida().getCategoria().getDescricao()).build())
                .build())
            .dono(DonoDTO.builder().descricao(entity.getDono().getDescricao()).build())
            .data(entity.getData())
            .valor(entity.getValor())
            .descricao(entity.getDescricao())
            .build();
    }

    @GetMapping("/creditosSum")
    public BigDecimal creditosSum(String dono, String contaPatrimonio) {
        return lancamentoService.creditosSum(donoService.findByDescricao(dono).get(), 
contaPatrimonioService.findByDescricao(contaPatrimonio).get());
    }
    
    @GetMapping("/debitosSum")
    public BigDecimal debitosSum(String dono, String contaPatrimonio) {
        return lancamentoService.debitosSum(donoService.findByDescricao(dono).get(), 
contaPatrimonioService.findByDescricao(contaPatrimonio).get());
    }
}
