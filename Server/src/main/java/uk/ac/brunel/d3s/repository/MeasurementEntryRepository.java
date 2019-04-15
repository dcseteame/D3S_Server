package uk.ac.brunel.d3s.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.data.rest.core.annotation.RestResource;
import org.springframework.stereotype.Repository;
import uk.ac.brunel.d3s.model.MeasurementEntry;

@Repository
public interface MeasurementEntryRepository extends CrudRepository<MeasurementEntry, Long> {

    @Override
    @RestResource(exported = false)
    void deleteById(Long l);

    @Override
    @RestResource(exported = false)
    void delete(MeasurementEntry measurementEntry);

    @Override
    @RestResource(exported = false)
    void deleteAll();

    @Override
    @RestResource(exported = false)
    void deleteAll(Iterable<? extends MeasurementEntry> iterable);

    @Override
    @RestResource(exported = false)
    <S extends MeasurementEntry> S save(S s);

    @Override
    @RestResource(exported = false)
    <S extends MeasurementEntry> Iterable<S> saveAll(Iterable<S> iterable);

}
