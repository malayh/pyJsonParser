#!/usr/bin/python3.6
import json
import argparse
import sys
import re




"""
WARNING:
    1) keys in the json cannot contain "."

Reserved Key words:
    1) FOR_EACH_KEY: run one command iterativly

Exit codes:
    1 : File not found
    2 : bad json file
    3 : key error
"""


def getArguments():
    parser=argparse.ArgumentParser()
    mxgroup = parser.add_mutually_exclusive_group(required=True)
    mxgroup.add_argument("-k",help="Get Keys")
    mxgroup.add_argument("-v",help="Get Values")
    mxgroup.add_argument("-t",help="Get type")
    parser.add_argument("--validate",help="Validate input json file and print errors",action="store_true")
    parser.add_argument("file",help="Input Json file.")
    args=parser.parse_args()
    return args

def parseKeys(keyStr):
    return [x for x in re.split(r'\.(?=\w+)',keyStr) if x!='' and x!='.']

def getKeys(jData,keys):
    """
    Throws error is jData is not subscriptable
    """
    if keys:
        k=keys.pop(0)
        if type(jData) is list:
            getKeys(jData[int(k)],keys)
        else:
            getKeys(jData[k],keys)
    else:
        if type(jData) is list:
            for i in range(len(jData)):
                print(i)
        else:
            for i in jData.keys():
                print(i)

def getType(jData,keys):
    """
    Throws error is jData is not subscriptable
    """
    if keys:
        k=keys.pop(0)
        if type(jData) is list:
            getType(jData[int(k)],keys)
        else:
            getType(jData[k],keys)

    else:
        print(re.match(r'<class\s\'(\w+)\'>',str(type(jData))).group(1))

def getValue(jData,keys):
    """
    Throws error is jData is not subscriptable
    """
    if keys:
        k=keys.pop(0)
        if type(jData) is list:
            getValue(jData[int(k)],keys)
        else:
            getValue(jData[k],keys)

    else:
        print(jData)

def main():
    args=getArguments()

    try:
        jData=json.loads(open(args.file).read())
    except FileNotFoundError as e:
        if args.validate:
            print(e)
        sys.exit(1)
    except json.decoder.JSONDecodeError as e:
        if args.validate:
            print(e)
        sys.exit(2)

    try:
        if args.t:
            keys=parseKeys(args.t)
            getType(jData,keys)
        elif args.v:
            keys=parseKeys(args.v)
            getValue(jData,keys)
        elif args.k:
            keys=parseKeys(args.k)
            getKeys(jData,keys)

    except KeyError as e:
        if args.validate:
            print("Invalid key: {}".format(e))
        sys.exit(3)
    except TypeError as e:
        if args.validate:
            print("Invalid key: {}".format(e))
        sys.exit(3)
    except AttributeError as e:
        if args.validate:
            print("Invalid key: {}".format(e))
        sys.exit(3)
    except IndexError as e:
        if args.validate:
            print("Invalid key: {}".format(e))
        sys.exit(3)


if __name__=="__main__":
    main()
