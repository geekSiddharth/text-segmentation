FROM library/python:2

MAINTAINER Siddharth Yadav "siddharth16268@iiitd.ac.in"

RUN pip install http://download.pytorch.org/whl/cu80/torch-0.3.0-cp27-cp27mu-linux_x86_64.whl
RUN pip install cython numpy scipy gensim ipython jupyter tqdm pathlib2 segeval tensorboard_logger flask flask_wtf nltk pandas xlrd xlsxwriter termcolor

VOLUME  ["/datadrive/sid/"]









