package uk.ac.brunel.d3s.rest;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import uk.ac.brunel.d3s.model.Device;
import uk.ac.brunel.d3s.model.MeasurementEntry;
import uk.ac.brunel.d3s.repository.DeviceRepository;
import uk.ac.brunel.d3s.repository.MeasurementEntryRepository;

import java.util.Random;
import java.util.UUID;

@RestController
public class RegisterController {

    private final DeviceRepository repository;
    private final MeasurementEntryRepository measurementEntryRepository;

    private RegisterController(DeviceRepository repository, MeasurementEntryRepository measurementEntryRepository) {
        this.repository = repository;
        this.measurementEntryRepository = measurementEntryRepository;
    }

    @RequestMapping(value = "/register", method = RequestMethod.GET)
    public String register() {
        String id = new UUID(new Random().nextInt(), new Random().nextInt()).toString();

        Device device = new Device(id);
        device.getMeasurementEntries().add(createMeasurementEntry());
        device.getMeasurementEntries().add(createMeasurementEntry());
        device.getMeasurementEntries().add(createMeasurementEntry());

        repository.save(device);

        return id;
    }

    private MeasurementEntry createMeasurementEntry() {
        MeasurementEntry measurementEntry = new MeasurementEntry();

        return measurementEntryRepository.save(measurementEntry);
    }

    @RequestMapping(value = "/unregister", method = RequestMethod.GET)
    public void unregister(@RequestParam("id") String id) {
        repository.deleteById(id);
    }

}
