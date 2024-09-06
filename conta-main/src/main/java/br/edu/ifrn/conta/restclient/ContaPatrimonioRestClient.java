package br.edu.ifrn.conta.restclient;

import br.edu.ifrn.conta.dto.ContaPatrimonioDTO;
import java.util.Optional;
import lombok.experimental.SuperBuilder;
import lombok.Data;

@Data
@SuperBuilder
public class ContaPatrimonioRestClient {

    private RestClientHelper<ContaPatrimonioDTO> entityRestHelper;

    public void deleteByDescricao(String descricao) {
        entityRestHelper.deleteByDescricao(descricao);
    }

    public Optional<ContaPatrimonioDTO> findByDescricao(String descricao) {
        return Optional.ofNullable(this.entityRestHelper.getRestTemplate().getForObject(
                entityRestHelper.findByDescricaoUri(descricao), ContaPatrimonioDTO.class));
    }

    public Iterable<ContaPatrimonioDTO> findAll() {
        return this.entityRestHelper.findAll();
    }

    public ContaPatrimonioDTO save(ContaPatrimonioDTO entity) {
        return this.entityRestHelper.getRestTemplate().postForObject(
                entityRestHelper.saveUri(), entity, ContaPatrimonioDTO.class);
    }

}
