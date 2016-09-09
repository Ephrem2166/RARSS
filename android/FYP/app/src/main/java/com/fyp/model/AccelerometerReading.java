package com.fyp.model;

// Used for both Accelerometer and Linear Accelerometer
public class AccelerometerReading extends SensorReading {
    private double ax, ay, az;

    public AccelerometerReading(long timestamp, double ax, double ay, double az) {
        super(timestamp);
        this.ax = ax;
        this.ay = ay;
        this.az = az;
    }

    public double getAx() {
        return ax;
    }

    public double getAy() {
        return ay;
    }

    public double getAz() {
        return az;
    }
}
