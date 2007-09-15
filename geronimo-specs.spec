# Copyright (c) 2000-2005, JPackage Project
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

%define bname           geronimo
%define section         free
%define gcj_support     1
                                                                                
Summary:        Geronimo J2EE server J2EE specifications
URL:            http://geronimo.apache.org
Source0:        %{name}-%{version}-src.tar.bz2
# svn export https://svn.apache.org/repos/asf/geronimo/specs/tags/1_0/

Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        %{name}-%{version}-jpp-depmap.xml
Source5:        %{name}-pom2project.xsl

Source6:        %{name}-%{version}-project.xml
Source7:        %{name}-%{version}-etc-project.xml
Source8:        %{name}-%{version}-etc-project.properties
Source9:        %{name}-%{version}-corba-maven.xml
Source10:       %{name}-%{version}-corba-project.xml
Source11:       %{name}-%{version}-j2ee-maven.xml
Source12:       %{name}-%{version}-j2ee-project.xml

# Fix problem with EJBMethodPermission returning the wrong signature
Patch0:         geronimo-specs-1.0-jacc.patch

Name:           geronimo-specs
Version:        1.0
Release:        %mkrel 3.8.1
Epoch:          0
License:        Apache License
Group:          Development/Java
#Vendor:        JPackage Project
#Distribution:  JPackage
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
BuildRequires:  jpackage-utils >= 0:1.5
%if 0
BuildRequires:  maven >= 0:1.1
BuildRequires:  saxon, saxon-scripts
BuildRequires:  maven-plugins-base
BuildRequires:  maven-plugin-license
BuildRequires:  maven-plugin-multiproject
BuildRequires:  maven-plugin-test
BuildRequires:  maven-plugin-xdoc
BuildRequires:  isorelax
%endif
BuildRequires:  junit >= 0:3.8.1
%if 0
BuildRequires:  jakarta-commons-jelly-tags-velocity
BuildRequires:  jakarta-commons-jelly-tags-xml
BuildRequires:  forehead
BuildRequires:  saxon-scripts
%endif
%if 0
BuildRequires:  mockobjects >= 0:0.09
BuildRequires:  mockobjects-jdk1.4 >= 0:0.09
BuildRequires:  mockobjects-jdk1.4-j2ee1.3 >= 0:0.09
%endif
BuildRequires:  mx4j >= 0:2.0.1
BuildRequires:  velocity 
%if 0
BuildRequires:  ws-scout 
BuildRequires:  xmlbeans 
%endif
BuildRequires:  xml-commons-resolver12

Requires:       mx4j >= 0:2.0.1
%if 0
Requires:       xmlbeans 
%endif
Requires:       xml-commons-resolver12

# The main package has links to all specs, so it requires all subpackages
# except j2ee-schema (not linked) and javadocs
Requires:       geronimo-jaf-1.0.2-api = %{version}-%{release}
%if 0
Requires:       geronimo-corba-2.3-apis = %{version}-%{release}
%endif
Requires:       geronimo-ejb-2.1-api = %{version}-%{release}
%if 0
Requires:       geronimo-j2ee-1.4-apis = %{version}-%{release}
%endif
Requires:       geronimo-j2ee-connector-1.5-api = %{version}-%{release}
Requires:       geronimo-j2ee-deployment-1.1-api = %{version}-%{release}
Requires:       geronimo-jacc-1.0-api = %{version}-%{release}
Requires:       geronimo-j2ee-management-1.0-api = %{version}-%{release}
Requires:       geronimo-javamail-1.3.1-api = %{version}-%{release}
%if 0
Requires:       geronimo-jaxr-1.0-api = %{version}-%{release}
%endif
Requires:       geronimo-jaxrpc-1.1-api = %{version}-%{release}
Requires:       geronimo-jms-1.1-api = %{version}-%{release}
Requires:       geronimo-jsp-2.0-api = %{version}-%{release}
Requires:       geronimo-jta-1.0.1B-api = %{version}-%{release}
Requires:       geronimo-qname-1.1-api = %{version}-%{release}
Requires:       geronimo-saaj-1.1-api = %{version}-%{release}
Requires:       geronimo-servlet-2.4-api = %{version}-%{release}
Obsoletes:      geronimo-specs-compat
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

