Splunk Lookups
==============

Description.

## Table of Contents
* [**Data Sources**](#data-sources)
* [**Format**](#format)
* [**Setup**](#setup)
* [**Usage**](#usage)
* [**Background & Motivation**](#background-motivation)
* [**License**](#license)
* [**Notes**](#notes)

## Data Sources



## Format



## Setup



## Usage



## Background & Motivation

Project background and motivation.

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/). a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). Read more about the license, and my other disclaimers, [at my website](https://zacs.site/disclaimers.html).

---

## Notes

- Download public DNS resolvers (https://public-dns.info/). Search for destinations DNS hosts in that list, and destination hosts not in that list (https://www.splunk.com/en_us/blog/security/lookup-before-you-go-go-hunting.html)
- AWS IP ranges (https://ip-ranges.amazonaws.com/ip-ranges.json)
- GCP IP ranges (https://www.gstatic.com/ipranges/cloud.json)
- Azure IP ranges (https://www.microsoft.com/en-us/download/details.aspx?id=56519)
- Port to service mappings (https://www.speedguide.net/port.php?port=0)
- Cloudflare IPv4 (https://www.cloudflare.com/ips-v4)
- Cloudflare IPv6 (https://www.cloudflare.com/ips-v6)
- TOR exit nodes
	- Scrape all tar.xz files from here: metrics.torproject.org/collector/archive/exit-lists/
	- Extract, parse, and ingest them in Splunk to create a historical Tor node lookup.
	- This page talks about the project:
	- 2019.www.torproject.org/projects/tordnsel.html.en
	- Each entry contains the relay fingerprint (field #1), the date it was published (field #2), the date it was contained in a network status update (field #3), the exit node's IP (field #4), and the date that exit IP was recorded in a network test (field #5).
- Other CSPs (https://github.com/nsacyber/HTTP-Connectivity-Tester/issues/2)
- DoD IP space