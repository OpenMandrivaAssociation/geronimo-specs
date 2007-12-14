# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define gcj_support 1 

%define _without_tests 1
%define without_tests %{?_without_tests:1}%{!?_without_tests:0}
%define with_tests %{!?_without_tests:1}%{?_without_tests:0}


%define bname           geronimo
%define section         free
                                                                                
Summary:        Geronimo J2EE server J2EE specifications
URL:            http://geronimo.apache.org


Name:           geronimo-specs
Version:        1.1
Release:        %mkrel 4.0.1
Epoch:          0
License:        Apache License
Group:          Development/Java
Source0:        %{name}-%{version}-src.tar.gz
# svn export https://svn.apache.org/repos/asf/geronimo/specs/tags/1_1/

Source1:        %{name}-jpp-depmap.xml

Patch1:        geronimo-specs-j2ee-management-pom.patch
Patch2:        geronimo-specs-pom_xml.patch
Patch3:        geronimo-jaxr-noscout-pom.patch
Patch4:        geronimo-nomockobjects-noscout-pom.patch
Patch5:        geronimo-jms-nomockobjects-pom.patch
Patch6:        geronimo-corba-jacorb-pom.patch

BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  java-1.7.0-icedtea
BuildRequires:  maven2 >= 0:2.0.4
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven-shared-file-management
BuildRequires:  sed
BuildRequires:  saxon
BuildRequires:  saxon-scripts
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-one
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-surefire
BuildRequires:  excalibur-avalon-logkit
BuildRequires:  mojo-maven2-plugin-idlj
#BuildRequires:  jacorb >= 0:2.2.3
%if %{with_tests}
BuildRequires:  junit >= 0:3.8.1
BuildRequires:  mockobjects >= 0:0.09
BuildRequires:  mockobjects < 0:0.10
BuildRequires:  mockobjects-jdk1.4-j2ee1.4 >= 0:0.09
BuildRequires:  mockobjects-jdk1.4-j2ee1.4 < 0:0.10
%endif
BuildRequires:  mx4j >= 0:2.0.1
#BuildRequires:  ws-scout 

Requires:  mx4j >= 0:2.0.1
Requires:  avalon-logkit
#Requires:  juddi 

# The main package has links to all specs, so it requires all subpackages
# except j2ee-schema (not linked) and javadocs
Requires: geronimo-commonj-1.1-apis = %{version}-%{release}
Requires: geronimo-jaf-1.0.2-api = %{version}-%{release}
Requires: geronimo-corba-1.0-apis = %{version}-%{release}
Requires: geronimo-corba-2.3-apis = %{version}-%{release}
Requires: geronimo-corba-3.0-apis = %{version}-%{release}
Requires: geronimo-ejb-2.1-api = %{version}-%{release}
Requires: geronimo-j2ee-1.4-apis = %{version}-%{release}
Requires: geronimo-j2ee-connector-1.5-api = %{version}-%{release}
Requires: geronimo-j2ee-deployment-1.1-api = %{version}-%{release}
Requires: geronimo-jacc-1.0-api = %{version}-%{release}
Requires: geronimo-j2ee-management-1.0-api = %{version}-%{release}
Requires: geronimo-javamail-1.3.1-api = %{version}-%{release}
Requires: geronimo-jaxr-1.0-api = %{version}-%{release}
Requires: geronimo-jaxrpc-1.1-api = %{version}-%{release}
Requires: geronimo-jms-1.1-api = %{version}-%{release}
Requires: geronimo-jsp-2.0-api = %{version}-%{release}
Requires: geronimo-jta-1.0.1B-api = %{version}-%{release}
Requires: geronimo-qname-1.1-api = %{version}-%{release}
Requires: geronimo-saaj-1.1-api = %{version}-%{release}
Requires: geronimo-servlet-2.4-api = %{version}-%{release}
Obsoletes:      geronimo-specs-compat
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Geronimo is Apache's ASF-licenced J2EE server project.
These are the J2EE-Specifications
Note: You should use the subpackages for the Specifications
that you actually need.  The ones installed by the main package
are deprecated and will disapear in future releases.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java

%description javadoc
Javadoc for %{name}.

%package -n geronimo-commonj-1.1-apis
Summary:        CommonJ APIs
Group:          Development/Libraries/Java
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}

%description -n geronimo-commonj-1.1-apis
CommonJ Spec

%package -n geronimo-jaf-1.0.2-api
Summary:        J2EE JAF v1.0.2 API
Group:          Development/Java
Provides:       jaf = 0:1.0.2
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}
# Don't obsolete jaf, classpathx-jaf provides it
# Don't even obsolete it versioned, as sun-jaf is at 1.1
#Obsoletes:    jaf
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-jaf-1.0.2-api
Java Activation Framework

%package -n geronimo-corba-1.0-apis
Summary:        CORBA v1.0 APIs
Group:          Development/Java
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}

%description -n geronimo-corba-1.0-apis
CORBA 1.0 Spec

%package -n geronimo-corba-2.3-apis
Summary:        CORBA v2.3 APIs
Group:          Development/Java
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}

%description -n geronimo-corba-2.3-apis
CORBA 2.3 Spec

%package -n geronimo-corba-3.0-apis
Summary:        CORBA v3.0 APIs
Group:          Development/Java
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}

%description -n geronimo-corba-3.0-apis
CORBA 3.0 Spec

