FROM python:latest
WORKDIR /home/jupyter/20k_docgen/src
RUN pip install jinja2
COPY ./src/docugen.py /home/jupyter/20k_docgen/src
CMD python docugen.py