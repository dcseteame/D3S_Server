package uk.ac.brunel.d3s.rest;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import uk.ac.brunel.d3s.model.Warning;
import uk.ac.brunel.d3s.repository.DeviceRepository;
import uk.ac.brunel.d3s.repository.MeasurementEntryRepository;
import uk.ac.brunel.d3s.repository.WarningRepository;

@RestController
public class WarningController {

    private final WarningRepository warningRepository;

    public WarningController(WarningRepository warningRepository) {
        this.warningRepository = warningRepository;
    }

    @RequestMapping(value = "/warning", method = RequestMethod.GET)
    public Warning ping(@RequestParam("description") String description) {
        Warning warning = new Warning(description);
        warningRepository.save(warning);
        return warning;
    }

}
