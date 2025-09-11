FROM node:20
USER root

COPY ./ /frontend
COPY ./package.json /frontend
RUN apt-get update && apt-get install -y curl

RUN apt-get -yq update \
    && apt-get -yq upgrade \
    && apt install -yq nodejs \
    && apt install -yq npm

RUN npm install -g react-devtools \
    && npm install -g serve

# RUN apt-get install --no-install-recommends apt-utils --yes \
#     && apt-get install --no-install-recommends npm --yes

EXPOSE 3000
RUN rm -rf /frontend/node_modules

WORKDIR /frontend
# CMD ["/bin/bash","-i","/bin/run.sh"]
RUN npm install
RUN npm ci

RUN echo "NPM: " && npm -v
RUN echo "NODE: " && node -v
# RUN npm start
RUN npm run build

CMD ["serve", "-s", "build"]
# RUN serve -s build
