---
title: Measurand 
---

# Measurand 

## 1 Definition 

Particular [Quantity](../quantity) subject to [Measurement](../measurement).

### Notes 

### Examples 

| Step   | Process description                                                                                                                                                                                                                                                              |
| :----- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| (Raw) | The complete and unaltered/unprocessed set of data acquired by one or several sensors on a platform                                                                                                                                                                             |
| M/0 uncalibrated  | Unaltered/unprocessed Level 0 (main) sensor data annotated with processed ancillary data and supplemented by auxiliary data (including radiometric and geometric calibration coefficients and geo-referencing parameters) allowing further processing to higher Levels. |
| M/1 sensor-calibrated | Level M/0 sensor data which have been calibrated (ideally traceable to SI) and spatially aligned (co-located, eventually co-gridded) to represent at-sensor measurements (value and uncertainty) in sensor nominal spatiotemporal sampling, supplemented by appropriate anc |
| M/2 target-calibrated| Level M/1 data processed to represent geophysical property values (and uncertainties) for a specified target (object, feature of interest, e.g. surface reflectance, apparent temperature) derived from M/1 sensor data, as much as possible maintaining the sensors nominal spatial and temporal sampling (observation preserving).   |
| M/3 homogenised   | Level M/1 or M/2 data which have been generalised and integrated across one or several platforms and acquisitions to achieve an increased, more regular or in any other form enhanced spatial or temporal coverage in which states geophysical values agnostic of the originally acquiring sensor and observation condition and thus directly comparable. This homogenisation and fusion may include measurand re-calibration to external standards and references including use of modelling, aggregation and interpolation.                                                                   |
| M/4 derived/infered | Model output or results from analyses of Level M/3 (or lower level) data i.e., attributes that might not be directly observable by the sensor(s) but are derived from observations in combination with other external incl. non-observational data using techniques like modelling or machine learning (AI).        |

From http://doi.org/10.2760/46796

### Sources
- VIM: 1993, 2.6
