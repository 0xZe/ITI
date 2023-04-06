# 1-base img

FROM nginx:alpine

# 2-steps to setup environment 

#change default html content in index.html
COPY ./index.html /usr/share/nginx/html/index.html

#change nginx default port in default.conf
COPY ./default.conf  /etc/nginx/conf.d/default.conf

# 3-container starting command
#(nginx img has already default starting command that i don't want to edit its behaviour)