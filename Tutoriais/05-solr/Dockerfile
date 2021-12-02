FROM solr:8.10
COPY . .
EXPOSE 8983
#CMD bin/solr create_core -c courses 
CMD ["bin/solr", "start", "-p", "8983"]