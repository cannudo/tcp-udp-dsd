package br.edu.ifrn.conta.service;

import br.edu.ifrn.conta.domain.Categoria;
import br.edu.ifrn.conta.persistence.CategoriaRepository;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * Service of Categoria.
 */
@Service
public class CategoriaService extends CrudService<Categoria, Long> {
    @Autowired
    private CategoriaRepository categoriaRepository;
    
    public Optional<Categoria> findByDescricao(String descricao) {
        return categoriaRepository.findByDescricao(descricao);
    }
    
    private Categoria categoria(String descricao) {
        Optional<Categoria> findByDescricao = findByDescricao(descricao);
        if (findByDescricao.isEmpty()) {
            Categoria result = Categoria.builder().descricao(descricao).build();
            return save(result);
        } else {
            return findByDescricao.get();
        }
    }
    
    public Categoria despesaTransferencia() {
        return categoria(Categoria.CATEGORIA_DESPESA_TRANSFERENCIA);
    }
    
    public Categoria receitaTransferencia() {
        return categoria(Categoria.CATEGORIA_RECEITA_TRANSFERENCIA);
    }
}
