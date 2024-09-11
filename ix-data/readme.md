# RSFLOODING: Porto Alegre IXP Dataset 

README version: 1, last modified: 2024-09-11.

This file describes the IPv4 routing dataset “bird.zip,” generated on 2024-05-24, provided by IX.br. It captures the routing view of the participant at poa.ix.br with two route servers (x.x.x.253 and x.x.x.254) during the period from 2024-04-16 to 2024-05-24. The data is real and non-anonymized.

## Contents
- Bird router MRT Dump File Metadata



## Metadata

| Field                     | Description                                                                                     |
|---------------------------|-------------------------------------------------------------------------------------------------|
| **dataSetName**            | poa.ix.br_2024-04-16_2024-05-24                                        |
| **status**                 | ufrgs_and_ixbr                                                                             |
| **shortDesc**              | Bird Router MRT dataset                                                        |
| **longDesc**               | Describes the IPv4 routing dataset “bird.zip,” generated on 2024-05-24, provided by IX.br. It captures the routing view of the participant at poa.ix.br with two route servers (x.x.x.253 and x.x.x.254) during the period from 2024-04-16 to 2024-05-24. The data is real and non-anonymized. |
| **datasetClass**           | Irrestricted                                                                        |
| **commercialAllowed**      | true                                                                                           |
| **requestReviewRequired**  | true                                                                                           |
| **productReviewRequired**  | false                                                                                          |
| **ongoingMeasurement**     | false                                                                                          |
| **submissionMethod**       | Upload                                                                                         |
| **collectionStartDate**    | 2024-04-16                                                                                     |
| **collectionStartTime**    | 15:46:00                                                                                       |
| **collectionEndDate**      | 2024-05-24                                                                                     |
| **collectionEndTime**      | 17:07:00                                                                                       |                                                                                 |
| **anonymization**          | none                                                                                           |
| **archivingAllowed**       | false                                                                                          |
| **keywords**               | category:internet-topology-data, subcategory:ixp-data, address-collection, topology  |
| **format**                 | MRTDump zipped file                                                                                        |
| **access**                 | https                                                                                                                                                                 |
| **providerName**           | UFRGS                                                                                            |                                                                           |
| **byteSize**               | 988190709                                                                                       |
| **expirationDays**         | none                                                                                             |
| **uncompressedSize**       | 5.4G                                                                                      |
| **Doi**              | not-yet-registered                                                                          |
| **useAgreement**           | false                                                                                  |
| **irbRequired**            | false                                                                                          |
| **UsageInstructions** | Community available dataset. Please cite [https://doi.org/10.1145/3646547.3689677](https://doi.org/10.1145/3646547.3689677)




## Dataset Contents and Usage

If you use this dataset, Please, use for reference the DOI https://doi.org/10.1145/3646547.3689677.

The unzipped file contains MRT dumps from poa.ix.br in the format ixp_yyyy-mm-dd_hhmm.mrt. Each dump have 10 minutes sample. 

**Usage**
<pre>
bgpdump -m ixp_2024-05-24_11h51m.mrt | head
2024-09-11 11:47:25 [info] logging to syslog
TABLE_DUMP2|1716551500|B|177.52.38.253|26162|189.89.82.0/24|16735 263009 263009 263009 263009 262749|INCOMPLETE|177.52.38.24|200|20|16735:111 16735:7000 16735:7315 16735:10211 16735:10221 26162:16735 26162:65051|NAG||
TABLE_DUMP2|1716551500|B|177.52.38.254|26162|189.89.82.0/24|16735 263009 263009 263009 263009 262749|INCOMPLETE|177.52.38.24|200|20|16735:111 16735:7000 16735:7315 16735:10211 16735:10221 26162:16735 26162:65051|NAG||
</pre>

### MRTDump Content

| **Metadata**     | **Description**                                                                 |
|------------------|---------------------------------------------------------------------------------|
| **Timestamp**    | The time when the data was recorded.                                             |
| **Peer IP**      | IP address of the BGP peer sending the route.                                    |
| **Peer AS Number**| Autonomous System (AS) number of the peer.                                      |
| **AS Path**      | Sequence of AS numbers that the route has traversed.                             |
| **Next Hop**     | IP address of the next router in the path to the destination.                    |
| **Origin**       | Route origin (IGP, EGP, or INCOMPLETE).                                          |
| **Communities**  | Tags applied to the route for policy control (e.g., BGP communities).            |
| **Local Preference & MED** | Metrics for internal path selection and preference.                   |
| **Prefix**       | Destination network (e.g., `192.168.0.0/24`).                                    |
| **Message Types**| `TABLE_DUMP`, `BGP4MP`, and `STATE_CHANGE` messages indicating routing states.   |
| **Flags**        | Indicators of route status or conditions.                                        |
| **MRT Header**   | Information about the type, subtype, and record length of the message.           

