# jenkins.yaml file generator on JCAC(Jenkins Configuration as Code)
JCac doesn't provide the export jenkins.yaml by API.
This tool will get the jenkins.yaml file from the jenkins jcac url.

# How to use
```
python3 jcac-yamlexporter.py --url https://jenkins.example.com/configuration-as-code/viewExport --user admin --password password
```