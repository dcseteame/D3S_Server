package uk.ac.brunel.d3s.rest;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import uk.ac.brunel.d3s.model.Warning;
import uk.ac.brunel.d3s.repository.DeviceRepository;
import uk.ac.brunel.d3s.repository.MeasurementEntryRepository;
import uk.ac.brunel.d3s.repository.WarningRepository;

import java.util.Iterator;

@RestController
public class PingController {

    private final DeviceRepository deviceRepository;
    private final WarningRepository warningRepository;

    public PingController(DeviceRepository deviceRepository, WarningRepository warningRepository) {
        this.deviceRepository = deviceRepository;
        this.warningRepository = warningRepository;
    }

    @RequestMapping(value = "/ping", method = RequestMethod.GET)
    public Warning ping(@RequestParam("id") String id) {
        deviceRepository.findById(id).ifPresent(device -> {
            device.setLastContact(System.currentTimeMillis());
            deviceRepository.save(device);
        });

        Warning warning = null;

        Iterable<Warning> warnings = warningRepository.findTop10ByOrderByIssueTimeDesc();
        Iterator<Warning> iterator = warnings.iterator();
        if (iterator.hasNext()) {
            warning = iterator.next();
        }

        if (warning == null) {
            warning = new Warning("ok");
            warningRepository.save(warning);
        }

        return warning;
    }

}