%package -n geronimo-ejb-2.1-api
Summary:        J2EE EJB v2.1 API
Group:          Development/Java
Provides:       ejb = 0:2.1
Obsoletes:      ejb
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-ejb-2.1-api
Enterprise JavaBeans Specification

%package -n geronimo-j2ee-1.4-apis
Summary:        J2EE v1.4 APIs
Group:          Development/Java
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}

%description -n geronimo-j2ee-1.4-apis
J2EE Specification (the complete set in one jar)

%package -n geronimo-j2ee-connector-1.5-api
Summary:        J2EE Connector v1.5 API
Group:          Development/Java
Provides:       j2ee-connector = 0:1.5
Obsoletes:      j2ee-connector
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-j2ee-connector-1.5-api
J2EE Connector Architecture Specification

%package -n geronimo-j2ee-deployment-1.1-api
Summary:        J2EE Deployment v1.1 API
Group:          Development/Java
Provides:       j2ee-deployment = 0:1.1
Obsoletes:      j2ee-deployment
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-j2ee-deployment-1.1-api
J2EE Application Deployment Specification

%package -n geronimo-jacc-1.0-api
Summary:        J2EE JACC v1.0 API
Group:          Development/Java
#Provides:      geronimo-jacc-1.0-api
Provides:       jacc = 0:1.0
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-jacc-1.0-api
Java Authorization Contract for Containers Specification

%package -n geronimo-j2ee-management-1.0-api
Summary:        J2EE Management v1.0 API
Group:          Development/Java
Provides:       j2ee-management = 0:1.0
Obsoletes:      j2ee-management
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-j2ee-management-1.0-api
J2EE Application Management Specification

%package -n geronimo-javamail-1.3.1-api
Summary:        J2EE JavaMail v1.3.1 API
Group:          Development/Java
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}
# Do not provide it as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
# FIXME: figure out what to do with this
#Provides:      javamail = 0:1.3.1

%description -n geronimo-javamail-1.3.1-api
JavaMail API

%package -n geronimo-jaxr-1.0-api
Summary:        J2EE JAXR v1.0 API
Group:          Development/Java
Provides:       jaxr = 0:1.0
Provides:       jaxr-api
Obsoletes:      jaxr-api
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-jaxr-1.0-api
Java API for XML Registries (JAXR)

%package -n geronimo-jaxrpc-1.1-api
Summary:        J2EE JAXRPC v1.1 API
Group:          Development/Java
Provides:       jaxrpc = 0:1.1
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-jaxrpc-1.1-api
Java API for XML-Based RPC (JAXRPC)

%package -n geronimo-jms-1.1-api
Summary:        J2EE JMS v1.1 API
Group:          Development/Java
Provides:       jms = 0:1.1
Obsoletes:      jms
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post):  update-alternatives

%description -n geronimo-jms-1.1-api
JMS Specification

%package -n geronimo-jsp-2.0-api
Summary:        J2EE JSP v2.0 API
Group:          Development/Java
Provides:       jsp = 0:2.0
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-jsp-2.0-api
JavaServer Pages Specification

%package -n geronimo-jta-1.0.1B-api
Summary:        J2EE JTA v1.0.1B API
Group:          Development/Java
Provides:       jta = 0:1.0.1B
# Don't obsolete jta, as this is provided by java-1.4.2-gcj-compat
#Obsoletes:    jta
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-jta-1.0.1B-api
Java Transaction API Specification

%package -n geronimo-qname-1.1-api
Summary:        Namespace v1.1 API
Group:          Development/Java
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}
Requires(preun):  update-alternatives
Requires(post):  update-alternatives


%description -n geronimo-qname-1.1-api
javax.xml.namespace.QName API

%package -n geronimo-saaj-1.1-api
Summary:        J2EE SAAJ v1.1 API
Group:          Development/Java
Provides:       saaj = 0:1.1
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-saaj-1.1-api
SOAP with Attachments API for Java (SAAJ)

%package -n geronimo-servlet-2.4-api
Summary:        J2EE Servlet v2.4 API
Group:          Development/Java
Provides:       servlet = 0:2.4
Requires:       %{name}-poms = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-servlet-2.4-api
J2EE Servlet v2.4 API

%package poms
Summary:        POM files for geronimo-specs
Group:          Development/Tools
Requires(post):   jpackage-utils >= 1.7.3
Requires(postun): jpackage-utils >= 1.7.3

%description poms
The Project Object Model files for the geronimo-specs modules.

%prep
%setup -q -n %{name}-%{version}
chmod -R go=u-w *
mkdir etc
cp %{bname}-spec-activation/LICENSE.txt etc
mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav
%patch4 -b .sav2
%patch5 -b .sav
#%patch6 -b .sav

%build
export JAVA_HOME=%{_jvmdir}/java-icedtea

# Mock objects is sort of a specia case  since it does not reside in 
# /usr/share/java. So we install it manually via maven.

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

#mvn-jpp install:install-file \
#    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
#    -DgroupId=mockobjects \
#    -DartifactId=mockobjects-jdk1.4-j2ee1.3 \
#    -Dversion=0.09 \
#    -Dpackaging=jar \
#    -Dfile=$(build-classpath mockobjects-j2ee1.4)

# Start building

mvn-jpp \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.test.failure.ignore=true \
    -Dmaven2.jpp.depmap.file=%{SOURCE1} \
