#!/bin/bash
/myhome/dev/pysortinghat/src/sort.py /storage/_completed/ /storage/\!Media/Movies/ /storage/\!Media/TV/
curl --data-binary '{ "jsonrpc": "2.0", "method": "VideoLibrary.Scan", "id": "mybash"}' -H 'content-type: application/json;' http://192.168.1.63/jsonrpc
echo ''
