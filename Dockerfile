FROM registry.esss.lu.se/ics-docker/maven:openjdk-11
USER root
RUN mkdir -p /opt/openxal/lattice/
COPY current /opt/openxal/lattice/current
COPY design /opt/openxal/lattice/design
COPY tracewin /opt/openxal/lattice/tracewin
USER maven
