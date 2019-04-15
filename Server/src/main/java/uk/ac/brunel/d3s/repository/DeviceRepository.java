package uk.ac.brunel.d3s.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.data.rest.core.annotation.RestResource;
import org.springframework.stereotype.Repository;
import uk.ac.brunel.d3s.model.Device;
import uk.ac.brunel.d3s.model.MeasurementEntry;

import java.util.List;

@Repository
public interface DeviceRepository extends CrudRepository<Device, String> {

    List<Device> findByLastContactLessThan(long time);

    @Override
    @RestResource(exported = false)
    void deleteById(String s);

    @Override
    @RestResource(exported = false)
    void delete(Device device);

    @Override
    @RestResource(exported = false)
    void deleteAll();

    @Override
    @RestResource(exported = false)
    void deleteAll(Iterable<? extends Device> iterable);

    @Override
    @RestResource(exported = false)
    <S extends Device> S save(S s);

    @Override
    @RestResource(exported = false)
    <S extends Device> Iterable<S> saveAll(Iterable<S> iterable);

}
