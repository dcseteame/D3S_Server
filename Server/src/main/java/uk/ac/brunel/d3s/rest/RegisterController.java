package uk.ac.brunel.d3s.rest;

import org.springframework.web.bind.annotation.*;
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
    public String register(@RequestParam(name = "samplingRate", defaultValue = "60") int samplingRate,
                           @RequestParam(name = "latitude", defaultValue = "0") double latitude,
                           @RequestParam(name = "longitude", defaultValue = "0") double longitude) {
        String id = new UUID(new Random().nextInt(), new Random().nextInt()).toString();

        Device device = new Device(id, samplingRate, latitude, longitude);
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

    @RequestMapping(value = "/addMeasurement", method = RequestMethod.POST)
    public void addMeasurement(@RequestBody MeasurementEntry measurementEntry,
                               @RequestParam(name = "id") String id) {
        repository.findById(id).ifPresent(device -> {
            device.getMeasurementEntries().add(measurementEntry);
            repository.save(device);
        });
    }

}
