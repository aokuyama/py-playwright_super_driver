FROM public.ecr.aws/lambda/python:3.8 as build
RUN yum install -y unzip
RUN curl -O https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip \
  && mkdir -p /usr/share/fonts/NotoSansCJKjp \
  && unzip NotoSansCJKjp-hinted.zip -d /usr/share/fonts/NotoSansCJKjp/ \
  && rm NotoSansCJKjp-hinted.zip

FROM public.ecr.aws/lambda/python:3.8

COPY --from=build /usr/share/fonts/NotoSansCJKjp /usr/share/fonts

RUN yum -y update && yum -y install libXScrnSaver gtk2 gtk3 alsa-lib.x86_64 alsa-lib-devel tar
RUN pip install --upgrade pip setuptools

ENV PLAYWRIGHT_BROWSERS_PATH=/playwright/bin
RUN mkdir -p $PLAYWRIGHT_BROWSERS_PATH

COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN playwright install chromium

COPY ./playwright_super_driver ./

CMD ["lambda_function.lambda_handler"]
