package br.edu.ifrn.conta.controller;

import br.edu.ifrn.conta.dto.DonoDTO;
import br.edu.ifrn.conta.domain.Dono;
import br.edu.ifrn.conta.service.DonoService;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * Dono Controller
 */
@RestController
@RequestMapping("/dono")
public class DonoController extends CrudController<DonoDTO, Dono, Long> {

    @Autowired
    private DonoService donoService;
    
    @GetMapping("/findByDescricao")
    public Optional<DonoDTO> findByDescricao(@RequestParam String descricao) {
        return toDTOOptional(donoService.findByDescricao(descricao));
    }
    
    @DeleteMapping("/deleteByDescricao")
    public void deleteByDescricao(@RequestParam String descricao) {
        donoService.deleteByDescricao(descricao);
    }

    @Override
    protected Dono toEntity(DonoDTO dto) {
        return Dono.builder()
           .descricao(dto.getDescricao())
           .build();        
    }

    @Override
    protected DonoDTO toDTO(Dono entity) {
        return DonoDTO.builder()
           .descricao(entity.getDescricao())
           .build();
    }
}
