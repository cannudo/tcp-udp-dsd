package br.edu.ifrn.conta.persistence;

import br.edu.ifrn.conta.domain.Categoria;
import java.util.Optional;

import org.springframework.data.repository.CrudRepository;

/**
 * Categoria Repository with method definition.
 */
public interface CategoriaRepository extends CrudRepository<Categoria, Long> {

    Optional<Categoria> findByDescricao(String descricao);

}