%if %{without_tests}
    -Dmaven.test.skip=true \
%endif
    install javadoc:javadoc

pushd geronimo-spec-j2ee
mvn-jpp \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.test.failure.ignore=true \
    -Dmaven2.jpp.depmap.file=%{SOURCE1} \
%if %{without_tests}
    -Dmaven.test.skip=true \
%endif
    install
popd

%install
rm -rf $RPM_BUILD_ROOT

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository

# Directory for poms
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

# subpackage jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -p -m 0644 geronimo-spec-activation/target/geronimo-activation_1.0.2_spec-1.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-jaf-1.0.2-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-jaf-1.0.2-api-%{version}.jar geronimo-jaf-1.0.2-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/jaf.jar # for %ghost
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-activation_1.0.2_spec/1.1/geronimo-activation_1.0.2_spec-1.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-jaf-1.0.2-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-activation_1.0.2_spec 1.1 JPP geronimo-jaf-1.0.2-api

install -p -m 0644 geronimo-spec-corba-2.3/target/geronimo-corba_2.3_spec-1.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-corba-2.3-apis-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-corba-2.3-apis-%{version}.jar geronimo-corba-2.3-apis.jar
popd
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-corba_2.3_spec/1.1/geronimo-corba_2.3_spec-1.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-corba-2.3-apis.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-corba_2.3_spec 1.1 JPP geronimo-corba-2.3-apis

install -p -m 0644 geronimo-spec-corba-3.0/target/geronimo-corba_3.0_spec-1.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-corba-3.0-apis-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-corba-3.0-apis-%{version}.jar geronimo-corba-3.0-apis.jar
popd
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-corba_3.0_spec/1.1/geronimo-corba_3.0_spec-1.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-corba-3.0-apis.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-corba_3.0_spec 1.1 JPP geronimo-corba-3.0-apis

install -p -m 0644 geronimo-spec-corba/target/geronimo-spec-corba-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-corba-1.0-apis-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-corba-1.0-apis-%{version}.jar geronimo-corba-1.0-apis.jar
popd
cp $MAVEN_REPO_LOCAL/geronimo-spec/geronimo-spec-corba/1.0/geronimo-spec-corba-1.0.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-corba-1.0-apis.pom
%add_to_maven_depmap geronimo-spec geronimo-spec-corba 1.0 JPP geronimo-corba-1.0-apis

install -p -m 0644 geronimo-spec-ejb/target/geronimo-ejb_2.1_spec-1.0.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-ejb-2.1-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-ejb-2.1-api-%{version}.jar geronimo-ejb-2.1-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/ejb.jar # for %ghost
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-ejb_2.1_spec/1.0.1/geronimo-ejb_2.1_spec-1.0.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-ejb-2.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-ejb_2.1_spec 1.0.1 JPP geronimo-ejb-2.1-api

install -p -m 0644 geronimo-spec-j2ee-connector/target/geronimo-j2ee-connector_1.5_spec-1.0.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-j2ee-connector-1.5-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-j2ee-connector-1.5-api-%{version}.jar \
    geronimo-j2ee-connector-1.5-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/j2ee-connector.jar # for %ghost
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-j2ee-connector_1.5_spec/1.0.1/geronimo-j2ee-connector_1.5_spec-1.0.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-j2ee-connector-1.5-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-j2ee-connector_1.5_spec 1.0.1 JPP geronimo-j2ee-connector-1.5-api

install -p -m 0644 geronimo-spec-j2ee-deployment/target/geronimo-j2ee-deployment_1.1_spec-1.0.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-j2ee-deployment-1.1-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-j2ee-deployment-1.1-api-%{version}.jar \
    geronimo-j2ee-deployment-1.1-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/j2ee-deployment.jar # for %ghost
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-j2ee-deployment_1.1_spec/1.0.1/geronimo-j2ee-deployment_1.1_spec-1.0.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-j2ee-deployment-1.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-j2ee-deployment_1.1_spec 1.0.1 JPP geronimo-j2ee-deployment-1.1-api

install -p -m 0644 geronimo-spec-j2ee-jacc/target/geronimo-j2ee-jacc_1.0_spec-1.0.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-jacc-1.0-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-jacc-1.0-api-%{version}.jar geronimo-jacc-1.0-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/jacc.jar # for %ghost
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-j2ee-jacc_1.0_spec/1.0.1/geronimo-j2ee-jacc_1.0_spec-1.0.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-jacc-1.0-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-j2ee-jacc_1.0_spec 1.0.1 JPP geronimo-jacc-1.0-api

install -p -m 0644 geronimo-spec-j2ee-management/target/geronimo-j2ee-management_1.0_spec-1.0.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-j2ee-management-1.0-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-j2ee-management-1.0-api-%{version}.jar \
    geronimo-j2ee-management-1.0-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/j2ee-management.jar # for %ghost
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-j2ee-management_1.0_spec/1.0.1/geronimo-j2ee-management_1.0_spec-1.0.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-j2ee-management-1.0-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-j2ee-management_1.0_spec 1.0.1 JPP geronimo-j2ee-management-1.0-api

install -p -m 0644 geronimo-spec-javamail/target/geronimo-javamail_1.3.1_spec-1.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-javamail-1.3.1-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-javamail-1.3.1-api-%{version}.jar \
    geronimo-javamail-1.3.1-api.jar
