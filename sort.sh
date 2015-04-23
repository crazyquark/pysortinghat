#!/bin/bash
python3 /myhome/dev/pysortinghat/src/sort.py /storage/_completed/ /storage/_Media/Movies/ /storage/_Media/TV/
curl --data-binary '{ "jsonrpc": "2.0", "method": "VideoLibrary.Scan", "id": "mybash"}' -H 'content-type: application/json;' http://192.168.1.213:8080/jsonrpc
echo ''
