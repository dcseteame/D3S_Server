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

    private float[] accelerationX = new float[50];
    private float[] accelerationY = new float[50];
    private float[] accelerationZ = new float[50];

    public MeasurementEntry() {
        time = System.nanoTime();
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

}
