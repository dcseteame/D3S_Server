package uk.ac.brunel.d3s.model;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
public class Device {

    @Id
    private String id;

    private long lastContact = System.currentTimeMillis();

    private int samplingRate = 60;

    private double latitude;
    private double longitude;

    @OneToMany(cascade = CascadeType.ALL, orphanRemoval = true)
    private List<MeasurementEntry> measurementEntries = new ArrayList<>();

    public Device() {

    }

    public Device(String id, int samplingRate, double latitude, double longitude) {
        this.id = id;
        this.samplingRate = samplingRate;
        this.latitude = latitude;
        this.longitude = longitude;
    }

    public String getId() {
        return id;
    }

    public long getLastContact() {
        return lastContact;
    }

    public void setLastContact(long lastContact) {
        this.lastContact = lastContact;
    }

    public int getSamplingRate() {
        return samplingRate;
    }

    public void setSamplingRate(int samplingRate) {
        this.samplingRate = samplingRate;
    }

    public double getLatitude() {
        return latitude;
    }

    public void setLatitude(double latitude) {
        this.latitude = latitude;
    }

    public double getLongitude() {
        return longitude;
    }

    public void setLongitude(double longitude) {
        this.longitude = longitude;
    }

    public List<MeasurementEntry> getMeasurementEntries() {
        return measurementEntries;
    }

}
