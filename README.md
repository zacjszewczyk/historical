hisTORical
==========

This project builds a historical list of Tor exit nodes.

## Table of Contents
* [**Data Sources**](#data-sources)
* [**Format**](#format)
* [**Usage**](#usage)
* [**Background & Motivation**](#background-motivation)
* [**License**](#license)
* [**Notes**](#notes)

## Data Sources

*hisTORical* scrapes data from [the CollecTor project](metrics.torproject.org/collector/archive/exit-lists/). As of October, 2020, these archives go back to February, 2010.

## Format

*histTORical* generates a CSV file. Each row contains the relay fingerprint (field #1), the date it was published (field #2), the date it was contained in a network status update (field #3), the exit node's IP (field #4), and the date that exit IP was recorded in a network test (field #5).

## Usage

To build the CSV, just run `tor.py`; within about 15 minutes, the script will have built the historical list of Tor exit nodes and saved it as `tor.csv` in the current working directory.

As of October, 2020, *hisTORical* builds a 12GB CSV file with well over 100,000,000 rows. This is not usable in typical spreadsheet applications. Using this resource either requires scripting, or the use of a SIEM designed to handle large datasets. I prefer [Splunk](https://www.splunk.com); run the command below to ingest the CSV file into a local Splunk instance:

```
/opt/splunk/bin/splunk add oneshot ./tor.csv -sourcetype csv -index main
```

## Background & Motivation

This project enables Incident Responders to build a list of known Tor exit nodes. When conducting analysis days or weeks after an event occurred, the Tor Project's [lists](https://blog.torproject.org/changes-tor-exit-list-service) will not suffice: by then, any nodes involved in the compromise may have aged off. By collecting *all* Tor exit nodes and stamping them with the time they were active, though, analysts can easily identify all nodes active during a given time period and then quickly confirm or deny their use during the compromise. 

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/). Read more about the license, and my other disclaimers, [at my website](https://zacs.site/disclaimers.html). Generally speaking, this license allows individuals to remix this work provided they release their adaptation under the same license and cite this project as the original, and prevents anyone from turning this work or its derivatives into a commercial product.