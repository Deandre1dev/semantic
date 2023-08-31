FROM pypy:latest
RUN pip3 install spacy==${SPACY_VERSION}
RUN python3 -m spacy.${LANG}.download all
RUN pip3 install python -m spacy download en_core_web_md
WORKDIR /app
COPY . /app
CMD python semantic.py
