# Plans for data provision
In this section we relay current plans for data access once we move on to data releases. This is subject to change, the current version was updated in August 2024.

##### Timeline
The most up-to-date status of the project and timeline can be found [here](https://www.lsst.org/about/project-status).
As of writing this gives roughly:

- First light end of March 2025
  - DP1 (first data preview release) 2-3 months later, ~June-July 2025
  - Survey start 4-7 months later, ~August-November 2025
  - DP2 (second data preview) 9-12 months later, ~January-March 2026

- First data release (DR1) anticipated 12-14 months after survey start
  - Roughly late 2026- early 2027

##### Data Location
All data will be accessible through the Rubin Science Platform and the TAP protocol, however we are planning to transfer significant amounts of this data to NERSC. The current plan is to transfer the following list of static science datasets. Contact Matt Becker and Nacho Sevilla with questions/concerns. 

- coadd object catalogs as flat files
- metadetection shear catalogs as flat files
- cell-based coadds for the main survey 
- cell-based coadds for the deep-drilling fields
- survey masks
- survey property maps
- catalogs of stars used for the PSF model fits w/ moments measurements for those stars and the models of them
- PSF models for the images (visits)
- astrometric solutions for the images
- smaller amounts of final visit images for TD analysis 
- small amounts of raw data w/ butler for reprocessing tests
- visit metadata / AuxTel information

DESC-generated data will be stored primarily at NERSC. 


##### How do I do XYZ?
One commonly asked question is - where do I perform my analysis? The answer to that depends on the type of data you need access to and the computational resources required, but here are some examples compiled by Ignacio Sevilla.

| I want to                        | I would use             | Comments                                       |
|:---------------------------------|:------------------------|:-----------------------------------------------|
| Quickly visualize images         | The RSP                 |                                                |
| Overlay catalogs over coadd images for testing (small sample sizes)| RSP | Do NOT download Rubin catalogs to NERSC yourself! Do NOT upload large amounts of DESC internal data products to the RSP | 
| Run TXPipe over a big catalog    | NERSC                   |                                                |
| Run MCMC analyses                | NERSC                   |                                                |
| Run exploratory data analysis on DESC's derived data products and internal catalogs | NERSC notebooks | |
| Run cosmological simulations or mocks | NERSC + other HPC resources | Should be co-ordinated across DESC to reduce duplication | 
| Run extensive image and SSI sims | NERSC + other collaboration resources in France + UK | Should be co-ordinated across DESC to reduce duplication |
| Look at commissioning data as part of the Rubin in-kind program | RSP + USDF | Non-public data CANNOT be moved from the USDF to NERSC. Only DESC members in commissioning teams or on the project can have access to non-public data. | 

##### What not to do
Please do not:
- download large amounts of Rubin data to NERSC yourself
- upload large amounts of DESC data to the RSP
- move embargoed and/or non-public Rubin data from the USDF to NERSC
- move embargoed and/or non-public DESC data to public places
- generate large amounts of simulated data on NERSC file systems without coordinating with your DESC colleagues

##### Feedback and Support
Any data issues should be first reported within DESC to the SRV group, through the desc-srv slack channel. This allows us to keep track of issues, to alert you to ongoing discussions, and to inform relevant working groups.

Questions which require expertise beyond DESC can then be addressed to the Rubin Community Science team, through community.lsst.io (support category). This is monitored daily and is the official first point of call for questions and emergent issues. Internally Rubin will escalate these to Jira issues for DM support if work is required to answer or fix an issue.

Feedback and improvement suggestions should similarly be first reported to DESC via the SRV group so that DESC can keep track and highlight important feedback. Feedback on the project data should then be directed to the Rubin Users Committee, which is tasked with soliciting feedback and recommending improvements in twice-yearly reports. You can contact them via email at RubinObs-Users-Committee@lists.lsst.org, via the Rubin Community Forum (start with community.lsst.org and then send a direct message to the @Users-Committee group), or via the google form at forms.gle/km4VS2r2uYrvJ2w58.

Note that for significant data issues or algorithm suggestions, it may be best to talk to various working groups within DESC to get a better idea of the science impact and potential solutions before discussing this with Rubin. Rubin staff will need to analyse these factors and conduct a technical feasibility analysis for the User Committee to make their recommendations, so by providing this information in our requests we better enable Rubin to effectively prioritize the requests and decide on updates. In this case, as always, please first contact the desc-srv channel, who will work with you to inititate DESC-wide discussions.
