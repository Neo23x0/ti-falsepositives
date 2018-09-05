# ti-falsepositives
A collection of typical false positive indicators

## Why?

Over the years, I've compiled a list of typical false positive hashes that are often included in IOC lists 

My favourites are: 
- file that contains 1 byte 0x0a 
- empty Word documents 
- 1x1 JPEG tracking pixel

## Content

1. False Positive Hashes : fp-hashes.py
2. False Positive Domains : (on the roadmap)

## Why Python?

- XML has too much overhead
- JSON doesn't support comments
- YAML is good, maybe I'll transform it some day
- I and I suppose that many others use Python scripts to process indicators of compromise
