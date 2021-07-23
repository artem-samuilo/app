FROM nginx
WORKDIR code
COPY ./code/index.html /code
COPY ./nginx-conf/nginx-front.conf /etc/nginx/conf.d/default.conf
CMD ["nginx", "-g", "daemon off;"]