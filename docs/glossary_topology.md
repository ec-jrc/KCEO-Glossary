## [Ancillary Data](../ancillary_data/)
**Parents**: [Data](../data/), [Position](../position/), [Sensor](../sensor/)

## [Area Of Interest](../area_of_interest/)
**Parents**: [Data](../data/), [Information](../information/)

## [Auxiliary Data](../auxiliary_data/)
**Parents**: [Data](../data/), [Sensor](../sensor/)

## [Band Central Wavelength](../band_central_wavelength/)
**Parents**: [Sensor](../sensor/), [Value](../value/)

## [Calibration](../calibration/)
**Parents**: [Data](../data/), [Model](../model/), [Sensor](../sensor/)

## [Characteristic](../characteristic/)
**Parents**: [Feature](../feature/)<br>
**Children**: [In-situ Observation](../in-situ_observation/), [Representativeness](../representativeness/), [Trait](../trait/)

## [Classification System](../classification_system/)
**Parents**: [Information](../information/)

## [Confidence interval](../confidence_interval/)
**Children**: [Expanded Uncertainty](../expanded_uncertainty/)

## [Copernicus Service Provider](../copernicus_service_provider/)
**Parents**: [Data](../data/), [Information](../information/)

## [Data](../data/)
**Children**: [Ancillary Data](../ancillary_data/), [Area Of Interest](../area_of_interest/), [Auxiliary Data](../auxiliary_data/), [Calibration](../calibration/), [Copernicus Service Provider](../copernicus_service_provider/), [Geographic Data](../geographic_data/), [Information](../information/), [Model](../model/), [Observation](../observation/), [Replicability](../replicability/), [Reproducibility](../reproducibility/), [Sensor](../sensor/), [Standard Uncertainty](../standard_uncertainty/), [User](../user/), [Validation](../validation/)

## [Duration](../duration/)
**Parents**: [Quantity](../quantity/)

## [Entity](../entity/)
**Children**: [Model](../model/), [Object](../object/), [Phenomenon](../phenomenon/), [Trait](../trait/), [User](../user/)

## [Expanded Uncertainty](../expanded_uncertainty/)
**Parents**: [Confidence interval](../confidence_interval/), [Uncertainty](../uncertainty/)

## [Feature](../feature/)
**Children**: [Characteristic](../characteristic/), [Geopositioning](../geopositioning/)

## [Geocoding](../geocoding/)
**Parents**: [Location](../location/)

## [Geographic Coordinate Reference System](../geographic_coordinate_reference_system/)
**Parents**: [Reference](../reference/)

## [Geographic Data](../geographic_data/)
**Parents**: [Data](../data/), [Location](../location/), [Reference](../reference/)

## [Geographic Grid](../geographic_grid/)
**Parents**: [Grid](../grid/), [Reference](../reference/)

## [Geolocating](../geolocating/)
**Parents**: [Geopositioning](../geopositioning/), [Model](../model/), [Object](../object/), [Sensor](../sensor/)

## [Geolocation Information](../geolocation_information/)
**Parents**: [Information](../information/), [Location](../location/)

## [Geopositioning](../geopositioning/)
**Parents**: [Feature](../feature/), [Position](../position/)<br>
**Children**: [Geolocating](../geolocating/)

## [Grid](../grid/)
**Children**: [Geographic Grid](../geographic_grid/)

## [In-situ Observation](../in-situ_observation/)
**Parents**: [Characteristic](../characteristic/), [Observation](../observation/), [Phenomenon](../phenomenon/), [Place](../place/), [Property](../property/), [Sensor](../sensor/), [Uncertainty](../uncertainty/), [Value](../value/)

## [Information](../information/)
**Parents**: [Data](../data/)<br>
**Children**: [Area Of Interest](../area_of_interest/), [Classification System](../classification_system/), [Copernicus Service Provider](../copernicus_service_provider/), [Geolocation Information](../geolocation_information/), [Temporal Reporting Period](../temporal_reporting_period/), [Thematic Resolution](../thematic_resolution/), [User](../user/)

## [Laboratory Observation](../laboratory_observation/)
**Parents**: [Object](../object/), [Phenomenon](../phenomenon/)

## [Location](../location/)
**Parents**: [Place](../place/)<br>
**Children**: [Geocoding](../geocoding/), [Geographic Data](../geographic_data/), [Geolocation Information](../geolocation_information/), [Representativeness](../representativeness/)

## [Measurand](../measurand/)
**Parents**: [Measurement](../measurement/), [Quantity](../quantity/)<br>
**Children**: [Uncertainty](../uncertainty/)

## [Measurement](../measurement/)
**Parents**: [Observation](../observation/), [Quantity](../quantity/)<br>
**Children**: [Measurand](../measurand/), [Representativeness](../representativeness/), [Traceability](../traceability/), [Uncertainty](../uncertainty/)

## [Model](../model/)
**Parents**: [Data](../data/), [Entity](../entity/)<br>
**Children**: [Calibration](../calibration/), [Geolocating](../geolocating/), [Temporal Resolution](../temporal_resolution/), [Time Of Day](../time_of_day/), [Time Of Year](../time_of_year/), [Vertical Levels](../vertical_levels/)

## [Object](../object/)
**Parents**: [Entity](../entity/)<br>
**Children**: [Geolocating](../geolocating/), [Laboratory Observation](../laboratory_observation/)

