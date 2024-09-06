package br.edu.ifrn.conta.service;

import java.io.Serializable;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.data.repository.CrudRepository;
import org.springframework.transaction.annotation.Transactional;

/**
 * Default service delagating to repository.
 * @param <T> entity
 * @param <ID> entity id
 */
@Transactional(readOnly = true)
public class CrudService<T extends Object, ID extends Serializable> {

	private CrudRepository<T, ID> repository;

	@Autowired
	public void setRepository(CrudRepository<T, ID> repository) {
		this.repository = repository;
	}

	@Transactional
	public <S extends T> Iterable<S> saveAll(Iterable<S> entities) {
		return this.repository.saveAll(entities);
	}

	@Transactional
	public <S extends T> S save(S entity) {
		return this.repository.save(entity);
	}

	@Transactional
	public void deleteAll(Iterable<? extends T> entities) {
		this.repository.deleteAll(entities);
	}

	@Transactional
	public void deleteAllById(Iterable<? extends ID> ids) {
		this.repository.deleteAllById(ids);
	}

	@Transactional
	public void deleteById(ID id) {
		this.repository.deleteById(id);
	}

	@Transactional
	public void delete(T entity) {
		this.repository.delete(entity);
	}

	@Transactional
	public void deleteAll() {
		this.repository.deleteAll();
	}

	public Optional<T> findById(ID id) {
		return this.repository.findById(id);
	}

	public Iterable<T> findAll() {
		return this.repository.findAll();
	}

	public Iterable<T> findAllById(Iterable<ID> ids) {
		return this.repository.findAllById(ids);
	}

	public long count() {
		return this.repository.count();
	}

	public boolean existsById(ID id) {
		return this.repository.existsById(id);
	}

}
