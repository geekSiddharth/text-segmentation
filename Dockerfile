FROM  ufoym/deepo:pytorch-py27
MAINTAINER Siddharth Yadav "siddharth16268@iiitd.ac.in"
RUN apt-get update \
    && apt-get install -y python-pip  python-dev build-essential
COPY . /app
WORKDIR /app

RUN pip install cython
RUN pip install numpy scipy gensim ipython
RUN pip install tqdm pathlib2 segeval tensorboard_logger flask flask_wtf nltk
RUN pip install pandas xlrd xlsxwriter termcolor

VOLUME        ["/datadrive/sid/"]









