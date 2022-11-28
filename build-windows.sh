curl -o cifar-10-python.tar.gz https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
mkdir cifar-data
tar -xzvf cifar-10-python.tar.gz -C cifar-data
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt