# Stage1 ( build react-app executable files )

# 1-base img
FROM node:alpine AS build-stage

# 2-steps to setup environment
WORKDIR /app 

#COPY  ./react-app/package.json . (additional step but not necessary)

COPY ./react-app/. .

RUN npm install

# the command that build the executable files
RUN npm run build 

# 3-container starting command 
ENTRYPOINT npm start

#===============================================================================================

# Stage2 ( take react-app executable files (that have built in stage1) to be served into nginx )

# 1-base img
FROM nginx:alpine

# 2-steps to setup environment
COPY --from=build-stage /app/build/. /usr/share/nginx/html

# 3-container starting command
#(nginx img has already default starting command that i don't want to edit its behaviour)

#===============================================================================================