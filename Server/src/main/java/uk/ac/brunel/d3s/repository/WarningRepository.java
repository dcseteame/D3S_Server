package uk.ac.brunel.d3s.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.data.rest.core.annotation.RestResource;
import org.springframework.stereotype.Repository;
import uk.ac.brunel.d3s.model.Device;
import uk.ac.brunel.d3s.model.Warning;

import java.util.List;

@Repository
public interface WarningRepository extends CrudRepository<Warning, Long> {

    List<Warning> findTop10ByOrderByIssueTimeDesc();

    @Override
    @RestResource(exported = false)
    void deleteById(Long l);

    @Override
    @RestResource(exported = false)
    void delete(Warning warning);

    @Override
    @RestResource(exported = false)
    void deleteAll();

    @Override
    @RestResource(exported = false)
    void deleteAll(Iterable<? extends Warning> iterable);

    @Override
    @RestResource(exported = false)
    <S extends Warning> S save(S s);

    @Override
    @RestResource(exported = false)
    <S extends Warning> Iterable<S> saveAll(Iterable<S> iterable);

}
