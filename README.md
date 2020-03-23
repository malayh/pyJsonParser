# pyJsonParser

This is a small command line utility I build to parse json files. Beacause I don't like reading configutaion text files. 
JSON is easy to understan an deal with. JSON is <3.

# Usage
```
usage: pyJSONParser.py [-h] (-k K | -v V | -t T) [--validate] file

positional arguments:
  file        Input Json file.

optional arguments:
  -h, --help  show this help message and exit
  -k K        Get Keys
  -v V        Get Values
  -t T        Get type
  --validate  Validate input json file and print errors
```

# How does keys look like

For the below json file named file.json
```
{
  "abc":"some value",
  "key2":{
    "key3":"value2",
    "key4":"value3",
  },
  "key5":[1,2,3]
}
```
The following are few exmples of how this works
```
./pyJSONParser.py file.json -v /abc 
some value

./pyJSONParser.py file.json -k /
abc
key2
key5

./pyJSONParser.py file.json -k /key5
0
1
2

./pyJSONParser.py file.json -v /key2/key3
value2

./pyJSONParser.py file.json -v /key5/1
2
```
