package br.edu.ifrn.conta.controller;

import br.edu.ifrn.conta.dto.CategoriaDTO;
import br.edu.ifrn.conta.domain.Categoria;
import br.edu.ifrn.conta.service.CategoriaService;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * Categoria controller.
 */
@RestController
@RequestMapping("/categoria")
public class CategoriaController extends CrudController<CategoriaDTO, Categoria, Long> {

    @Autowired
    private CategoriaService categoriaService;
    
    @GetMapping("/findByDescricao")
    public Optional<CategoriaDTO> findByDescricao(@RequestParam String descricao) {
        return toDTOOptional(categoriaService.findByDescricao(descricao));
    }

    @Override
    protected Categoria toEntity(CategoriaDTO dto) {
        return Categoria.builder()
           .descricao(dto.getDescricao())
           .build();
    }

    @Override
    protected CategoriaDTO toDTO(Categoria entity) {
        return CategoriaDTO.builder()
           .descricao(entity.getDescricao())
           .build();
    }

}
