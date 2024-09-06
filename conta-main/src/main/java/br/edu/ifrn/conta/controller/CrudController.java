package br.edu.ifrn.conta.controller;

import br.edu.ifrn.conta.service.CrudService;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

/**
 * Crud Controller
 */
public abstract class CrudController <D extends Object, T extends Object, ID extends Serializable> {

    @Autowired
    private CrudService<T, ID> crudService;
    
    @PostMapping
    public D save(@RequestBody D dto) {
        T saved = crudService.save(toEntity(dto));
        return toDTO(saved);
    }
    
    @GetMapping
    public Iterable<D> findAll() {
        List<D> result = new ArrayList<>();
        for(T entity : crudService.findAll()) {
            result.add(toDTO(entity));
        }
        return  result;
    }
    
    public Optional<D> toDTOOptional(Optional<T> entity) {
        if (entity.isEmpty()) {
            return Optional.empty();
        } else {
            return Optional.of(toDTO(entity.get()));
        }
    }
    
    protected abstract T toEntity(D dto);
    
    protected abstract D toDTO(T entity);
}