%package -n geronimo-jaf-1.0.2-api
Summary:        J2EE JAF v1.0.2 API
Group:          Development/Java
Provides:       jaf = 0:1.0.2
Obsoletes:      jaf
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-jaf-1.0.2-api
Java Activation Framework

%if 0
%package -n geronimo-corba-2.3-apis
Summary:        CORBA v2.3 APIs
Group:          Development/Java

%description -n geronimo-corba-2.3-apis
CORBA Spec
%endif

%package -n geronimo-ejb-2.1-api
Summary:        J2EE EJB v2.1 API
Group:          Development/Java
Provides:       ejb = 0:2.1
Obsoletes:      ejb
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-ejb-2.1-api
Enterprise JavaBeans Specification

%if 0
%package -n geronimo-j2ee-1.4-apis
Summary:        J2EE v1.4 APIs
Group:          Development/Java

%description -n geronimo-j2ee-1.4-apis
J2EE Specification (the complete set in one jar)
%endif

%package -n geronimo-j2ee-connector-1.5-api
Summary:        J2EE Connector v1.5 API
Group:          Development/Java
Provides:       j2ee-connector = 0:1.5
Obsoletes:      j2ee-connector
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-j2ee-connector-1.5-api
J2EE Connector Architecture Specification

%package -n geronimo-j2ee-deployment-1.1-api
Summary:        J2EE Deployment v1.1 API
Group:          Development/Java
Provides:       j2ee-deployment = 0:1.1
Obsoletes:      j2ee-deployment
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-j2ee-deployment-1.1-api
J2EE Application Deployment Specification

%package -n geronimo-jacc-1.0-api
Summary:        J2EE JACC v1.0 API
Group:          Development/Java
#Provides:      geronimo-jacc-1.0-api
Provides:       jacc = 0:1.0
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-jacc-1.0-api
Java Authorization Contract for Containers Specification

%package -n geronimo-j2ee-management-1.0-api
Summary:        J2EE Management v1.0 API
Group:          Development/Java
Provides:       j2ee-management = 0:1.0
Obsoletes:      j2ee-management
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-j2ee-management-1.0-api
J2EE Application Management Specification

%package -n geronimo-javamail-1.3.1-api
Summary:        J2EE JavaMail v1.3.1 API
Group:          Development/Java
# Do not provide it as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
# FIXME: figure out what to do with this
#Provides:      javamail = 0:1.3.1

%description -n geronimo-javamail-1.3.1-api
JavaMail API

%if 0
%package -n geronimo-jaxr-1.0-api
Summary:        J2EE JAXR v1.0 API
Group:          Development/Java
Provides:       jaxr = 0:1.0
Provides:       jaxr-api
Obsoletes:      jaxr-api
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-jaxr-1.0-api
Java API for XML Registries (JAXR)
%endif

%package -n geronimo-jaxrpc-1.1-api
Summary:        J2EE JAXRPC v1.1 API
Group:          Development/Java
Provides:       jaxrpc = 0:1.1
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-jaxrpc-1.1-api
Java API for XML-Based RPC (JAXRPC)

%package -n geronimo-jms-1.1-api
Summary:        J2EE JMS v1.1 API
Group:          Development/Java
Provides:       jms = 0:1.1
Obsoletes:      jms
Requires(preun): update-alternatives
Requires(post):  update-alternatives

%description -n geronimo-jms-1.1-api
JMS Specification

%package -n geronimo-jsp-2.0-api
Summary:        J2EE JSP v2.0 API
Group:          Development/Java
Provides:       jsp = 0:2.0
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-jsp-2.0-api
JavaServer Pages Specification

%package -n geronimo-jta-1.0.1B-api
Summary:        J2EE JTA v1.0.1B API
Group:          Development/Java
Provides:       jta = 0:1.0.1B
Obsoletes:      jta
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-jta-1.0.1B-api
Java Transaction API Specification

%package -n geronimo-qname-1.1-api
Summary:        Namespace v1.1 API
Group:          Development/Java
Requires:       wsdl4j >= 0:1.5.2

%description -n geronimo-qname-1.1-api
javax.xml.namespace.QName API

%package -n geronimo-saaj-1.1-api
Summary:        J2EE SAAJ v1.1 API
Group:          Development/Java
Provides:       saaj = 0:1.1
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-saaj-1.1-api
SOAP with Attachments API for Java (SAAJ)

