package br.edu.ifrn.conta.restclient;

import br.edu.ifrn.conta.dto.TransferenciaDTO;
import java.math.BigDecimal;
import lombok.experimental.SuperBuilder;
import lombok.Data;
import org.springframework.web.util.UriComponentsBuilder;

@Data
@SuperBuilder
public class TransferenciaRestClient {

    private RestClientHelper<TransferenciaDTO> entityRestHelper;

    public void transferir(TransferenciaDTO transferenciaDTO) {
        this.entityRestHelper.getRestTemplate().postForObject(
         UriComponentsBuilder.fromHttpUrl(entityRestHelper.url() + "/transferir").build().encode().toUri(),
      transferenciaDTO,
  Void.class);
    }
    
}
