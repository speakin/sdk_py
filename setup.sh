#/bin/bash
cd openapi
pip install -r requirements.txt
python setup.py install
cd ../tok
python setup.py install 