%package -n geronimo-servlet-2.4-api
Summary:        J2EE Servlet v2.4 API
Group:          Development/Java
Provides:       servlet = 0:2.4
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description -n geronimo-servlet-2.4-api
J2EE Servlet v2.4 API


%prep
%setup -q -n %{name}-%{version}
chmod -R go=u-w *
mkdir etc
cp %{bname}-spec-activation/LICENSE.txt etc
cp %{SOURCE6} project.xml
cp %{SOURCE7} etc/project.xml
cp %{SOURCE8} etc/project.properties
cp %{SOURCE9} %{bname}-spec-corba/maven.xml
cp %{SOURCE10} %{bname}-spec-corba/project.xml
cp %{SOURCE11} %{bname}-spec-j2ee/maven.xml
cp %{SOURCE12} %{bname}-spec-j2ee/project.xml

pushd %{bname}-spec-j2ee-jacc
%patch0 -p2 
popd

pushd %{bname}-spec-j2ee-deployment
rm -f src/test/javax/enterprise/deploy/shared/factories/DeploymentFactoryManagerTest.java
popd

%if 0
for sp in activation ejb j2ee-connector j2ee-deployment j2ee-jacc j2ee-management javamail jaxrpc jaxr jms jsp jta qname saaj servlet; do
    pushd %{bname}-spec-${sp}
        saxon pom.xml %{SOURCE5} > project.xml
    popd
done

export DEPCAT=$(pwd)/%{name}-%{version}-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > %{name}-%{version}-depmap.new.xml
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

# Remove spurious package from ejb
rm -fr specs/ejb/src/java/javax/xml

mkdir -p .maven/repository/JPP/jars
pushd .maven/repository/JPP/jars
ln -sf $(build-classpath mockobjects-j2ee1.3) mockobjects-jdk1.4-j2ee1.3.jar
popd
%endif

%build
%if 0
[ -z "$JAVA_HOME" ] && JAVA_HOME=%{_jvmdir}/java
export JAVA_HOME

export MAVEN_HOME_LOCAL=$(pwd)/.maven

maven -Dmaven.repo.remote=file:/usr/share/maven/repository \
      -Dmaven.home.local=${MAVEN_HOME_LOCAL} \
      -Dmaven.javadoc.mode.online=false \
      -Dgoal=jar:install,javadoc:generate \
      multiproject:goal
%endif
export CLASSPATH=$(build-classpath junit mx4j)
cp=
# TODO: jaxr-1.0/ws-scout, j2ee-1.4, corba-2.3
for spec in activation-1.0.2 ejb-2.1 j2ee-connector-1.5 j2ee-deployment-1.1 servlet-2.4 j2ee-jacc-1.0 j2ee-management-1.0 javamail-1.3.1 saaj-1.1 jaxrpc-1.1 jms-1.1 jsp-2.0 jta-1.0.1B qname-1.1;
do
    sp=`echo $spec | sed 's:-[^-]*$::'`
    version=`echo $spec | sed 's:'${sp}-'::'`
    pushd %{bname}-spec-${sp}
        cp=${cp}:$(pwd)/target/geronimo-${sp}_${version}_spec-%{version}.jar
        export CLASSPATH=${CLASSPATH}:${cp}
        %{__mkdir_p} target
        pushd src/java
        %{javac} `find . -type f -name "*.java"` || exit 1
        %{jar} cf ../../target/geronimo-${sp}_${version}_spec-%{version}.jar `find . -type f -name "*.class"`
        %{javadoc} -d ../../target/docs/apidocs `find . -type f -name "*.java"`
        popd
    popd
done


%install
rm -rf $RPM_BUILD_ROOT

# subpackage jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -p -m 0644 geronimo-spec-activation/target/geronimo-activation_1.0.2_spec-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-jaf-1.0.2-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-jaf-1.0.2-api-%{version}.jar geronimo-jaf-1.0.2-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/jaf.jar # for %ghost

%if 0
install -p -m 0644 geronimo-spec-corba/target/geronimo-corba_2.3_spec-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-corba-2.3-apis-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-corba-2.3-apis-%{version}.jar geronimo-corba-2.3-apis.jar
popd
%endif

