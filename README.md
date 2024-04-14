# Gen AI Hackathon
Repository of Picipolo team for Accenture's TechFest Hackathon.

## Authors

* Mikołaj Gałkowski
* Wiktor Jakubowski
* Łukasz Tomaszewski

## Installation
The application is already provisioned and availble under the following [link](todo). To set it up yourself, follow the steps:
1. Deploy GenAI model (based on LangChain Agent) per instructions in `agent-api` README.
2. Deploy Streamlit application with chatbot (make sure to copy API URL as environment variable) per instructions in `app` README.

## Risk Analysis

Risk analysis is perfomed in two-ways:
1. Software Risk analysis.
This is performed using GitGuardian software. It checks for any vulnerabilities in the existing source code, including Common Vulnerabilities and Exposures, outdated libraries, license issues etc.

2. Infrastructure risk analysis.
This is performed using Azure Security Center. It is a service provided by Azure cloud to monitor deployed resources. It inspects vulnerabilities and suggests recommendations for provided resources.
