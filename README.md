
# Variability of dissolved inorganic carbon in the largest karst estuarine lagoon system of the southern Gulf of Mexico

### José Andrés Martínez-Trejo<sup>1</sup>, Jose-Gilberto Cardoso-Mohedano<sup>2,*</sup>, Joan Albert Sanchez-Cabeza<sup>3</sup>, José Martin Hernández Ayón<sup>4</sup>, Ana Carolina Ruiz-Fernández<sup> 3 </sup>, Mario Alejandro Gómez-Ponce <sup>2</sup> , Linda Barranco-Servín<sup>5</sup>, Daniel Pech<sup>5</sup>

<sup> 1 </sup> Posgrado en Ciencias del Mar y Limnología, Universidad Nacional Autónoma de México; Avenida Ciudad Universitaria 3000, C.P. 04510, Coyoacán, Ciudad de México, Méxic

<sup> 2 </sup>  Estación el Carmen, Instituto de Ciencias del Mar y Limnología, Universidad Nacional Autónoma de México, Carretera Carmen-Puerto Real km. 9.5, 24157 Ciudad del Carmen, Campeche, México

<sup> 3 </sup>  Unidad Académica Mazatlán, Instituto de Ciencias del Mar y Limnología, Universidad Nacional Autónoma de México, Calzada Joel Montes Camarena s/n, Colonia Playa Sur, Mazatlán 82000, Sinaloa, México

<sup> 4 </sup>  Instituto de Investigaciones Oceanológicas, Universidad Autónoma de Baja California, Km. 103 CarreteraTijuana-Ensenada, Ensenada, Baja California, México

<sup> 5 </sup> Laboratorio de Biodiversidad Marina y Cambio Climático (BIOMARCCA), El Colegio de la Frontera Sur, Lerma, Campeche, México. 

 \*Corresponding Author: gcardoso@cmarl.unam.mx Phone:+52-938-38-31847

[doi:XXXXX](https://XXXX)

_________________________________________________________________________________________

We thank GitHub Copilot for helping us code with the "Access free GitHub Education" program, which improved our coding productivity.
_________________________________________________________________________________________

## Climatological Year of Temperature and Salinity Variation (2016-2018)

This repository contains data and model simulations for the climatological year of temperature and salinity variation throughout 2016-2018.

## Data Field

The data is located in the file 'data\salinity_terminos_marina_delft3d.csv', which contains the following columns:

- Date_GMT_00 (for each year)
- Conductivity_microsiemens_cm
- Temp_C
- Conductivity_microsiemens_cm_average

## Climatological Data

The climatological data includes:

- Temp_C_average
- Conductivity_microsiemens_cm_average

These measurements were taken every 30 minutes using Onset U24-001 Conductivity Data Logger sensors (HOBO) at the Ciudad del Carmen Observatory 1, located at the Carmen Coastal Observatory (18°37'54.04"N, 91°49'55.15"W), in Marina Port of the Ciudad del Carmen, Campeche[^1].

## Salinity Calculation

The salinity was calculated using a Python implementation of the Thermodynamic Equation of Seawater 2010[^2], assuming a constant sea level pressure of 0.

## Model Data

This repository also includes temperature and salinity results from a 3D hydrodynamic model. This model was implemented at the Ecological Modelling Laboratory, Ciudad del Carmen, ICML, UNAM, using Delft3D 4.01.00[^2].

**Note:** 2016 is used as the reference year.

The model data includes:

- Time_model
- Salinity_psu_model
- Temperature_C_model

For further details, please refer to the article *In preparation* or contact Gilberto Cardoso[^4].

[^1]: Sanchez-Cabeza, J.A. et al. A low-cost long-term model of coastal observatories of global change. Journal of Operational Oceanography 12, (2019). https://doi.org/c4dp
[^2]: https://teos-10.github.io/GSW-Python/#gsw-python
[^3]: https://www.icmyl.unam.mx/el_carmen/quienes_somos/personal_academico/jose-gilberto-cardoso-mohedano
[^4]: https://blinq.me/YKZ9U8mqdr8n?bs=db

## References

- Humphreys, M. P., Lewis, E. R., Sharp, J. D., & Pierrot, D. (2022). PyCO2SYS v1.8: Marine carbonate system calculations in Python. Geoscientific Model Development, 15(1), 15–43. https://doi.org/10.5194/gmd-15-15-2022
- Millero, F. J. (2010). Carbonate constants for estuarine waters. Marine and Freshwater Research, 61(2), 139. https://doi.org/10.1071/MF09254
- Wolf-Gladrow, D. A., Zeebe, R. E., Klaas, C., Körtzinger, A., & Dickson, A. G. (2007). Total alkalinity: The explicit conservative expression and its application to biogeochemical processes. Marine Chemistry, 106(1–2), 287–300. https://doi.org/10.1016/j.marchem.2007.01.006