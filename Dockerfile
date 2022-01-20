FROM registry.esss.lu.se/ics-docker/maven:openjdk-11
USER root
RUN mkdir -p /opt/openxal/lattice/
COPY current /opt/openxal/lattice/current
COPY design /opt/openxal/lattice/design
COPY tracewin /opt/openxal/lattice/tracewin
RUN mkdir -p /etc/openxal/ && echo "mainPath=/opt/openxal/lattice/design/main.xal" >> /etc/openxal/xal.smf.data.prefs
ADD https://gitlab.esss.lu.se/ess-crs/openxal/-/raw/site.ess.master/third-party-libs/lib/libhdf5_java.so /usr/lib/libhdf5_java.so
USER maven