install -p -m 0644 geronimo-spec-ejb/target/geronimo-ejb_2.1_spec-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-ejb-2.1-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-ejb-2.1-api-%{version}.jar geronimo-ejb-2.1-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/ejb.jar # for %ghost

install -p -m 0644 geronimo-spec-j2ee-connector/target/geronimo-j2ee-connector_1.5_spec-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-j2ee-connector-1.5-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-j2ee-connector-1.5-api-%{version}.jar \
        geronimo-j2ee-connector-1.5-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/j2ee-connector.jar # for %ghost

install -p -m 0644 geronimo-spec-j2ee-deployment/target/geronimo-j2ee-deployment_1.1_spec-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-j2ee-deployment-1.1-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-j2ee-deployment-1.1-api-%{version}.jar \
        geronimo-j2ee-deployment-1.1-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/j2ee-deployment.jar # for %ghost

install -p -m 0644 geronimo-spec-j2ee-jacc/target/geronimo-j2ee-jacc_1.0_spec-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-jacc-1.0-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-jacc-1.0-api-%{version}.jar geronimo-jacc-1.0-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/jacc.jar # for %ghost

install -p -m 0644 geronimo-spec-j2ee-management/target/geronimo-j2ee-management_1.0_spec-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-j2ee-management-1.0-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-j2ee-management-1.0-api-%{version}.jar \
        geronimo-j2ee-management-1.0-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/j2ee-management.jar # for %ghost

install -p -m 0644 geronimo-spec-javamail/target/geronimo-javamail_1.3.1_spec-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-javamail-1.3.1-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-javamail-1.3.1-api-%{version}.jar \
        geronimo-javamail-1.3.1-api.jar
popd
# Do not provide it as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
#touch $RPM_BUILD_ROOT%{_javadir}/javamail.jar # for %ghost

%if 0
install -p -m 0644 geronimo-spec-jaxr/target/geronimo-jaxr_1.0_spec-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-jaxr-1.0-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-jaxr-1.0-api-%{version}.jar geronimo-jaxr-1.0-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/jaxr.jar # for %ghost
%endif

install -p -m 0644 geronimo-spec-jaxrpc/target/geronimo-jaxrpc_1.1_spec-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-jaxrpc-1.1-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-jaxrpc-1.1-api-%{version}.jar geronimo-jaxrpc-1.1-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/jaxrpc.jar # for %ghost

%if 0
install -p -m 0644 geronimo-spec-j2ee/target/geronimo-j2ee_1.4_spec-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-j2ee-1.4-apis-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-j2ee-1.4-apis-%{version}.jar geronimo-j2ee-1.4-apis.jar
popd
%endif

install -p -m 0644 geronimo-spec-jms/target/geronimo-jms_1.1_spec-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-jms-1.1-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-jms-1.1-api-%{version}.jar geronimo-jms-1.1-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/jms.jar # for %ghost

install -p -m 0644 geronimo-spec-jsp/target/geronimo-jsp_2.0_spec-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-jsp-2.0-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-jsp-2.0-api-%{version}.jar geronimo-jsp-2.0-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/jsp.jar # for %ghost

install -p -m 0644 geronimo-spec-jta/target/geronimo-jta_1.0.1B_spec-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-jta-1.0.1B-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-jta-1.0.1B-api-%{version}.jar geronimo-jta-1.0.1B-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/jta.jar # for %ghost

install -p -m 0644 geronimo-spec-qname/target/geronimo-qname_1.1_spec-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-qname-1.1-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-qname-1.1-api-%{version}.jar geronimo-qname-1.1-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/qname.jar # for %ghost

install -p -m 0644 geronimo-spec-saaj/target/geronimo-saaj_1.1_spec-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-saaj-1.1-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-saaj-1.1-api-%{version}.jar geronimo-saaj-1.1-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/saaj.jar # for %ghost

install -p -m 0644 geronimo-spec-servlet/target/geronimo-servlet_2.4_spec-1.0.jar \
      $RPM_BUILD_ROOT%{_javadir}/geronimo-servlet-2.4-api-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf geronimo-servlet-2.4-api-%{version}.jar geronimo-servlet-2.4-api.jar
popd
touch $RPM_BUILD_ROOT%{_javadir}/servlet.jar # for %ghost

# main package jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/geronimo
pushd $RPM_BUILD_ROOT%{_javadir}/geronimo
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

