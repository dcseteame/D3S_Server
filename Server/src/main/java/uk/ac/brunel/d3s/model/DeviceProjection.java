package uk.ac.brunel.d3s.model;

import org.springframework.data.rest.core.config.Projection;

import java.util.List;

@Projection(name = "deviceProjection", types = Device.class)
public interface DeviceProjection {

    String getId();

    int getSamplingRate();

    long getLatitude();

    long getLongitude();

    List<MeasurementEntry> getMeasurementEntries();

}
