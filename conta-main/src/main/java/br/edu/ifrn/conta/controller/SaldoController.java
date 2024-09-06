package br.edu.ifrn.conta.controller;

import br.edu.ifrn.conta.service.ContaPatrimonioService;
import br.edu.ifrn.conta.service.ContaService;
import br.edu.ifrn.conta.service.DonoService;
import br.edu.ifrn.conta.service.SaldoService;
import java.math.BigDecimal;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * Saldo controller
 */
@RestController
@RequestMapping("/")
public class SaldoController {

    @Autowired
    private SaldoService saldoService;
    @Autowired
    private DonoService donoService;
    @Autowired
    private ContaPatrimonioService contaPatrimonioService;
    @Autowired
    private ContaService contaService;

    @GetMapping("/saldo")
    public BigDecimal saldo(@RequestParam String dono, @RequestParam String contaPatrimonio) {
        return saldoService.saldo(donoService.findByDescricao(dono).get(),
                contaPatrimonioService.findByDescricao(contaPatrimonio).get());
    }
}
