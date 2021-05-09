# Dataset

### Environment
ubuntu-20.04.2.0

### Installation
#### Dependency
```python
# Install Java 1.8 or up
$ sudo apt-get install g++ openjdk-8-jdk python3-dev python3-pip curl
# Install pandas
sudo apt-get install python3-pandas
# Install pptx, pdf processor
pip3 install python-pptx
pip3 install pdfminer
```
#### Install KoNLPy
```python
$ python3 -m pip install --upgrade pip
$ python3 -m pip install konlpy # Python 3.x

# Install Mecab
$ sudo apt-get install curl git
$ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)﻿
```

#### Usage for Google NL API
##### 1. Install client library
```python
pip install --upgrade google-cloud-language
```
##### 2. Download key.json from google cloud console
##### 3. Set Path
```python
export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
```
##### 4. Install Google Cloud SDK
```python
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
sudo apt-get install apt-transport-https ca-certificates gnupg
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
sudo apt-get update && sudo apt-get install google-cloud-sdk
```
##### 5. Start : 
```python
gcloud init
```




