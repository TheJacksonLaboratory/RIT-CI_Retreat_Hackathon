# RIT-CI_Retreat_Hackathon
The following data sources can be integrated with this Github Repo:


Torque Logs
- Helix, Cadillac, Gilber, Exome
These PBX logs will be converted to JSON.

Slurm Logs Accounting DB
- Sumner, Winter

Singularity Reg/Builder
- jaxreg
- ctbuilder (cachedOCI blobs)

Storage Reports
- Tier 1-3 (Primary Sources)
- Tier 0?

Spacewalk (BH, CT)
- System Config

RStudio/RShiny
- Hosted Apps

Bright

Active Directory

ServiceNow

LibreNMS

Greglog

Grafana

Facilities (Power)


Commands:

docker pull mcr.microsoft.com/azure-cli

docker run -it -v/opt/prod/sregistry:/sreg mcr.microsoft.com/azure-cli


To bind the storage from the host to the container:

az login -u first.last@jax.org -p password

az storage copy -r -s /source/ -d /destination
