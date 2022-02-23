FROM public.ecr.aws/lambda/python:3.8

RUN yum -y update && yum -y install libXScrnSaver gtk2 gtk3 alsa-lib.x86_64 alsa-lib-devel tar
RUN pip install --upgrade pip setuptools

ENV PLAYWRIGHT_BROWSERS_PATH=/playwright/bin
RUN mkdir -p $PLAYWRIGHT_BROWSERS_PATH

COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN playwright install chromium

COPY ./playwright_super_driver ./

CMD ["lambda_function.lambda_handler"]
