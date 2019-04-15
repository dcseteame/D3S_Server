package uk.ac.brunel.d3s;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;
import uk.ac.brunel.d3s.repository.DeviceRepository;

@Component
public class InactivityRemover {

    private static final Logger LOGGER = LoggerFactory.getLogger(InactivityRemover.class);

    private final DeviceRepository deviceRepository;

    public InactivityRemover(DeviceRepository deviceRepository) {
        this.deviceRepository = deviceRepository;
    }

    @Scheduled(fixedRate = 5000)
    public void removeAllInactiveDevices() {
        deviceRepository.findByLastContactLessThan(System.currentTimeMillis() - 1000000).forEach(device -> {
            deviceRepository.delete(device);
            LOGGER.info("Removing dead device " + device.getId());
        });
    }

}
