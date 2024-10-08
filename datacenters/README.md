# RSFLOODING: Porto Alegre Metropolitan Network Datacenters location and flooding status

README version: 1, last modified: 2024-09-11.

This file describes the datacenters dataset “dcs-flooding-state.csv,” generated on 2024-05-24. It describes the status of each datacenter and its location in the flooding area.

## Contents
- CSV Data File Metadata

## Metadata

| **Field**                 | **Description**                                                                                     |
|---------------------------|-----------------------------------------------------------------------------------------------------|
| **dataSetName**            | dcs-flooding-state.csv                                                                    |
| **status**                 | ufrgs                                                                                    |
| **shortDesc**              | Datacenters CSV dataset                                                                                 |
| **longDesc**               | Describes the location and datacenters states, if turned off during the event by any reason. All cases were validated with datacenter operators. |
| **datasetClass**           | Irrestricted                                                                                        |
| **commercialAllowed**      | true                                                                                               |
| **requestReviewRequired**  | true                                                                                               |
| **productReviewRequired**  | true                                                                                              |
| **ongoingMeasurement**     | false                                                                                              |
| **submissionMethod**       | Upload                                                                                             |
| **collectionStartDate**    | 2024-05-24                                                                                        |
| **collectionStartTime**    | 00:00:00                                                                                           |
| **collectionEndDate**      | 2024-05-24                                                                                         |
| **collectionEndTime**      | 00:00:00                                                                                           |
| **anonymization**          | none                                                                                               |
| **archivingAllowed**       | false                                                                                              |
| **keywords**               | category:internet-topology-data, subcategory:physical-location, event-status                 |
| **format**                 | CSV file                                                                                           |
| **access**                 | https                                                                                              |
| **providerName**           | UFRGS                                                                                              |
| **byteSize**               | 1069                                                                                          |
| **expirationDays**         | none                                                                                               |
| **uncompressedSize**       | 1069                                                                                               |
| **Doi**                    | not-yet-registered                                                                                 |
| **useAgreement**           | false                                                                                              |
| **irbRequired**            | false                                                                                              |
| **UsageInstructions**      | Community available dataset |



### CSV Content

| **Metadata**     | **Description**                                                                 |
|------------------|---------------------------------------------------------------------------------|
| **Flooding-state**    | Indicates the current status of flooding at different data centers. Two possible values are on (online during the event), or off (offline at least for one day).                                             |
| **Datacenter**      | Datacenter identification.                                     |
| **Address**      | Physical address location                              |
| **City**     | City Identification                    |
| **CC**       | Contry code                                         |
| **Website**  | Datacenter company website |


            
## Citation

If you use this dataset to conduct additional research, please cite it as:
 
```bibtex
@inproceedings{bertholdo2024building,
  author    = {Leandro Márcio Bertholdo and Renan Barreto Paredes and Pedro de Botelho Marcos},
  title     = {Poster: Building Comprehensive Telecommunications Datasets During a Major Climatic Event},
  booktitle = {Proceedings of the 2024 ACM Internet Measurement Conference (IMC '24)},
  year      = {2024},
  month     = nov,
  location  = {Madrid, Spain},
  publisher = {ACM},
  address   = {New York, NY, USA},
  pages     = {2},
  url       = {https://doi.org/10.1145/3646547.3689677},
  doi       = {10.1145/3646547.3689677}
}
