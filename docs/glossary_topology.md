## Ancillary Data
**Parents**: Data, Position, Sensor

## Area Of Interest
**Parents**: Data, Information

## Auxiliary Data
**Parents**: Data, Sensor

## Band Central Wavelength
**Parents**: Sensor, Value

## Calibration
**Parents**: Data, Model, Sensor

## Characteristic
**Parents**: Feature<br>
**Children**: In-situ Observation, Representativeness, Trait

## Classification System
**Parents**: Information

## Confidence interval
**Children**: Expanded Uncertainty

## Copernicus Service Provider
**Parents**: Data, Information

## Data
**Children**: Ancillary Data, Area Of Interest, Auxiliary Data, Calibration, Copernicus Service Provider, Geographic Data, Information, Model, Observation, Replicability, Reproducibility, Sensor, Standard Uncertainty, User, Validation

## Duration
**Parents**: Quantity

## Entity
**Children**: Model, Object, Phenomenon, Trait, User

## Expanded Uncertainty
**Parents**: Confidence interval, Uncertainty

## Feature
**Children**: Characteristic, Geopositioning

## Geocoding
**Parents**: Location

## Geographic Coordinate Reference System
**Parents**: Reference

## Geographic Data
**Parents**: Data, Location, Reference

## Geographic Grid
**Parents**: Grid, Reference

## Geolocating
**Parents**: Geopositioning, Model, Object, Sensor

## Geolocation Information
**Parents**: Information, Location

## Geopositioning
**Parents**: Feature, Position<br>
**Children**: Geolocating

## Grid
**Children**: Geographic Grid

## In-situ Observation
**Parents**: Characteristic, Observation, Phenomenon, Place, Property, Sensor, Uncertainty, Value

## Information
**Parents**: Data<br>
**Children**: Area Of Interest, Classification System, Copernicus Service Provider, Geolocation Information, Temporal Reporting Period, Thematic Resolution, User

## Laboratory Observation
**Parents**: Object, Phenomenon

## Location
**Parents**: Place<br>
**Children**: Geocoding, Geographic Data, Geolocation Information, Representativeness

## Measurand
**Parents**: Measurement, Quantity<br>
**Children**: Uncertainty

## Measurement
**Parents**: Observation, Quantity<br>
**Children**: Measurand, Representativeness, Traceability, Uncertainty

## Model
**Parents**: Data, Entity<br>
**Children**: Calibration, Geolocating, Temporal Resolution, Time Of Day, Time Of Year, Vertical Levels

## Object
**Parents**: Entity<br>
**Children**: Geolocating, Laboratory Observation

## Observation
**Parents**: Data, Phenomenon, Property, Sensor, Value<br>
**Children**: In-situ Observation, Measurement, Reference, Remote Sensing, Representativeness, Temporal Resolution

## Period
**Children**: Period Identifier, Representativeness, Temporal Reporting Period, Temporal Resolution

## Period Identifier
**Parents**: Period, Reference

## Phenomenon
**Parents**: Entity, Property<br>
**Children**: In-situ Observation, Laboratory Observation, Observation, Reference, Remote Sensing, Sensor

## Place
**Children**: In-situ Observation, Location, Position

## Position
**Parents**: Place, Reference<br>
**Children**: Ancillary Data, Geopositioning

## Property
**Parents**: Trait<br>
**Children**: In-situ Observation, Observation, Phenomenon, Quantity, Traceability

## Quantity
**Parents**: Property<br>
**Children**: Duration, Measurand, Measurement

## Reference
**Parents**: Observation, Phenomenon, Uncertainty<br>
**Children**: Geographic Coordinate Reference System, Geographic Data, Geographic Grid, Period Identifier, Position, Traceability

## Remote Sensing
**Parents**: Observation, Phenomenon

## Replicability
**Parents**: Data

## Representativeness
**Parents**: Characteristic, Location, Measurement, Observation, Period

## Reproducibility
**Parents**: Data

## Sample
**Children**: Temporal Consistency

## Sensor
**Parents**: Data, Phenomenon<br>
**Children**: Ancillary Data, Auxiliary Data, Band Central Wavelength, Calibration, Geolocating, In-situ Observation, Observation

## Standard Uncertainty
**Parents**: Data, Uncertainty

## Temporal Consistency
**Parents**: Sample

## Temporal Reporting Period
**Parents**: Information, Period, Temporal resolution

## Temporal Resolution
**Parents**: Model, Observation, Period

## Temporal resolution
**Children**: Temporal Reporting Period

## Thematic Resolution
**Parents**: Information

## Thematic Uncertainty
**Parents**: Uncertainty

## Time Of Day
**Parents**: Model

## Time Of Year
**Parents**: Model

## Traceability
**Parents**: Measurement, Property, Reference, Uncertainty

## Trait
**Parents**: Characteristic, Entity<br>
**Children**: Property

## Uncertainty
**Parents**: Measurand, Measurement<br>
**Children**: Expanded Uncertainty, In-situ Observation, Reference, Standard Uncertainty, Thematic Uncertainty, Traceability

## User
**Parents**: Data, Entity, Information

## Validation
**Parents**: Data

## Value
**Children**: Band Central Wavelength, In-situ Observation, Observation

## Vertical Levels
**Parents**: Model

