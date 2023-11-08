#!/bin/bash

cd src/repositories
rm geckodriver
cd ..
cd ..
cd ..
tar xvzf geckodriver-v0.33.0-linux64.tar.gz
mv geckodriver hh_parsing/src/repositories/
tar xvjf firefox-87.0.tar.bz2
cd hh_parsing/src/

echo "Parsing of data is started: "
python main.py