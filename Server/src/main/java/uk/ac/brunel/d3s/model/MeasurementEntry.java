package uk.ac.brunel.d3s.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class MeasurementEntry {

    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    private Long id;

    private long time;

    private float[] accelerationX;
    private float[] accelerationY;
    private float[] accelerationZ;

    public MeasurementEntry() {
    }

    public long getTime() {
        return time;
    }

    public float[] getAccelerationX() {
        return accelerationX;
    }

    public float[] getAccelerationY() {
        return accelerationY;
    }

    public float[] getAccelerationZ() {
        return accelerationZ;
    }

    public void setAccelerationX(float[] accelerationX) {
        this.accelerationX = accelerationX;
    }

    public void setAccelerationY(float[] accelerationY) {
        this.accelerationY = accelerationY;
    }

    public void setAccelerationZ(float[] accelerationZ) {
        this.accelerationZ = accelerationZ;
    }

    public void setTime(long time) {
        this.time = time;
    }
}
