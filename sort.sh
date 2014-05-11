#!/bin/bash
/myhome/dev/pysortinghat/src/sort.py /storage/CompletedDownloads/ /storage/\!Media/Movies/ /storage/\!Media/TV/
curl --data-binary '{ "jsonrpc": "2.0", "method": "VideoLibrary.Scan", "id": "mybash"}' -H 'content-type: application/json;' http://xbian:8080/jsonrpc
echo ''
