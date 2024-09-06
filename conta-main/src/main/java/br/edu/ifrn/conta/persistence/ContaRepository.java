package br.edu.ifrn.conta.persistence;

import java.io.Serializable;

import br.edu.ifrn.conta.domain.Conta;
import java.util.Optional;

import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.query.QueryByExampleExecutor;

/**
 * Using parameterized types. Using Query By Example also.
 *
 * @param <T> account
 * @param <ID> account key
 */
public interface ContaRepository<T extends Conta, ID extends Serializable> extends CrudRepository<T, ID>, QueryByExampleExecutor<T> {

    Optional<T> findByDescricao(String descricao);

}