%if 0
  ln -sf ../geronimo-j2ee-1.4-apis-%{version}.jar spec-j2ee-1.4-%{version}.jar
  ln -sf spec-j2ee-1.4-%{version}.jar spec-j2ee-1.4.jar
%endif

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
#              $RPM_BUILD_ROOT%{_javadir}/geronimo/spec-j2ee-schema-1.0-M4.jar
#pushd $RPM_BUILD_ROOT%{_javadir}/geronimo
#  ln -sf spec-j2ee-schema-1.0-M4.jar spec-j2ee-schema-1.0.jar
#popd


# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
for sp in activation ejb j2ee-connector j2ee-deployment j2ee-management javamail jaxrpc jaxr jms jsp jta qname saaj servlet; do
# XXX
    test -d geronimo-spec-${sp}/target/docs/apidocs && install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/${sp} || :
    cp -pr geronimo-spec-${sp}/target/docs/apidocs/* \
         $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/${sp} || :
done
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jacc
cp -pr geronimo-spec-j2ee-jacc/target/docs/apidocs/* \
         $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jacc
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%{__perl} -pi -e 's/\r$//g' `find . -name LICENSE.txt` 

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{gcj_support}
%post
%{update_gcjdb}

%postun
%{clean_gcjdb}
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -sf %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%triggerpostun -n geronimo-jaf-1.0.2-api -- classpathx-jaf <= 0:1.0-2jpp_4rh
# Remove file from old non-free packages
rm -f %{_javadir}/jaf.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/jaf %{_javadir}/jaf.jar

%post -n geronimo-jaf-1.0.2-api
/usr/sbin/update-alternatives --install %{_javadir}/jaf.jar jaf %{_javadir}/geronimo-jaf-1.0.2-api.jar 10002

%preun -n geronimo-jaf-1.0.2-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove jaf %{_javadir}/geronimo-jaf-1.0.2-api.jar
fi

%triggerpostun -n geronimo-ejb-2.1-api -- ejb <= 0:2.1-3jpp_2rh
# Remove file from old non-free packages
rm -f %{_javadir}/ejb.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/ejb %{_javadir}/ejb.jar

%post -n geronimo-ejb-2.1-api
/usr/sbin/update-alternatives --install %{_javadir}/ejb.jar ejb %{_javadir}/geronimo-ejb-2.1-api.jar 20100

%preun -n geronimo-ejb-2.1-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove ejb %{_javadir}/geronimo-ejb-2.1-api.jar
fi

%triggerpostun -n geronimo-j2ee-connector-1.5-api -- j2ee-connector <= 0:1.5-3jpp_2rh
# Remove file from old non-free packages
rm -f %{_javadir}/j2ee-connector.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/j2ee-connector %{_javadir}/j2ee-connector.jar

%post -n geronimo-j2ee-connector-1.5-api
/usr/sbin/update-alternatives --install %{_javadir}/j2ee-connector.jar j2ee-connector %{_javadir}/geronimo-j2ee-connector-1.5-api.jar 10500

%preun -n geronimo-j2ee-connector-1.5-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove j2ee-connector %{_javadir}/geronimo-j2ee-connector-1.5-api.jar
fi

%triggerpostun -n geronimo-j2ee-deployment-1.1-api -- j2ee-deployment <= 0:1.1-1jpp_1rh
# Remove file from old non-free packages
rm -f %{_javadir}/j2ee-deployment.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/j2ee-deployment %{_javadir}/j2ee-deployment.jar

%post -n geronimo-j2ee-deployment-1.1-api
/usr/sbin/update-alternatives --install %{_javadir}/j2ee-deployment.jar j2ee-deployment %{_javadir}/geronimo-j2ee-deployment-1.1-api.jar 10100

%preun -n geronimo-j2ee-deployment-1.1-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove j2ee-deployment %{_javadir}/geronimo-j2ee-deployment-1.1-api.jar
fi

%triggerpostun -n geronimo-jacc-1.0-api -- jacc <= 0:1.0-1jpp
# Remove file from old non-free packages
rm -f %{_javadir}/jacc.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/jacc %{_javadir}/jacc.jar

%post -n geronimo-jacc-1.0-api
/usr/sbin/update-alternatives --install %{_javadir}/jacc.jar jacc %{_javadir}/geronimo-jacc-1.0-api.jar 10000

%preun -n geronimo-jacc-1.0-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove jacc %{_javadir}/geronimo-jacc-1.0-api.jar
fi

%triggerpostun -n geronimo-j2ee-management-1.0-api -- j2ee-management <= 0:1.0-1jpp_1rh
# Remove file from old non-free packages
rm -f %{_javadir}/j2ee-management.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/j2ee-management %{_javadir}/j2ee-management.jar

%post -n geronimo-j2ee-management-1.0-api
/usr/sbin/update-alternatives --install %{_javadir}/j2ee-management.jar j2ee-management %{_javadir}/geronimo-j2ee-management-1.0-api.jar 10000

%preun -n geronimo-j2ee-management-1.0-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove j2ee-management %{_javadir}/geronimo-j2ee-management-1.0-api.jar
fi

# Do not provide it as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
#%post -n geronimo-javamail-1.3.1-api
#/usr/sbin/update-alternatives --install %{_javadir}/javamail.jar javamail %{_javadir}/geronimo-javamail-1.3.1-api.jar 10301
#
#%preun -n geronimo-javamail-1.3.1-api
#if [ "$1" = "0" ]; then
#    /usr/sbin/update-alternatives --remove javamail %{_javadir}/geronimo-javamail-1.3.1-api.jar
#fi

%if 0
%triggerpostun -n geronimo-jaxr-1.0-api -- jaxr-api <= 0:1.0-1jpp
# Remove file from old non-free packages
rm -f %{_javadir}/jaxr.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/jaxr %{_javadir}/jaxr.jar
%endif

%if 0
%post -n geronimo-jaxr-1.0-api
/usr/sbin/update-alternatives --install %{_javadir}/jaxr.jar jaxr %{_javadir}/geronimo-jaxr-1.0-api.jar 10000

%preun -n geronimo-jaxr-1.0-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove jaxr %{_javadir}/geronimo-jaxr-1.0-api.jar
fi
%endif

%post -n geronimo-jaxrpc-1.1-api
/usr/sbin/update-alternatives --install %{_javadir}/jaxrpc.jar jaxrpc %{_javadir}/geronimo-jaxrpc-1.1-api.jar 10100

%preun -n geronimo-jaxrpc-1.1-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove jaxrpc %{_javadir}/geronimo-jaxrpc-1.1-api.jar
fi

%triggerpostun -n geronimo-jms-1.1-api -- jms <= 0:1.1-3jpp_2rh
# Remove file from old non-free packages
rm -f %{_javadir}/jms.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/jms %{_javadir}/jms.jar

%post -n geronimo-jms-1.1-api
/usr/sbin/update-alternatives --install %{_javadir}/jms.jar jms %{_javadir}/geronimo-jms-1.1-api.jar 10100

%preun -n geronimo-jms-1.1-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove jms %{_javadir}/geronimo-jms-1.1-api.jar
fi

%post -n geronimo-jsp-2.0-api
/usr/sbin/update-alternatives --install %{_javadir}/jsp.jar jsp %{_javadir}/geronimo-jsp-2.0-api.jar 20000

%preun -n geronimo-jsp-2.0-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove jsp %{_javadir}/geronimo-jsp-2.0-api.jar
fi

%triggerpostun -n geronimo-jta-1.0.1B-api -- jta <= 0:1.0.1-0.b.3jpp_2rh
# Remove file from old non-free packages
rm -f %{_javadir}/jta.jar
# Recreate the link as update-alternatives could not do it
ln -s %{_sysconfdir}/alternatives/jta %{_javadir}/jta.jar

%post -n geronimo-jta-1.0.1B-api
/usr/sbin/update-alternatives --install %{_javadir}/jta.jar jta %{_javadir}/geronimo-jta-1.0.1B-api.jar 10001

%preun -n geronimo-jta-1.0.1B-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove jta %{_javadir}/geronimo-jta-1.0.1B-api.jar
fi

%post -n geronimo-qname-1.1-api
ln -sf %{_javadir}/geronimo-qname-1.1-api-%{version}.jar %{_javadir}/qname.jar

%postun -n geronimo-qname-1.1-api
if [ "$1" = "0" ]; then
  rm -f %{_javadir}/qname.jar
fi

%post -n geronimo-saaj-1.1-api
/usr/sbin/update-alternatives --install %{_javadir}/saaj.jar saaj %{_javadir}/geronimo-saaj-1.1-api.jar 10100

%preun -n geronimo-saaj-1.1-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove saaj %{_javadir}/geronimo-saaj-1.1-api.jar
fi

%post -n geronimo-servlet-2.4-api
/usr/sbin/update-alternatives --install %{_javadir}/servlet.jar servlet %{_javadir}/geronimo-servlet-2.4-api.jar 20400

%preun -n geronimo-servlet-2.4-api
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove servlet %{_javadir}/geronimo-servlet-2.4-api.jar
fi


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

%files -n geronimo-jaf-1.0.2-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-jaf-1.0.2-api*.jar
%doc geronimo-spec-activation/LICENSE.txt
%ghost %{_javadir}/jaf.jar

%if 0
%files -n geronimo-corba-2.3-apis
%defattr(-,root,root,-)
%{_javadir}/geronimo-corba-2.3-apis*.jar
%doc geronimo-spec-corba/LICENSE.txt
%endif

%files -n geronimo-ejb-2.1-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-ejb-2.1-api*.jar
%doc geronimo-spec-ejb/LICENSE.txt
%ghost %{_javadir}/ejb.jar

%if 0
%files -n geronimo-j2ee-1.4-apis
%defattr(-,root,root,-)
%{_javadir}/geronimo-j2ee-1.4-apis*.jar
%doc geronimo-spec-j2ee/LICENSE.txt
%endif

%files -n geronimo-j2ee-connector-1.5-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-j2ee-connector-1.5-api*.jar
%doc geronimo-spec-j2ee-connector/LICENSE.txt
%ghost %{_javadir}/j2ee-connector.jar

%files -n geronimo-j2ee-deployment-1.1-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-j2ee-deployment-1.1-api*.jar
%doc geronimo-spec-j2ee-deployment/LICENSE.txt
%ghost %{_javadir}/j2ee-deployment.jar

%files -n geronimo-jacc-1.0-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-jacc-1.0-api*.jar
%doc geronimo-spec-j2ee-jacc/LICENSE.txt
%ghost %{_javadir}/jacc.jar

%files -n geronimo-j2ee-management-1.0-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-j2ee-management-1.0-api*.jar
%doc geronimo-spec-j2ee-management/LICENSE.txt
%ghost %{_javadir}/j2ee-management.jar

%files -n geronimo-javamail-1.3.1-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-javamail-1.3.1-api*.jar
%doc geronimo-spec-javamail/LICENSE.txt
# Do not provide it as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
#%ghost %{_javadir}/javamail.jar

%if 0
%files -n geronimo-jaxr-1.0-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-jaxr-1.0-api*.jar
%doc geronimo-spec-jaxr/LICENSE.txt
%ghost %{_javadir}/jaxr.jar
%endif

%files -n geronimo-jaxrpc-1.1-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-jaxrpc-1.1-api*.jar
%doc geronimo-spec-jaxrpc/LICENSE.txt
%ghost %{_javadir}/jaxrpc.jar

%files -n geronimo-jms-1.1-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-jms-1.1-api*.jar
%doc geronimo-spec-jms/LICENSE.txt
%ghost %{_javadir}/jms.jar

%files -n geronimo-jsp-2.0-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-jsp-2.0-api*.jar
%doc geronimo-spec-jsp/LICENSE.txt
%ghost %{_javadir}/jsp.jar

%files -n geronimo-jta-1.0.1B-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-jta-1.0.1B-api*.jar
%doc geronimo-spec-jta/LICENSE.txt
%ghost %{_javadir}/jta.jar

%files -n geronimo-qname-1.1-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-qname-1.1-api*.jar
%doc geronimo-spec-qname/LICENSE.txt
%ghost %{_javadir}/qname.jar

%files -n geronimo-saaj-1.1-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-saaj-1.1-api*.jar
%doc geronimo-spec-saaj/LICENSE.txt
%ghost %{_javadir}/saaj.jar

%files -n geronimo-servlet-2.4-api
%defattr(-,root,root,-)
%{_javadir}/geronimo-servlet-2.4-api*.jar
%doc geronimo-spec-servlet/LICENSE.txt
%ghost %{_javadir}/servlet.jar


