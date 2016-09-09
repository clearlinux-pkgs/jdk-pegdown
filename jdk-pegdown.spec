Name     : jdk-pegdown
Version  : 1.4.2
Release  : 1
URL      : https://github.com/sirthias/pegdown/archive/1.4.2.tar.gz
Source0  : https://github.com/sirthias/pegdown/archive/1.4.2.tar.gz
Source1  : http://repo1.maven.org/maven2/org/pegdown/pegdown/1.4.2/pegdown-1.4.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-apache-parent
BuildRequires : jdk-aqute-bndlib
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-beanutils
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-digester
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-commons-validator
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-eclipse-eclipse
BuildRequires : jdk-eclipse-osgi
BuildRequires : jdk-eclipse-osgi-services
BuildRequires : jdk-felix
BuildRequires : jdk-felix-bundlerepository
BuildRequires : jdk-felix-framework
BuildRequires : jdk-felix-osgi-foundation
BuildRequires : jdk-felix-utils
BuildRequires : jdk-glassfish-servlet-api
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-jtidy
BuildRequires : jdk-kxml
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-bundle-plugin
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-dependency-tree
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-jar-plugin
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-reporting-impl
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-osgi-compendium
BuildRequires : jdk-osgi-core
BuildRequires : jdk-parboiled
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy-java
BuildRequires : jdk-surefire
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xmlunit
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn
Patch1: pegdown-rhbz1096735.patch

%description
Introduction
------------
_pegdown_ is a pure Java library for clean and lightweight [Markdown] processing based on a [parboiled] PEG parser.

%prep
%setup -q -n pegdown-1.4.2
%patch1 -p1

find . -name "*.class" -delete
find . -name "*.jar" -delete

cp -p %{SOURCE1} pom.xml

python3 /usr/share/java-utils/pom_editor.py pom_xpath_inject   "pom:project" "

<build>
  <plugins>

  </plugins>
</build>"

python3 /usr/share/java-utils/pom_editor.py pom_xpath_inject   "pom:build" "

<resources>
  <resource>
    <directory>.</directory>
    <targetPath>\${project.build.outputDirectory}/META-INF</targetPath>
    <includes>
      <include>LICENSE</include>
      <include>NOTICE</include>
    </includes>
  </resource>
</resources>"

python3 /usr/share/java-utils/pom_editor.py pom_add_plugin     org.apache.maven.plugins:maven-jar-plugin . "

<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
    <manifest>
      <addDefaultImplementationEntries>true</addDefaultImplementationEntries>
      <addDefaultSpecificationEntries>true</addDefaultSpecificationEntries>
    </manifest>
  </archive>
</configuration>"

python3 /usr/share/java-utils/pom_editor.py pom_add_plugin     org.apache.felix:maven-bundle-plugin . "

<extensions>true</extensions>
<configuration>
  <instructions>
    <Built-By>\${user.name}</Built-By>
    <Bundle-SymbolicName>org.pegdown</Bundle-SymbolicName>
    <Bundle-Name>pegdown</Bundle-Name>
    <Bundle-Vendor>pegdown.org</Bundle-Vendor>
    <Bundle-Version>\${project.version}</Bundle-Version>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>"

rm -r src/test/scala/*
python3 /usr/share/java-utils/pom_editor.py pom_remove_dep org.specs2:specs2_2.9.3
python3 /usr/share/java-utils/mvn_file.py :pegdown pegdown

%build
python3 /usr/share/java-utils/mvn_build.py

%install
xmvn-install  -R .xmvn-reactor -n pegdown-1.4.2 -d %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/java/pegdown.jar
/usr/share/maven-metadata/pegdown-1.4.2.xml
/usr/share/maven-poms/pegdown.pom
