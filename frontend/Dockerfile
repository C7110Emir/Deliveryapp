FROM node:alpine

WORKDIR /app/frontend

COPY package.json  yarn.lock /app/frontend/

RUN yarn install && yarn cache clean

COPY . /app/frontend

CMD ["yarn", "run", "start"]