popd
# Do not provide it as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
#touch $RPM_BUILD_ROOT%{_javadir}/javamail.jar # for %ghost
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-javamail_1.3.1_spec/1.1/geronimo-javamail_1.3.1_spec-1.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-javamail-1.3.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-javamail_1.3.1_spec 1.1 JPP geronimo-javamail-1.3.1-api

install -p -m 0644 geronimo-spec-jaxr/target/geronimo-jaxr_1.0_spec-1.0.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-jaxr-1.0-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-jaxr-1.0-api-%{version}.jar geronimo-jaxr-1.0-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/jaxr.jar # for %ghost
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-jaxr_1.0_spec/1.0.1/geronimo-jaxr_1.0_spec-1.0.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-jaxr-1.0-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-jaxr_1.0_spec 1.0.1 JPP geronimo-jaxr-1.0-api

install -p -m 0644 geronimo-spec-jaxrpc/target/geronimo-jaxrpc_1.1_spec-1.0.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-jaxrpc-1.1-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-jaxrpc-1.1-api-%{version}.jar geronimo-jaxrpc-1.1-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/jaxrpc.jar # for %ghost
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-jaxrpc_1.1_spec/1.0.1/geronimo-jaxrpc_1.1_spec-1.0.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-jaxrpc-1.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-jaxrpc_1.1_spec 1.0.1 JPP geronimo-jaxrpc-1.1-api

install -p -m 0644 geronimo-spec-j2ee/target/geronimo-j2ee_1.4_spec-1.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-j2ee-1.4-apis-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-j2ee-1.4-apis-%{version}.jar geronimo-j2ee-1.4-apis.jar
popd
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-j2ee_1.4_spec/1.1/geronimo-j2ee_1.4_spec-1.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-j2ee-1.4-apis.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-j2ee_1.4_spec 1.1 JPP geronimo-j2ee-1.4-apis

install -p -m 0644 geronimo-spec-jms/target/geronimo-jms_1.1_spec-1.0.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-jms-1.1-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-jms-1.1-api-%{version}.jar geronimo-jms-1.1-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/jms.jar # for %ghost
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-jms_1.1_spec/1.0.1/geronimo-jms_1.1_spec-1.0.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-jms-1.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-jms_1.1_spec 1.0.1 JPP geronimo-jms-1.1-api

install -p -m 0644 geronimo-spec-jsp/target/geronimo-jsp_2.0_spec-1.0.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-jsp-2.0-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-jsp-2.0-api-%{version}.jar geronimo-jsp-2.0-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/jsp.jar # for %ghost
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-jsp_2.0_spec/1.0.1/geronimo-jsp_2.0_spec-1.0.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-jsp-2.0-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-jsp_2.0_spec 1.0.1 JPP geronimo-jsp-2.0-api

install -p -m 0644 geronimo-spec-jta/target/geronimo-jta_1.0.1B_spec-1.0.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-jta-1.0.1B-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-jta-1.0.1B-api-%{version}.jar geronimo-jta-1.0.1B-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/jta.jar # for %ghost
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-jta_1.0.1B_spec/1.0.1/geronimo-jta_1.0.1B_spec-1.0.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-jta-1.0.1B-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-jta_1.0.1B_spec 1.0.1 JPP geronimo-jta-1.0.1B-api

install -p -m 0644 geronimo-spec-qname/target/geronimo-qname_1.1_spec-1.0.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-qname-1.1-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-qname-1.1-api-%{version}.jar geronimo-qname-1.1-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/qname.jar # for %ghost
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-qname_1.1_spec/1.0.1/geronimo-qname_1.1_spec-1.0.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-qname-1.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-qname_1.1_spec 1.0.1 JPP geronimo-qname-1.1-api

install -p -m 0644 geronimo-spec-saaj/target/geronimo-saaj_1.1_spec-1.0.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-saaj-1.1-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-saaj-1.1-api-%{version}.jar geronimo-saaj-1.1-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/saaj.jar # for %ghost
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-saaj_1.1_spec/1.0.1/geronimo-saaj_1.1_spec-1.0.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-saaj-1.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-saaj_1.1_spec 1.0.1 JPP geronimo-saaj-1.1-api

install -p -m 0644 geronimo-spec-servlet/target/geronimo-servlet_2.4_spec-1.0.1.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-servlet-2.4-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-servlet-2.4-api-%{version}.jar geronimo-servlet-2.4-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/servlet.jar # for %ghost
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-servlet_2.4_spec/1.0.1/geronimo-servlet_2.4_spec-1.0.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-servlet-2.4-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-servlet_2.4_spec 1.0.1 JPP geronimo-servlet-2.4-api

install -p -m 0644 geronimo-spec-commonj/target/geronimo-commonj_1.1_spec-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-commonj-1.1-apis-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-commonj-1.1-apis-%{version}.jar geronimo-commonj-1.1-apis.jar
popd
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/geronimo-commonj_1.1_spec/1.0/geronimo-commonj_1.1_spec-1.0.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-commonj-1.1-apis.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-commonj_1.1_spec 1.0 JPP geronimo-commonj-1.1-apis

# Add the parent geronimo-specs pom
cp $MAVEN_REPO_LOCAL/org/apache/geronimo/specs/specs/1.1/specs-1.1.pom \
  $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-geronimo-specs.pom
%add_to_maven_depmap org.apache.geronimo.specs specs 1.1 JPP geronimo-specs

# main package jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/geronimo
pushd $RPM_BUILD_ROOT%{_javadir}/geronimo
  ln -sf ../geronimo-commonj-1.1-apis-%{version}.jar spec-commonj-1.1-%{version}.jar
  ln -sf spec-commonj-1.1-%{version}.jar spec-commonj-1.1.jar

  ln -sf ../geronimo-jaf-1.0.2-api-%{version}.jar spec-jaf-1.0.2-%{version}.jar
  ln -sf spec-jaf-1.0.2-%{version}.jar spec-jaf-1.0.2.jar

  ln -sf ../geronimo-ejb-2.1-api-%{version}.jar spec-ejb-2.1-%{version}.jar
  ln -sf spec-ejb-2.1-%{version}.jar spec-ejb-2.1.jar

  ln -sf ../geronimo-j2ee-connector-1.5-api-%{version}.jar \
    spec-j2ee-connector-1.5-%{version}.jar
  ln -sf spec-j2ee-connector-1.5-%{version}.jar spec-j2ee-connector-1.5.jar

  ln -sf ../geronimo-j2ee-deployment-1.1-api-%{version}.jar \
    spec-j2ee-deployment-1.1-%{version}.jar
  ln -sf spec-j2ee-deployment-1.1-%{version}.jar spec-j2ee-deployment-1.1.jar

  ln -sf ../geronimo-jacc-1.0-api-%{version}.jar spec-jacc-1.0-%{version}.jar
  ln -sf spec-jacc-1.0-%{version}.jar spec-jacc-1.0.jar

  ln -sf ../geronimo-j2ee-management-1.0-api-%{version}.jar \
    spec-j2ee-management-1.0-%{version}.jar
  ln -sf spec-j2ee-management-1.0-%{version}.jar spec-j2ee-management-1.0.jar

  ln -sf ../geronimo-j2ee-1.4-apis-%{version}.jar spec-j2ee-1.4-%{version}.jar
  ln -sf spec-j2ee-1.4-%{version}.jar spec-j2ee-1.4.jar

  ln -sf ../geronimo-jms-1.1-api-%{version}.jar spec-jms-1.1-%{version}.jar
  ln -sf spec-jms-1.1-%{version}.jar spec-jms-1.1.jar

  ln -sf ../geronimo-jsp-2.0-api-%{version}.jar spec-jsp-2.0-%{version}.jar
  ln -sf spec-jsp-2.0-%{version}.jar spec-jsp-2.0.jar

  ln -sf ../geronimo-jta-1.0.1B-api-%{version}.jar spec-jta-1.0.1B-%{version}.jar
  ln -sf spec-jta-1.0.1B-%{version}.jar spec-jta-1.0.1B.jar

  ln -sf ../geronimo-servlet-2.4-api-%{version}.jar spec-servlet-2.4-%{version}.jar
  ln -sf spec-servlet-2.4-%{version}.jar spec-servlet-2.4.jar
popd

#install -p -m 0644 modules/j2ee-schema/target/geronimo-j2ee-schema-1.0-M4.jar \
#          $RPM_BUILD_ROOT%{_javadir}/geronimo/spec-j2ee-schema-1.0-M4.jar
#pushd $RPM_BUILD_ROOT%{_javadir}/geronimo
#  ln -sf spec-j2ee-schema-1.0-M4.jar spec-j2ee-schema-1.0.jar
#popd

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
for sp in activation commonj corba corba-2.3 corba-3.0 corba ejb j2ee-connector j2ee-deployment j2ee-management javamail jaxrpc jaxr jms jsp jta qname saaj servlet; do
    install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/${sp}
    cp -pr geronimo-spec-${sp}/target/site/apidocs/* \
         $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/${sp}
done
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jacc
cp -pr geronimo-spec-j2ee-jacc/target/site/apidocs/* \
         $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jacc
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} 


%{__perl} -pi -e 's/\r$//g' `find . -name LICENSE.txt` 

%if %{gcj_support}
mv $RPM_BUILD_ROOT%{_javadir}/geronimo-j2ee-1.4-apis-%{version}.jar .
%{_bindir}/aot-compile-rpm
mv geronimo-j2ee-1.4-apis-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/geronimo-j2ee-1.4-apis-%{version}.jar
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post poms
%update_maven_depmap

%postun poms
%update_maven_depmap

%triggerpostun -n geronimo-jaf-1.0.2-api -- classpathx-jaf <= 0:1.0-2jpp_4rh
# Remove file from old non-free packages
rm -f %{_javadir}/jaf.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/jaf %{_javadir}/jaf.jar

%post -n geronimo-jaf-1.0.2-api
/usr/sbin/update-alternatives --install %{_javadir}/jaf.jar jaf %{_javadir}/geronimo-jaf-1.0.2-api.jar 10002
%if %{gcj_support}
%{update_gcjdb}
%endif


%preun -n geronimo-jaf-1.0.2-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove jaf %{_javadir}/geronimo-jaf-1.0.2-api.jar
fi

%if %{gcj_support}
%postun -n geronimo-jaf-1.0.2-api
%{clean_gcjdb}
%endif

%if %{gcj_support}
%post -n geronimo-commonj-1.1-apis
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun -n geronimo-commonj-1.1-apis
%{clean_gcjdb}
%endif

%if %{gcj_support}
%post -n geronimo-corba-1.0-apis
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun -n geronimo-corba-1.0-apis
%{clean_gcjdb}
%endif

%if %{gcj_support}
%post -n geronimo-corba-2.3-apis
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun -n geronimo-corba-2.3-apis
%{clean_gcjdb}
%endif

%if %{gcj_support}
%post -n geronimo-corba-3.0-apis
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun -n geronimo-corba-3.0-apis
%{clean_gcjdb}
%endif


%triggerpostun -n geronimo-ejb-2.1-api -- ejb <= 0:2.1-3jpp_2rh
# Remove file from old non-free packages
rm -f %{_javadir}/ejb.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/ejb %{_javadir}/ejb.jar

%post -n geronimo-ejb-2.1-api
/usr/sbin/update-alternatives --install %{_javadir}/ejb.jar ejb %{_javadir}/geronimo-ejb-2.1-api.jar 20100
%if %{gcj_support}
%{update_gcjdb}
%endif


%preun -n geronimo-ejb-2.1-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove ejb %{_javadir}/geronimo-ejb-2.1-api.jar
fi
%if %{gcj_support}
%postun -n geronimo-ejb-2.1-api
%{clean_gcjdb}
%endif


%triggerpostun -n geronimo-j2ee-connector-1.5-api -- j2ee-connector <= 0:1.5-3jpp_2rh
# Remove file from old non-free packages
rm -f %{_javadir}/j2ee-connector.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/j2ee-connector %{_javadir}/j2ee-connector.jar

%post -n geronimo-j2ee-connector-1.5-api
/usr/sbin/update-alternatives --install %{_javadir}/j2ee-connector.jar j2ee-connector %{_javadir}/geronimo-j2ee-connector-1.5-api.jar 10500
%if %{gcj_support}
%{update_gcjdb}
%endif

%preun -n geronimo-j2ee-connector-1.5-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove j2ee-connector %{_javadir}/geronimo-j2ee-connector-1.5-api.jar
fi

%if %{gcj_support}
%postun -n geronimo-j2ee-connector-1.5-api
%{clean_gcjdb}
%endif

%triggerpostun -n geronimo-j2ee-deployment-1.1-api -- j2ee-deployment <= 0:1.1-1jpp_1rh
# Remove file from old non-free packages
rm -f %{_javadir}/j2ee-deployment.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/j2ee-deployment %{_javadir}/j2ee-deployment.jar

%post -n geronimo-j2ee-deployment-1.1-api
/usr/sbin/update-alternatives --install %{_javadir}/j2ee-deployment.jar j2ee-deployment %{_javadir}/geronimo-j2ee-deployment-1.1-api.jar 10100
%if %{gcj_support}
%{update_gcjdb}
%endif

%preun -n geronimo-j2ee-deployment-1.1-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove j2ee-deployment %{_javadir}/geronimo-j2ee-deployment-1.1-api.jar
fi

%if %{gcj_support}
%postun -n geronimo-j2ee-deployment-1.1-api
%{clean_gcjdb}
%endif


%triggerpostun -n geronimo-jacc-1.0-api -- jacc <= 0:1.0-1jpp
# Remove file from old non-free packages
rm -f %{_javadir}/jacc.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/jacc %{_javadir}/jacc.jar

%post -n geronimo-jacc-1.0-api
/usr/sbin/update-alternatives --install %{_javadir}/jacc.jar jacc %{_javadir}/geronimo-jacc-1.0-api.jar 10000
%if %{gcj_support}
%{update_gcjdb}
%endif

%preun -n geronimo-jacc-1.0-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove jacc %{_javadir}/geronimo-jacc-1.0-api.jar
fi

%if %{gcj_support}
%postun -n geronimo-jacc-1.0-api
%{clean_gcjdb}
%endif

%triggerpostun -n geronimo-j2ee-management-1.0-api -- j2ee-management <= 0:1.0-1jpp_1rh
# Remove file from old non-free packages
rm -f %{_javadir}/j2ee-management.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/j2ee-management %{_javadir}/j2ee-management.jar

%post -n geronimo-j2ee-management-1.0-api
/usr/sbin/update-alternatives --install %{_javadir}/j2ee-management.jar j2ee-management %{_javadir}/geronimo-j2ee-management-1.0-api.jar 10000
%if %{gcj_support}
%{update_gcjdb}
%endif

%preun -n geronimo-j2ee-management-1.0-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove j2ee-management %{_javadir}/geronimo-j2ee-management-1.0-api.jar
fi

%if %{gcj_support}
%postun -n geronimo-j2ee-management-1.0-api
%{clean_gcjdb}
%endif

# Do not provide it as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
%if %{gcj_support}
%post -n geronimo-javamail-1.3.1-api
%{update_gcjdb}
%endif

#/usr/sbin/update-alternatives --install %{_javadir}/javamail.jar javamail %{_javadir}/geronimo-javamail-1.3.1-api.jar 10301
#
#%preun -n geronimo-javamail-1.3.1-api
#if [ "$1" = "0" ]; then
#    /usr/sbin/update-alternatives --remove javamail %{_javadir}/geronimo-javamail-1.3.1-api.jar
#fi

%if %{gcj_support}
%postun -n geronimo-javamail-1.3.1-api
%{clean_gcjdb}
%endif

%triggerpostun -n geronimo-jaxr-1.0-api -- jaxr-api <= 0:1.0-1jpp
# Remove file from old non-free packages
rm -f %{_javadir}/jaxr.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/jaxr %{_javadir}/jaxr.jar

%post -n geronimo-jaxr-1.0-api
/usr/sbin/update-alternatives --install %{_javadir}/jaxr.jar jaxr %{_javadir}/geronimo-jaxr-1.0-api.jar 10000
%if %{gcj_support}
%{update_gcjdb}
%endif

%preun -n geronimo-jaxr-1.0-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove jaxr %{_javadir}/geronimo-jaxr-1.0-api.jar
fi

%if %{gcj_support}
%postun -n geronimo-jaxr-1.0-api
%{clean_gcjdb}
%endif

%post -n geronimo-jaxrpc-1.1-api
/usr/sbin/update-alternatives --install %{_javadir}/jaxrpc.jar jaxrpc %{_javadir}/geronimo-jaxrpc-1.1-api.jar 10100
%if %{gcj_support}
%{update_gcjdb}
%endif

%preun -n geronimo-jaxrpc-1.1-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove jaxrpc %{_javadir}/geronimo-jaxrpc-1.1-api.jar
fi

%if %{gcj_support}
%postun -n geronimo-jaxrpc-1.1-api
%{clean_gcjdb}
%endif

%triggerpostun -n geronimo-jms-1.1-api -- jms <= 0:1.1-3jpp_2rh
# Remove file from old non-free packages
rm -f %{_javadir}/jms.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/jms %{_javadir}/jms.jar

%post -n geronimo-jms-1.1-api
/usr/sbin/update-alternatives --install %{_javadir}/jms.jar jms %{_javadir}/geronimo-jms-1.1-api.jar 10100
%if %{gcj_support}
%{update_gcjdb}
%endif

%preun -n geronimo-jms-1.1-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove jms %{_javadir}/geronimo-jms-1.1-api.jar
fi

%if %{gcj_support}
%postun -n geronimo-jms-1.1-api
%{clean_gcjdb}
%endif


%post -n geronimo-jsp-2.0-api
/usr/sbin/update-alternatives --install %{_javadir}/jsp.jar jsp %{_javadir}/geronimo-jsp-2.0-api.jar 20000
%if %{gcj_support}
%{update_gcjdb}
%endif

%preun -n geronimo-jsp-2.0-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove jsp %{_javadir}/geronimo-jsp-2.0-api.jar
fi

%if %{gcj_support}
%postun -n geronimo-jsp-2.0-api
%{clean_gcjdb}
%endif

%triggerpostun -n geronimo-jta-1.0.1B-api -- jta <= 0:1.0.1-0.b.3jpp_2rh
# Remove file from old non-free packages
rm -f %{_javadir}/jta.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/jta %{_javadir}/jta.jar

%post -n geronimo-jta-1.0.1B-api
/usr/sbin/update-alternatives --install %{_javadir}/jta.jar jta %{_javadir}/geronimo-jta-1.0.1B-api.jar 10001
%if %{gcj_support}
%{update_gcjdb}
%endif

%preun -n geronimo-jta-1.0.1B-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove jta %{_javadir}/geronimo-jta-1.0.1B-api.jar
fi

%if %{gcj_support}
%postun -n geronimo-jta-1.0.1B-api
%{clean_gcjdb}
%endif

%post -n geronimo-qname-1.1-api
/usr/sbin/update-alternatives --install %{_javadir}/qname.jar qname %{_javadir}/geronimo-qname-1.1-api.jar 10100
%if %{gcj_support}
%{update_gcjdb}
%endif

%postun -n geronimo-qname-1.1-api
  /usr/sbin/update-alternatives --remove qname %{_javadir}/geronimo-qname-1.1-api.jar
fi
%if %{gcj_support}
%{clean_gcjdb}
%endif

%post -n geronimo-saaj-1.1-api
/usr/sbin/update-alternatives --install %{_javadir}/saaj.jar saaj %{_javadir}/geronimo-saaj-1.1-api.jar 10100
%if %{gcj_support}
%{update_gcjdb}
%endif

%preun -n geronimo-saaj-1.1-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove saaj %{_javadir}/geronimo-saaj-1.1-api.jar
fi

%post -n geronimo-servlet-2.4-api
/usr/sbin/update-alternatives --install %{_javadir}/servlet.jar servlet %{_javadir}/geronimo-servlet-2.4-api.jar 20400
%if %{gcj_support}
%{update_gcjdb}
%endif

%preun -n geronimo-servlet-2.4-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove servlet %{_javadir}/geronimo-servlet-2.4-api.jar
fi

%if %{gcj_support}
%postun -n geronimo-servlet-2.4-api
%{clean_gcjdb}
%endif


%files
%defattr(-,root,root,-)
%doc etc/LICENSE.txt
%dir %{_javadir}/geronimo
%{_javadir}/geronimo/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.jar.*
%endif

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files poms
%defattr(-,root,root,-)
%{_mavendepmapfragdir}
%{_datadir}/maven2/poms

%files -n geronimo-commonj-1.1-apis
%defattr(-,root,root,-)
%{_javadir}/geronimo-commonj-1.1-apis*.jar
%doc geronimo-spec-commonj/LICENSE.txt
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-commonj-1.1-apis-%{version}.jar.*
%endif

%files -n geronimo-jaf-1.0.2-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-jaf-1.0.2-api*.jar
%doc geronimo-spec-activation/LICENSE.txt
%ghost %{_javadir}/jaf.jar
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-jaf-1.0.2-api-%{version}.jar.*
%endif

%files -n geronimo-corba-1.0-apis
%defattr(-,root,root,-)
%{_javadir}/geronimo-corba-1.0-apis*.jar
#%doc geronimo-spec-corba/LICENSE.txt
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-corba-1.0-apis-%{version}.jar.*
%endif

%files -n geronimo-corba-2.3-apis
%defattr(-,root,root,-)
%{_javadir}/geronimo-corba-2.3-apis*.jar
%doc geronimo-spec-corba-2.3/LICENSE.txt
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-corba-2.3-apis-%{version}.jar.*
%endif

%files -n geronimo-corba-3.0-apis
%defattr(-,root,root,-)
%{_javadir}/geronimo-corba-3.0-apis*.jar
%doc geronimo-spec-corba-3.0/LICENSE.txt
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-corba-3.0-apis-%{version}.jar.*
%endif

%files -n geronimo-ejb-2.1-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-ejb-2.1-api*.jar
%doc geronimo-spec-ejb/LICENSE.txt
%ghost %{_javadir}/ejb.jar
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-ejb-2.1-api-%{version}.jar.*
%endif

%files -n geronimo-j2ee-1.4-apis
%defattr(-,root,root,-)
%{_javadir}/geronimo-j2ee-1.4-apis*.jar
%doc geronimo-spec-j2ee/LICENSE.txt
#%if %{gcj_support}
#%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
#%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-j2ee-1.4-apis-%{version}.jar.*
#%endif

%files -n geronimo-j2ee-connector-1.5-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-j2ee-connector-1.5-api*.jar
%doc geronimo-spec-j2ee-connector/LICENSE.txt
%ghost %{_javadir}/j2ee-connector.jar
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-j2ee-connector-1.5-api-%{version}.jar.*
%endif

%files -n geronimo-j2ee-deployment-1.1-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-j2ee-deployment-1.1-api*.jar
%doc geronimo-spec-j2ee-deployment/LICENSE.txt
%ghost %{_javadir}/j2ee-deployment.jar
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-j2ee-deployment-1.1-api-%{version}.jar.*
%endif

%files -n geronimo-jacc-1.0-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-jacc-1.0-api*.jar
%doc geronimo-spec-j2ee-jacc/LICENSE.txt
%ghost %{_javadir}/jacc.jar
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-jacc-1.0-api-%{version}.jar.*
%endif

%files -n geronimo-j2ee-management-1.0-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-j2ee-management-1.0-api*.jar
%doc geronimo-spec-j2ee-management/LICENSE.txt
%ghost %{_javadir}/j2ee-management.jar
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-j2ee-management-1.0-api-%{version}.jar.*
%endif

%files -n geronimo-javamail-1.3.1-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-javamail-1.3.1-api*.jar
%doc geronimo-spec-javamail/LICENSE.txt
# Do not provide it as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
#%ghost %{_javadir}/javamail.jar
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-javamail-1.3.1-api-%{version}.jar.*
%endif

%files -n geronimo-jaxr-1.0-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-jaxr-1.0-api*.jar
%doc geronimo-spec-jaxr/LICENSE.txt
%ghost %{_javadir}/jaxr.jar
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-jaxr-1.0-api-%{version}.jar.*
%endif

%files -n geronimo-jaxrpc-1.1-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-jaxrpc-1.1-api*.jar
%doc geronimo-spec-jaxrpc/LICENSE.txt
%ghost %{_javadir}/jaxrpc.jar
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-jaxrpc-1.1-api-%{version}.jar.*
%endif

%files -n geronimo-jms-1.1-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-jms-1.1-api*.jar
%doc geronimo-spec-jms/LICENSE.txt
%ghost %{_javadir}/jms.jar
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-jms-1.1-api-%{version}.jar.*
%endif

%files -n geronimo-jsp-2.0-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-jsp-2.0-api*.jar
%doc geronimo-spec-jsp/LICENSE.txt
%ghost %{_javadir}/jsp.jar
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-jsp-2.0-api-%{version}.jar.*
%endif

%files -n geronimo-jta-1.0.1B-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-jta-1.0.1B-api*.jar
%doc geronimo-spec-jta/LICENSE.txt
%ghost %{_javadir}/jta.jar
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-jta-1.0.1B-api-%{version}.jar.*
%endif

%files -n geronimo-qname-1.1-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-qname-1.1-api*.jar
%doc geronimo-spec-qname/LICENSE.txt
%ghost %{_javadir}/qname.jar
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-qname-1.1-api-%{version}.jar.*
%endif

%files -n geronimo-saaj-1.1-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-saaj-1.1-api*.jar
%doc geronimo-spec-saaj/LICENSE.txt
%ghost %{_javadir}/saaj.jar
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-saaj-1.1-api-%{version}.jar.*
%endif

%files -n geronimo-servlet-2.4-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-servlet-2.4-api*.jar
%doc geronimo-spec-servlet/LICENSE.txt
%ghost %{_javadir}/servlet.jar
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/geronimo-servlet-2.4-api-%{version}.jar.*
%endif


