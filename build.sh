curl -o cifar-10-python.tar.gz https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
mkdir cifar-data
tar -xzvf cifar-10-python.tar.gz -C cifar-data
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt