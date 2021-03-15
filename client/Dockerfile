FROM node:lts-alpine

RUN mkdir -p /client/node_modules

WORKDIR /client

COPY package*.json ./

RUN npm install

CMD npm run serve
