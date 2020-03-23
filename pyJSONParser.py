#!/usr/bin/python3


"""
Copyright (c) 2020 Malay Hazarika (malay.hazarika@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import json
import argparse
import sys
import re

"""
Exit codes:
    1 : File not found
    2 : bad json file
    3 : key error
"""


TESTING_MODE=False


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
    return [x for x in re.split(r'/(?=\w+)',keyStr) if x!='' and x!='/']


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

def test():
    pass

if __name__=="__main__":
    if not TESTING_MODE:
        main()
    else:
        test()