## [Observation](../observation/)
**Parents**: [Data](../data/), [Phenomenon](../phenomenon/), [Property](../property/), [Sensor](../sensor/), [Value](../value/)<br>
**Children**: [In-situ Observation](../in-situ_observation/), [Measurement](../measurement/), [Reference](../reference/), [Remote Sensing](../remote_sensing/), [Representativeness](../representativeness/), [Temporal Resolution](../temporal_resolution/)

## [Period](../period/)
**Children**: [Period Identifier](../period_identifier/), [Representativeness](../representativeness/), [Temporal Reporting Period](../temporal_reporting_period/), [Temporal Resolution](../temporal_resolution/)

## [Period Identifier](../period_identifier/)
**Parents**: [Period](../period/), [Reference](../reference/)

## [Phenomenon](../phenomenon/)
**Parents**: [Entity](../entity/), [Property](../property/)<br>
**Children**: [In-situ Observation](../in-situ_observation/), [Laboratory Observation](../laboratory_observation/), [Observation](../observation/), [Reference](../reference/), [Remote Sensing](../remote_sensing/), [Sensor](../sensor/)

## [Place](../place/)
**Children**: [In-situ Observation](../in-situ_observation/), [Location](../location/), [Position](../position/)

## [Position](../position/)
**Parents**: [Place](../place/), [Reference](../reference/)<br>
**Children**: [Ancillary Data](../ancillary_data/), [Geopositioning](../geopositioning/)

## [Property](../property/)
**Parents**: [Trait](../trait/)<br>
**Children**: [In-situ Observation](../in-situ_observation/), [Observation](../observation/), [Phenomenon](../phenomenon/), [Quantity](../quantity/), [Traceability](../traceability/)

## [Quantity](../quantity/)
**Parents**: [Property](../property/)<br>
**Children**: [Duration](../duration/), [Measurand](../measurand/), [Measurement](../measurement/)

## [Reference](../reference/)
**Parents**: [Observation](../observation/), [Phenomenon](../phenomenon/), [Uncertainty](../uncertainty/)<br>
**Children**: [Geographic Coordinate Reference System](../geographic_coordinate_reference_system/), [Geographic Data](../geographic_data/), [Geographic Grid](../geographic_grid/), [Period Identifier](../period_identifier/), [Position](../position/), [Traceability](../traceability/)

## [Remote Sensing](../remote_sensing/)
**Parents**: [Observation](../observation/), [Phenomenon](../phenomenon/)

## [Replicability](../replicability/)
**Parents**: [Data](../data/)

## [Representativeness](../representativeness/)
**Parents**: [Characteristic](../characteristic/), [Location](../location/), [Measurement](../measurement/), [Observation](../observation/), [Period](../period/)

## [Reproducibility](../reproducibility/)
**Parents**: [Data](../data/)

## [Sample](../sample/)
**Children**: [Temporal Consistency](../temporal_consistency/)

## [Sensor](../sensor/)
**Parents**: [Data](../data/), [Phenomenon](../phenomenon/)<br>
**Children**: [Ancillary Data](../ancillary_data/), [Auxiliary Data](../auxiliary_data/), [Band Central Wavelength](../band_central_wavelength/), [Calibration](../calibration/), [Geolocating](../geolocating/), [In-situ Observation](../in-situ_observation/), [Observation](../observation/)

## [Standard Uncertainty](../standard_uncertainty/)
**Parents**: [Data](../data/), [Uncertainty](../uncertainty/)

## [Temporal Consistency](../temporal_consistency/)
**Parents**: [Sample](../sample/)

## [Temporal Reporting Period](../temporal_reporting_period/)
**Parents**: [Information](../information/), [Period](../period/), [Temporal resolution](../temporal_resolution/)

## [Temporal Resolution](../temporal_resolution/)
**Parents**: [Model](../model/), [Observation](../observation/), [Period](../period/)

## [Temporal resolution](../temporal_resolution/)
**Children**: [Temporal Reporting Period](../temporal_reporting_period/)

## [Thematic Resolution](../thematic_resolution/)
**Parents**: [Information](../information/)

## [Thematic Uncertainty](../thematic_uncertainty/)
**Parents**: [Uncertainty](../uncertainty/)

## [Time Of Day](../time_of_day/)
**Parents**: [Model](../model/)

## [Time Of Year](../time_of_year/)
**Parents**: [Model](../model/)

## [Traceability](../traceability/)
**Parents**: [Measurement](../measurement/), [Property](../property/), [Reference](../reference/), [Uncertainty](../uncertainty/)

## [Trait](../trait/)
**Parents**: [Characteristic](../characteristic/), [Entity](../entity/)<br>
**Children**: [Property](../property/)

## [Uncertainty](../uncertainty/)
**Parents**: [Measurand](../measurand/), [Measurement](../measurement/)<br>
**Children**: [Expanded Uncertainty](../expanded_uncertainty/), [In-situ Observation](../in-situ_observation/), [Reference](../reference/), [Standard Uncertainty](../standard_uncertainty/), [Thematic Uncertainty](../thematic_uncertainty/), [Traceability](../traceability/)

## [User](../user/)
**Parents**: [Data](../data/), [Entity](../entity/), [Information](../information/)

## [Validation](../validation/)
**Parents**: [Data](../data/)

## [Value](../value/)
**Children**: [Band Central Wavelength](../band_central_wavelength/), [In-situ Observation](../in-situ_observation/), [Observation](../observation/)

## [Vertical Levels](../vertical_levels/)
**Parents**: [Model](../model/)

