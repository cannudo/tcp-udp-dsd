package br.edu.ifrn.conta.controller;

import br.edu.ifrn.conta.dto.ContaDebitoDTO;
import br.edu.ifrn.conta.dto.CategoriaDTO;
import br.edu.ifrn.conta.domain.ContaDebito;
import br.edu.ifrn.conta.service.CategoriaService;
import br.edu.ifrn.conta.service.ContaDebitoService;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * conta debito controller.
 */
@RestController
@RequestMapping("/contaDebito")
public class ContaDebitoController extends CrudController<ContaDebitoDTO, ContaDebito, Long> {

    @Autowired
    private ContaDebitoService contaDebitoService;
    
    @Autowired
    private CategoriaService categoriaService;
    
    @GetMapping("/findByDescricao")
    public Optional<ContaDebitoDTO> findByDescricao(@RequestParam String descricao) {
        return toDTOOptional(contaDebitoService.findByDescricao(descricao));
    }

    @Override
    protected ContaDebito toEntity(ContaDebitoDTO dto) {
        return ContaDebito.builder()
            .descricao(dto.getDescricao())
            .categoria(categoriaService.findByDescricao(dto.getCategoria().getDescricao()).get())
            .build();
    }

    @Override
    protected ContaDebitoDTO toDTO(ContaDebito entity) {
        return ContaDebitoDTO.builder()
            .descricao(entity.getDescricao())
            .categoria(CategoriaDTO.builder().descricao(entity.getCategoria().getDescricao()).build())
            .build();
    }
}
