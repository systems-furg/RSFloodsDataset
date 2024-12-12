# RSFLOODING datasets

# Internet Resilience in Rio Grande do Sul, May 2024 Flooding Event
README version: 1.2, last modified: 2024-12-12.

In May 2024, Rio Grande do Sul, Brazil's southernmost state, endured weeks of severe rainfall, causing extensive infrastructure damage in more than 400 cities. The flooding impacted roads, bridges, electrical plants, data centers, communication systems, and homes, disrupting the lives of millions. This repository contains datasets used to analyze the effects of these climatic events on the resilience of Internet infrastructure in the region and its subsequent recovery.

# References

IMC-2024 [Poster: Building Comprehensive Telecommunications Datasets
During a Major Climatic Event](https://github.com/systems-furg/RSFloodsDataset/blob/main/IMC2024-poster.pdf)

PAM-2025 [Analyzing the Efect of an Extreme Weather Event on Telecommunications and Information Technology: Insights from 30 Days of Flooding] (https://github.com/systems-furg/RSFloodsDataset/blob/main/IMC2024-poster.pdf)

## Overview

This repository provides data from various vantage points to support the analyses presented in the accompanying paper. The study investigates the impact of these disruptions on different aspects of Internet infrastructure, including:

- **Metropolitan network backbone**: Analyzes the outages and recoveries within a major metropolitan network.
- **Data centers**: Focuses on the operational resilience and failure patterns of local data centers.
- **Internet Exchange Point (IXP)**: Explores how the IXP in Rio Grande do Sul was affected during the flooding.
- **Brazilian National Research and Education Network (RNP) backbone**: Looks into the disruptions experienced by the research network's backbone.
- **Bandwidth measurements from ISPs**: Contains end-user bandwidth measurement data, highlighting the performance from various ISPs during the crisis.

The study involves non-anonymized datasets from public sources, as well as anonymized data from private entities, all of which have been obtained with the required consent. No personal or sensitive information is included. The main objective is to educate and promote learning in a neutral and non-judgmental manner.

## Datasets

- **Metropolitan Network Backbone Dataset**  
  Contains data on outages and recovery times for major metropolitan networks in Rio Grande do Sul.
  
- **Data Centers Outage Dataset**  
  Provides records of failures and recovery events for data centers operating in the affected areas.

- **Internet Exchange Point (IXP) Dataset**  
  Captures traffic and operational logs from the IXP in Rio Grande do Sul, showing the impact of the flooding.

- **Brazilian National Research and Education Network (RNP) Dataset**  
  Data on the backbone of the RNP, detailing network performance, downtimes, and recovery periods.

- **ISP Bandwidth Measurements Dataset**  
  Contains bandwidth and network performance measurements from end-users across different Internet Service Providers (ISPs).

**NOTE:** Some of the datasets are currently unavailable due to pending authorization. The integrity of the data was ensured through collaborative efforts between academic institutions and private operators, built on transparency and trust through interdisciplinary partnerships. 

<!---
## How to Use

1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/internet-resilience-rs-2024.git


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
-->



