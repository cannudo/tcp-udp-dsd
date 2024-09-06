package br.edu.ifrn.conta.controller;

import br.edu.ifrn.conta.dto.ContaPatrimonioDTO;
import br.edu.ifrn.conta.dto.DonoDTO;
import br.edu.ifrn.conta.dto.ValorInicialDoDonoNaContaPatrimonioDTO;
import br.edu.ifrn.conta.domain.ValorInicialDoDonoNaContaPatrimonio;
import br.edu.ifrn.conta.service.ContaPatrimonioService;
import br.edu.ifrn.conta.service.DonoService;
import br.edu.ifrn.conta.service.ValorInicialDoDonoNaContaPatrimonioService;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * valorInicialDoDonoNaContaPatrimonio controller.
 */
@RestController
@RequestMapping("/valorInicialDoDonoNaContaPatrimonio")
public class ValorInicialDoDonoNaContaPatrimonioController extends CrudController<ValorInicialDoDonoNaContaPatrimonioDTO, ValorInicialDoDonoNaContaPatrimonio, Long> {

    @Autowired
    private ValorInicialDoDonoNaContaPatrimonioService valorInicialDoDonoNaContaPatrimonioService;
    
    @Autowired
    private DonoService donoService;
    
    @Autowired
    private ContaPatrimonioService contaPatrimonioService;
    
    @GetMapping("findByDonoAndContaPatrimonio")
    public Optional<ValorInicialDoDonoNaContaPatrimonioDTO> findByDonoAndContaPatrimonio(@RequestParam String dono, @RequestParam String contaPatrimonio) {
        return toDTOOptional(valorInicialDoDonoNaContaPatrimonioService.findByDonoAndContaPatrimonio(
        donoService.findByDescricao(dono).get(), 
contaPatrimonioService.findByDescricao(contaPatrimonio).get()));
    }

    @Override
    protected ValorInicialDoDonoNaContaPatrimonio toEntity(ValorInicialDoDonoNaContaPatrimonioDTO dto) {
        return ValorInicialDoDonoNaContaPatrimonio.builder()
            .valorInicial(dto.getValorInicial())
            .dono(donoService.findByDescricao(dto.getDono().getDescricao()).get())
            .contaPatrimonio(contaPatrimonioService.findByDescricao(dto.getContaPatrimonio().getDescricao()).get())
            .build();        
    }

    @Override
    protected ValorInicialDoDonoNaContaPatrimonioDTO toDTO(ValorInicialDoDonoNaContaPatrimonio entity) {
        return ValorInicialDoDonoNaContaPatrimonioDTO.builder()
           .valorInicial(entity.getValorInicial())
           .dono(DonoDTO.builder().descricao(entity.getDono().getDescricao()).build())
           .contaPatrimonio(ContaPatrimonioDTO.builder().descricao(entity.getContaPatrimonio().getDescricao()).build())
           .build();
    }
}
