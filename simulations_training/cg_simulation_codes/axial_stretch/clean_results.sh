#!/usr/bin/sh

for i in $(ls -d ./*/);do
rm $i/results/*
done

