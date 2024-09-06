package br.edu.ifrn.conta.controller;

import br.edu.ifrn.conta.dto.ContaPatrimonioDTO;
import br.edu.ifrn.conta.dto.CategoriaDTO;
import br.edu.ifrn.conta.domain.ContaPatrimonio;
import br.edu.ifrn.conta.service.CategoriaService;
import br.edu.ifrn.conta.service.ContaPatrimonioService;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * conta patrimonio controller.
 */
@RestController
@RequestMapping("/contaPatrimonio")
public class ContaPatrimonioController extends CrudController<ContaPatrimonioDTO, ContaPatrimonio, Long> {

    @Autowired
    private ContaPatrimonioService contaPatrimonioService;

    @Autowired
    private CategoriaService categoriaService;

    @GetMapping("/findByDescricao")
    public Optional<ContaPatrimonioDTO> findByDescricao(@RequestParam String descricao) {
        return toDTOOptional(contaPatrimonioService.findByDescricao(descricao));
    }

    @Override
    protected ContaPatrimonio toEntity(ContaPatrimonioDTO dto) {
        return ContaPatrimonio.builder()
                .descricao(dto.getDescricao())
                .categoria(categoriaService.findByDescricao(dto.getCategoria().getDescricao()).get())
                .build();
    }

    @Override
    protected ContaPatrimonioDTO toDTO(ContaPatrimonio entity) {
        return ContaPatrimonioDTO.builder()
                .descricao(entity.getDescricao())
                .categoria(CategoriaDTO.builder().descricao(entity.getCategoria().getDescricao()).build())
                .build();
    }
}
