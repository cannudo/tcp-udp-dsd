package br.edu.ifrn.conta.restclient;

import java.net.URI;
import lombok.experimental.SuperBuilder;
import lombok.Data;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpMethod;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.util.UriComponentsBuilder;

@Data
@SuperBuilder
public class RestClientHelper <T> {

    private String endpoint;
    private String protocol;
    private String servername;
    private int port;
    private RestTemplate restTemplate;

    public String url() {
        return protocol + "://" + servername + ":" + port + "/" + endpoint;
    }

    private URI uri() {
        return UriComponentsBuilder.fromHttpUrl(url())
            .build().encode().toUri();
    }
    
    private URI uri(String suffix, String param, String value) {
        return UriComponentsBuilder.fromHttpUrl(url() + suffix)
            .queryParam(param, value)
            .build().encode().toUri();
    }
    
    public void deleteByDescricao(String descricao) {
        this.restTemplate.exchange(uri("/deleteByDescricao", "descricao", descricao), 
        HttpMethod.DELETE, null, new ParameterizedTypeReference<T>(){});
    }

    public Iterable<T> findAll() {
        return this.restTemplate.exchange(findAllUri(), 
      HttpMethod.GET, null, 
            new ParameterizedTypeReference<Iterable<T>>(){})
                .getBody();
    }

    public T save(T entity) {
        return this.restTemplate.exchange(saveUri(), 
            HttpMethod.POST, new HttpEntity<>(entity), new ParameterizedTypeReference<T>(){}).getBody();
    }
    
    public URI findByDescricaoUri(String descricao) {
        return uri("/findByDescricao", "descricao", descricao);
    }

    public URI findAllUri() {
        return uri();
    }

    public URI saveUri() {
        return uri();
    }

}
