PKG_NAME := jdk-pegdown
URL := https://github.com/sirthias/pegdown/archive/1.4.2.tar.gz
ARCHIVES := http://repo1.maven.org/maven2/org/pegdown/pegdown/1.4.2/pegdown-1.4.2.pom %{buildroot}

include ../common/Makefile.common
