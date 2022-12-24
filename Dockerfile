FROM python:3.7.9-slim
RUN pip install python-binance==1.0.15
RUN pip install numpy==1.21.5
RUN pip install pandas==21.0.1