FROM python:3.9-buster
ENV PYTHONUNBUFFERED 1
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -

RUN apt-get update && apt-get install -y \
    apt-utils \
    postgresql-client \
    gdal-bin \
    libgdal-dev \
    libspatialindex-dev \
    nodejs

RUN npm install --global yarn

RUN apt-get install -y wget gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf libxss1 libcairo2 libpangocairo-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /code
WORKDIR /code
COPY Pipfile Pipfile.lock /code
RUN pip install pipenv && pipenv install --system 

COPY . /code/
CMD ["uwsgi", "--ini", "uwsgi.ini" ]
