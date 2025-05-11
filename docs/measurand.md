---
title: Measurand 
---

# Measurand 

## 1 Definition 

Particular [Quantity](../quantity) subject to [Measurement](../measurement).

### Notes 

### Examples 

| Step   | [Process](../process) description                                                                                                                                                                                                                                                              |
| :----- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| (Raw) | The complete and unaltered/unprocessed set of [Data](../data) acquired by one or several [sensors](../sensor) on a platform                                                                                                                                                                             |
| M/0 uncalibrated  | Unaltered/unprocessed Level 0 (main) [Sensor](../sensor) [Data](../data) annotated with processed [Ancillary Data](../ancillary_data) and supplemented by [Auxiliary Data](../auxiliary_data) (including radiometric and geometric [Calibration](../calibration) coefficients and geo-referencing parameters) allowing further processing to higher Levels. |
| M/1 [Sensor](../sensor)-calibrated | Level M/0 [Sensor](../sensor) [Data](../data) which have been calibrated (ideally traceable to SI) and spatially aligned (co-located, eventually co-gridded) to represent at-[Sensor](../sensor) [measurements](../measurement) ([Value](../value) and [Uncertainty](../uncertainty)) in [Sensor](../sensor) nominal spatiotemporal sampling, supplemented by appropriate anc |
| M/2 target-calibrated| Level M/1 [Data](../data) processed to represent geophysical [Property](../property) [values](../value) (and uncertainties) for a specified target ([Object](../object), [Feature](../feature) of interest, e.g. surface reflectance, apparent temperature) derived from M/1 [Sensor](../sensor) [Data](../data), as much as possible maintaining the [sensors](../sensor) nominal spatial and temporal sampling ([Observation](../observation) preserving).   |
| M/3 homogenised   | Level M/1 or M/2 [Data](../data) which have been generalised and integrated across one or several platforms and acquisitions to achieve an increased, more regular or in any other form enhanced spatial or temporal coverage in which states geophysical [values](../value) agnostic of the originally acquiring [Sensor](../sensor) and [Observation](../observation) condition and thus directly comparable. This homogenisation and fusion may include measurand re-[Calibration](../calibration) to external standards and [references](../reference) including use of modelling, aggregation and interpolation.                                                                   |
| M/4 derived/infered | [Model](../model) output or results from analyses of Level M/3 (or lower level) [Data](../data) i.e., attributes that might not be directly observable by the [Sensor](../sensor)(s) but are derived from [observations](../observation) in combination with other external incl. non-observational [Data](../data) using techniques like modelling or machine learning (AI).        |

From http://doi.org/10.2760/46796

### Sources
- VIM: 1993, 2.6
