FROM public.ecr.aws/docker/library/python:3.7
RUN  mkdir WORK_DIR
RUN  cd  WORK_DIR
WORKDIR  /WORK_DIR
ENV TEST_GROUP="getters or not getters"
COPY ./pyproject.toml /WORK_DIR/pyproject.toml
COPY ./requirements.txt /WORK_DIR/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./core /WORK_DIR/core
COPY ./tests /WORK_DIR/tests
CMD py.test --junitxml=test_reports/test_report.xml  --cache-clear -v -m "${TEST_GROUP}" tests
