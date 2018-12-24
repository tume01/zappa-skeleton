FROM lambci/lambda:build-python3.6
ENV PYTHONUNBUFFERED 1

WORKDIR /var/task
# Fancy prompt to remind you are in zappashell
RUN echo 'export PS1="\[\e[36m\]zappashell>\[\e[m\] "' >> /root/.bashrc

#Additional RUN commands here
RUN yum clean all && \
    yum -y install mysql-devel

#python requirements
ADD requirements.txt /var/task
RUN cd /var && python -m venv django-environment
RUN source /var/django-environment/bin/activate && pip install -r requirements.txt

# Add project source
ADD . /var/task
