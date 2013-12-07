%define _duplicate_files_terminate_build 0

%define with_tests 0

%define bname       geronimo
%define section     free
%define sver_activation_1_0_2 1.2
%define sver_activation_1_1 1.0
%define sver_annotation_1_0 1.1.0
%define sver_corba_1_0 1.0
%define sver_corba_2_3 1.1
%define sver_corba_3_0 1.1
%define sver_ejb_2_1 1.1
%define sver_ejb_3_0 1.0
%define sver_el_1_0 1.0
%define sver_interceptor_3_0 1.0
%define sver_j2ee_connector_1_5 1.1.1
%define sver_j2ee_deployment_1_1 1.1
%define sver_javaee_deployment_1_1MR3 1.0
%define sver_j2ee_jacc_1_0 1.1
%define sver_jacc_1_1 1.0
%define sver_j2ee_management_1_0 1.1
%define sver_j2ee_management_1_1 1.0
%define sver_javamail_1_3_1 1.3
%define sver_javamail_1_4 1.1
%define sver_jaxr_1_0 1.1
%define sver_jaxrpc_1_1 1.1
%define sver_jms_1_1 1.1
%define sver_jpa_3_0 1.1.0
%define sver_jsp_2_0 1.1
%define sver_jsp_2_1 1.0
%define sver_jta_1_0_1B 1.1.1
%define sver_jta_1_1 1.1.0
%define sver_qname_1_1 1.1
%define sver_saaj_1_1 1.1
%define sver_servlet_2_4 1.1.1
%define sver_servlet_2_5 1.1
%define sver_stax_1_0 1.0
%define sver_ws_metadata_2_0 1.1.1
%define sver_commonj_1_1 1.0

Name:           geronimo-specs
Version:        1.2
Release:        6
Epoch:          0
Summary:        Geronimo J2EE server J2EE specifications
Url:            http://geronimo.apache.org
License:        Apache License
Group:          Development/Java
Source0:        %{name}-%{version}-src.tar.bz2

Source1:        %{name}-jpp-depmap.xml
Source1000:     geronimo-specs.build.xml
Source1001:     undot.py
Patch0:         geronimo-specs-1.2-pom_xml.patch
Patch1:         geronimo-specs-jta-1.0.1B-pom_xml.patch
Patch2:         geronimo-specs-j2ee-connector-1.5-pom_xml.patch
Patch3:         geronimo-specs-servlet-2.4-pom_xml.patch
Patch4:         geronimo-specs-j2ee-1.4-pom_xml.patch
Patch5:         geronimo-specs-corba-2.3-pom_xml.patch
BuildRequires:  jpackage-utils >= 1.7.2
BuildRequires:  java-devel >= 0:1.6.0
BuildRequires:  java-rpmbuild
BuildRequires:  ant
BuildRequires:  junit >= 3.8.1
BuildRequires:  xml-commons-jaxp-1.3-apis
BuildRequires:  xerces-j2
BuildRequires:  fdupes

Requires: geronimo-commonj-1.1-apis = %{version}-%{release}
Requires: geronimo-jaf-1.0.2-api = %{version}-%{release}
Requires: geronimo-jaf-1.1-api = %{version}-%{release}
Requires: geronimo-annotation-1.0-api = %{version}-%{release}
Requires: geronimo-corba-1.0-apis = %{version}-%{release}
Requires: geronimo-corba-2.3-apis = %{version}-%{release}
Requires: geronimo-ejb-2.1-api = %{version}-%{release}
Requires: geronimo-ejb-3.0-api = %{version}-%{release}
Requires: geronimo-el-1.0-api = %{version}-%{release}
Requires: geronimo-interceptor-3.0-api = %{version}-%{release}
Requires: geronimo-j2ee-1.4-apis = %{version}-%{release}
Requires: geronimo-j2ee-connector-1.5-api = %{version}-%{release}
Requires: geronimo-javaee-deployment-1.1-api = %{version}-%{release}
Requires: geronimo-javaee-deployment-1.1-api = %{version}-%{release}
Requires: geronimo-jacc-1.0-api = %{version}-%{release}
Requires: geronimo-jacc-1.1-api = %{version}-%{release}
Requires: geronimo-j2ee-management-1.0-api = %{version}-%{release}
Requires: geronimo-j2ee-management-1.1-api = %{version}-%{release}
Requires: geronimo-javamail-1.3.1-api = %{version}-%{release}
Requires: geronimo-javamail-1.4-api = %{version}-%{release}
Requires: geronimo-jaxr-1.0-api = %{version}-%{release}
Requires: geronimo-jaxrpc-1.1-api = %{version}-%{release}
Requires: geronimo-jms-1.1-api = %{version}-%{release}
Requires: geronimo-jpa-3.0-api = %{version}-%{release}
Requires: geronimo-jsp-2.0-api = %{version}-%{release}
Requires: geronimo-jsp-2.1-api = %{version}-%{release}
Requires: geronimo-jta-1.0.1B-api = %{version}-%{release}
Requires: geronimo-jta-1.1-api = %{version}-%{release}
Requires: geronimo-qname-1.1-api = %{version}-%{release}
Requires: geronimo-saaj-1.1-api = %{version}-%{release}
Requires: geronimo-servlet-2.4-api = %{version}-%{release}
Requires: geronimo-servlet-2.5-api = %{version}-%{release}
Requires: geronimo-stax-1.0-api = %{version}-%{release}
Requires: geronimo-ws-metadata-2.0-api = %{version}-%{release}

BuildArch:      noarch

%description
Geronimo is Apache's ASF-licensed J2EE server project.
These are the J2EE-Specifications
Note: You should use the sub packages for the Specifications
that you actually need.  The ones installed by the main package
are deprecated and will disappear in future releases.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java

%description javadoc
Javadoc for %{name}.

%package -n geronimo-commonj-1.1-apis
Summary:        CommonJ APIs
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    commonj_1_1_apis = %{version}-%{release}
Provides:    commonj_apis = 0:1.1

%description -n geronimo-commonj-1.1-apis
CommonJ Spec

%package -n geronimo-jaf-1.0.2-api
Summary:        J2EE JAF v1.0.2 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    jaf = 0:1.0.2
# TODO: drop asap
Provides:    jaf_1_0_2_api = %{version}-%{release}
Provides:    activation_1_0_2_api = %{version}-%{release}
Provides:    jaf_api = 0:1.0.2
Provides:    activation_api = 0:1.0.2
# Don't obsolete jaf, classpathx-jaf provides it
# Don't even obsolete it versioned, as sun-jaf is at 1.1
#Obsoletes:    jaf
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-jaf-1.0.2-api
Java Activation Framework 1.0.2


%package -n geronimo-jaf-1.1-api
Summary:        J2EE JAF v1.1 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    jaf = 0:1.1
# TODO: drop asap
Provides:    jaf_1_1_api = %{version}-%{release}
Provides:    activation_1_1_api = %{version}-%{release}
Provides:    jaf_api = 0:1.1
Provides:    activation_api = 0:1.1
# Don't obsolete jaf, classpathx-jaf provides it
# Don't even obsolete it versioned, as sun-jaf is at 1.1
#Obsoletes:    jaf
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-jaf-1.1-api
Java Activation Framework 1.1


%package -n geronimo-annotation-1.0-api
Summary:        JEE Common Annotations v1.0
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    annotation_1_0_api = %{version}-%{release}
Provides:    annotation_api = 0:1.0
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-annotation-1.0-api
JEE Common Annotations v1.0


%package -n geronimo-corba-1.0-apis
Summary:        CORBA v1.0 APIs
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    corba_1_0_apis = %{version}-%{release}
Provides:    corba_apis = 0:1.0

%description -n geronimo-corba-1.0-apis
CORBA 1.0 Spec


%package -n geronimo-corba-2.3-apis
Summary:        CORBA v2.3 APIs
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    corba_2_3_apis = %{version}-%{release}
Provides:    corba_apis = 0:2.3

%description -n geronimo-corba-2.3-apis
CORBA 2.3 Spec


%package -n geronimo-ejb-2.1-api
Summary:        J2EE EJB v2.1 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    ejb = 0:2.1
# TODO: drop asap
Provides:    ejb_2_1_api = %{version}-%{release}
Provides:    ejb_api = 0:2.1
# drop the following asap
Provides:    ejb = %{version}-%{release}
#Obsoletes:   ejb
Requires:    jta_1_0_1B_api
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives
Obsoletes:   geronimo-specs-compat <= 0:1.0

%description -n geronimo-ejb-2.1-api
Enterprise JavaBeans Specification 2.1


%package -n geronimo-ejb-3.0-api
Summary:        J2EE EJB v3.0 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    ejb = 0:3.0
# TODO: drop asap
Provides:    ejb_3_0_api = %{version}-%{release}
Provides:    ejb_api = 0:3.0
#Obsoletes:   ejb
Requires:    annotation_1_0_api
Requires:    interceptor_3_0_api
Requires:    jta_1_1_api
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives
Obsoletes:   geronimo-specs-compat <= 0:1.0

%description -n geronimo-ejb-3.0-api
Enterprise JavaBeans Specification 3.0



%package -n geronimo-el-1.0-api
Summary:        Expression Language v1.0 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    el_1_0_api = %{version}-%{release}
Provides:    el_api = 0:1.0
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-el-1.0-api
Expression Language 1.0



%package -n geronimo-interceptor-3.0-api
Summary:        Interceptor v3.0 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    interceptor_3_0_api = %{version}-%{release}
Provides:    interceptor_api = 0:3.0
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-interceptor-3.0-api
Interceptor 3.0



%package -n geronimo-j2ee-1.4-apis
Summary:        J2EE v1.4 APIs
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-j2ee-1.4-apis
J2EE Specification (the complete set in one jar)


%package -n geronimo-j2ee-connector-1.5-api
Summary:        J2EE Connector v1.5 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    j2ee_connector_1_5_api = %{version}-%{release}
Provides:    j2ee_connector_api = 0:1.5
# drop the following asap
Provides:    j2ee-connector = 0:1.5
# Obsoletes:   j2ee-connector
Requires:    jta_1_0_1B_api
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives
Obsoletes:   geronimo-specs-compat <= 0:1.0

%description -n geronimo-j2ee-connector-1.5-api
J2EE Connector Architecture 1.5 Specification


%package -n geronimo-j2ee-deployment-1.1-api
Summary:        J2EE Deployment v1.1 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    j2ee_deployment_1_1_api = %{version}-%{release}
Provides:    j2ee_deployment_api = 0:1.1
# drop the following asap
Provides:    j2ee-deployment = 0:1.1
# Obsoletes:    j2ee-deployment
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives
Obsoletes:   geronimo-specs-compat <= 0:1.0

%description -n geronimo-j2ee-deployment-1.1-api
J2EE Application Deployment Specification

%package -n geronimo-javaee-deployment-1.1-api
Summary:        JEE Deployment v1.1 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    javaee_deployment_1_1_api = %{version}-%{release}
Provides:    javaee_deployment_api = 0:1.1
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-javaee-deployment-1.1-api
JEE Application Deployment Specification

%package -n geronimo-jacc-1.0-api
Summary:        J2EE JACC v1.0 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    jacc = 0:1.0
# TODO: drop asap
Provides:    jacc_1_0_api = %{version}-%{release}
Provides:    jacc_api = 0:1.0
Requires:    servlet_2_4_api
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives
Obsoletes:   geronimo-specs-compat <= 0:1.0

%description -n geronimo-jacc-1.0-api
Java Authorization Contract for Containers v1.0 Specification

%package -n geronimo-jacc-1.1-api
Summary:        J2EE JACC v1.1 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    jacc_1_1_api = %{version}-%{release}
Provides:    jacc_api = 0:1.1
Requires:    servlet_2_5_api
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-jacc-1.1-api
Java Authorization Contract for Containers v1.1 Specification

%package -n geronimo-j2ee-management-1.0-api
Summary:        J2EE Management v1.0 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    j2ee_management_1_0_api = %{version}-%{release}
Provides:    j2ee_management_api = 0:1.0
# drop the following asap
Provides:    j2ee-management = 0:1.0
#Obsoletes:   j2ee-management
Requires:    ejb_2_1_api
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-j2ee-management-1.0-api
J2EE Application Management Specification 1.0

%package -n geronimo-j2ee-management-1.1-api
Summary:        J2EE Management v1.1 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    j2ee_management_1_1_api = %{version}-%{release}
Provides:    j2ee_management_api = 0:1.1
# drop the following asap
Provides:    j2ee-management = 0:1.1
#Obsoletes:   j2ee-management
Requires:    ejb_3_0_api
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-j2ee-management-1.1-api
J2EE Application Management Specification 1.1

%package -n geronimo-javamail-1.3.1-api
Summary:        J2EE JavaMail v1.3.1 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    javamail_1_3_1_api = %{version}-%{release}
Provides:    javamail_api = 0:1.3.1
Requires:    jaf_1_0_2_api
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives
# Do not provide javamail as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
#Provides:    javamail = 0:1.3.1

%description -n geronimo-javamail-1.3.1-api
JavaMail API 1.3.1

%package -n geronimo-javamail-1.4-api
Summary:        J2EE JavaMail v1.4 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    javamail_1_4_api = %{version}-%{release}
Provides:    javamail_api = 0:1.4
Requires:    jaf_1_1_api
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives
# Do not provide javamail as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
#Provides:    javamail = 0:1.4

%description -n geronimo-javamail-1.4-api
JavaMail API 1.4

%package -n geronimo-jaxr-1.0-api
Summary:        J2EE JAXR v1.0 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    jaxr_1_0_api = %{version}-%{release}
Provides:    jaxr_api = 0:1.0
# drop the following asap
Provides:    jaxr = 0:1.0
# Obsoletes:   jaxr-api
Requires:    jaf_1_0_2_api
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-jaxr-1.0-api
Java API for XML Registries (JAXR)


%package -n geronimo-jaxrpc-1.1-api
Summary:        J2EE JAXRPC v1.1 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    jaxrpc = 0:1.1
# TODO: drop asap
Provides:    jaxrpc_1_1_api = %{version}-%{release}
Provides:    jaxrpc_api = 0:1.1
Requires:    qname_1_1_api
Requires:    saaj_1_1_api
Requires:    servlet_2_4_api
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-jaxrpc-1.1-api
Java API for XML-Based RPC (JAXRPC)


%package -n geronimo-jms-1.1-api
Summary:        J2EE JMS v1.1 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    jms_1_1_api = %{version}-%{release}
Provides:    jms_api = 0:1.1
# drop the following asap
Provides:    jms = 0:1.1
# Obsoletes:    jms
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives
Obsoletes:   geronimo-specs-compat <= 0:1.0

%description -n geronimo-jms-1.1-api
JMS Specification


%package -n geronimo-jpa-3.0-api
Summary:        JPA v3.0 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    jpa_3_0_api = %{version}-%{release}
Provides:    jpa_api = 0:3.0
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-jpa-3.0-api
JPA Specification

%package -n geronimo-jsp-2.0-api
Summary:        J2EE JSP v2.0 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    jsp = 0:2.0
# TODO: drop asap
Provides:    jsp_2_0_api = %{version}-%{release}
Provides:    jsp_api = 0:2.0
Requires:    servlet_2_4_api
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-jsp-2.0-api
JavaServer Pages Specification 2.0


%package -n geronimo-jsp-2.1-api
Summary:        JEE JSP v2.1 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    jsp = 0:2.1
# TODO: drop asap
Provides:    jsp_2_1_api = %{version}-%{release}
Provides:    jsp_api = 0:2.1
Requires:    servlet_2_5_api
Requires:    el_1_0_api
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-jsp-2.1-api
JavaServer Pages Specification 2.1


%package -n geronimo-jta-1.0.1B-api
Summary:        J2EE JTA v1.0.1B API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    jta_1_0_1B_api = %{version}-%{release}
Provides:    jta_api = 0:1.0.1B
# drop the following asap
Provides:    jta = 0:1.0.1B
# Don't obsolete jta, as this is provided by java-1.4.2-gcj-compat
#Obsoletes:    jta
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives
Obsoletes:   geronimo-specs-compat <= 0:1.0

%description -n geronimo-jta-1.0.1B-api
Java Transaction API Specification 1.0.1B


%package -n geronimo-jta-1.1-api
Summary:        J2EE JTA v1.1 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    jta_1_1_api = %{version}-%{release}
Provides:    jta_api = 0:1.1
# drop the following asap
Provides:    jta = 0:1.1
# Don't obsolete jta, as this is provided by java-1.4.2-gcj-compat
#Obsoletes:    jta
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives
Obsoletes:   geronimo-specs-compat <= 0:1.0

%description -n geronimo-jta-1.1-api
Java Transaction API Specification 1.1


%package -n geronimo-qname-1.1-api
Summary:        Namespace v1.1 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    qname_1_1_api = %{version}-%{release}
Provides:    qname_api = 0:1.1
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-qname-1.1-api
javax.xml.namespace.QName API


%package -n geronimo-saaj-1.1-api
Summary:        J2EE SAAJ v1.1 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    saaj = 0:1.1
# TODO: drop asap
Provides:    saaj_1_1_api = %{version}-%{release}
Provides:    saaj_api = 0:1.1
Requires:    jaf_1_0_2_api
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-saaj-1.1-api
SOAP with Attachments API for Java (SAAJ)


%package -n geronimo-servlet-2.4-api
Summary:        J2EE Servlet v2.4 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    servlet = 0:2.4
# TODO: drop asap
Provides:    servlet_2_4_api = %{version}-%{release}
Provides:    servlet_api = 0:2.4
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-servlet-2.4-api
J2EE Servlet v2.4 API


%package -n geronimo-servlet-2.5-api
Summary:        JEE Servlet v2.5 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    servlet = 0:2.5
# TODO: drop asap
Provides:    servlet_2_5_api = %{version}-%{release}
Provides:    servlet_api = 0:2.5
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-servlet-2.5-api
JEE Servlet v2.5 API


%package -n geronimo-stax-1.0-api
Summary:        XML Stax v1.0 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    stax_1_0_api = %{version}-%{release}
Provides:    stax_api = 0:1.0
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-stax-1.0-api
XML STax v1.0 API



%package -n geronimo-ws-metadata-2.0-api
Summary:        Webservices Metadata v2.0 API
Group:          Development/Java
Requires:    %{name}-poms = %{version}-%{release}
Provides:    ws_metadata_2_0_api = %{version}-%{release}
Provides:    ws_metadata_api = 0:2.0
Requires(preun):  %{_sbindir}/update-alternatives
Requires(post):  %{_sbindir}/update-alternatives

%description -n geronimo-ws-metadata-2.0-api
Webservices Metadata v2.0 API


%package poms
Summary:        POM files for geronimo-specs
Group:          Development/Java
Requires(post):   jpackage-utils >= 1.7.3
Requires(postun): jpackage-utils >= 1.7.3

%description poms
The Project Object Model files for the geronimo-specs modules.



%prep
%setup -q -n %{name}-%{version}
chmod -R go=u-w *
mkdir etc
cp LICENSE.txt etc
mkdir external_repo
ln -s %{_javadir} external_repo/JPP
%patch0 -b .sav0
%patch1 -p0 -b .sav1
%patch2 -p0 -b .sav2
%patch3 -p0 -b .sav3
%patch4 -p0 -b .sav4
%patch5 -p0 -b .sav5
cp %{SOURCE1000} build.xml

%build

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
    -Didlj=%{java_home}/bin/idlj


%install
# Directory for poms
install -d -m 0755 %{buildroot}%{_datadir}/maven2/poms
# subpackage jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 0644 \
  geronimo-activation_1.0.2_spec-1.2/target/geronimo-activation_1.0.2_spec-1.2.jar \
  %{buildroot}%{_javadir}/geronimo-jaf-1.0.2-api-%{sver_activation_1_0_2}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-jaf-1.0.2-api-%{sver_activation_1_0_2}.jar \
         geronimo-jaf-1.0.2-api.jar
popd
touch %{buildroot}%{_javadir}/jaf.jar
touch %{buildroot}%{_javadir}/jaf_api.jar
touch %{buildroot}%{_javadir}/jaf_1_0_2_api.jar
install -m 0644 geronimo-activation_1.0.2_spec-1.2/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-jaf-1.0.2-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-activation_1.0.2_spec %{sver_activation_1_0_2} JPP geronimo-jaf-1.0.2-api
install -m 0644 \
  geronimo-activation_1.1_spec-1.0/target/geronimo-activation_1.1_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-jaf-1.1-api-%{sver_activation_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-jaf-1.1-api-%{sver_activation_1_1}.jar \
         geronimo-jaf-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/jaf.jar
touch %{buildroot}%{_javadir}/jaf_api.jar
touch %{buildroot}%{_javadir}/jaf_1_1_api.jar
install -m 0644 geronimo-activation_1.1_spec-1.0/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-jaf-1.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-activation_1.1_spec %{sver_activation_1_1} JPP geronimo-jaf-1.1-api
install -m 0644 \
  geronimo-annotation_1.0_spec-1.1.0/target/geronimo-annotation_1.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-annotation-1.0-api-%{sver_annotation_1_0}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-annotation-1.0-api-%{sver_annotation_1_0}.jar \
         geronimo-annotation-1.0-api.jar
popd
touch %{buildroot}%{_javadir}/annotation_api.jar
touch %{buildroot}%{_javadir}/annotation_1_0_api.jar
install -m 0644 geronimo-annotation_1.0_spec-1.1.0/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-annotation-1.0-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-annotation_1.0_spec %{sver_annotation_1_0} JPP geronimo-annotation-1.0-api
install -m 0644 \
  geronimo-spec-corba-2.3/target/geronimo-corba_2.3_spec-null.jar \
  %{buildroot}%{_javadir}/geronimo-corba-2.3-apis-%{sver_corba_2_3}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-corba-2.3-apis-%{sver_corba_2_3}.jar \
         geronimo-corba-2.3-apis.jar
popd
touch %{buildroot}%{_javadir}/corba_apis.jar
touch %{buildroot}%{_javadir}/corba_2_3_apis.jar
install -m 0644 geronimo-spec-corba-2.3/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-corba-2.3-apis.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-corba_2.3_spec %{sver_corba_2_3} JPP geronimo-corba-2.3-apis

install -m 0644 \
  geronimo-spec-corba/target/geronimo-spec-corba-null.jar \
  %{buildroot}%{_javadir}/geronimo-corba-1.0-apis-%{sver_corba_1_0}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-corba-1.0-apis-%{sver_corba_1_0}.jar \
         geronimo-corba-1.0-apis.jar
popd
touch %{buildroot}%{_javadir}/corba_apis.jar
touch %{buildroot}%{_javadir}/corba_1_0_apis.jar
install -m 0644 geronimo-spec-corba/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-corba-1.0-apis.pom
%add_to_maven_depmap geronimo-spec geronimo-spec-corba %{sver_corba_1_0} JPP geronimo-corba-1.0-apis
install -m 0644 \
  geronimo-ejb_2.1_spec-1.1/target/geronimo-ejb_2.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-ejb-2.1-api-%{sver_ejb_2_1}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-ejb-2.1-api-%{sver_ejb_2_1}.jar \
         geronimo-ejb-2.1-api.jar
popd
touch %{buildroot}%{_javadir}/ejb.jar
touch %{buildroot}%{_javadir}/ejb_api.jar
touch %{buildroot}%{_javadir}/ejb_2_1_api.jar
install -m 0644 geronimo-ejb_2.1_spec-1.1/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-ejb-2.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-ejb_2.1_spec %{sver_ejb_2_1} JPP geronimo-ejb-2.1-api
install -m 0644 \
  geronimo-ejb_3.0_spec-1.0/target/geronimo-ejb_3.0_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-ejb-3.0-api-%{sver_ejb_3_0}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-ejb-3.0-api-%{sver_ejb_3_0}.jar \
         geronimo-ejb-3.0-api.jar
popd
touch %{buildroot}%{_javadir}/ejb.jar
touch %{buildroot}%{_javadir}/ejb_api.jar
touch %{buildroot}%{_javadir}/ejb_3_0_api.jar
install -m 0644 geronimo-ejb_3.0_spec-1.0/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-ejb-3.0-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-ejb_3.0_spec %{sver_ejb_3_0} JPP geronimo-ejb-3.0-api
install -m 0644 \
  geronimo-el_1.0_spec-1.0/target/geronimo-el_1.0_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-el-1.0-api-%{sver_el_1_0}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-el-1.0-api-%{sver_el_1_0}.jar \
         geronimo-el-1.0-api.jar
popd
touch %{buildroot}%{_javadir}/el_api.jar
touch %{buildroot}%{_javadir}/el_1_0_api.jar
install -m 0644 geronimo-el_1.0_spec-1.0/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-el-1.0-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-el_1.0_spec %{sver_el_1_0} JPP geronimo-el-1.0-api
install -m 0644 \
  geronimo-interceptor_3.0_spec-1.0/target/geronimo-interceptor_3.0_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-interceptor-3.0-api-%{sver_interceptor_3_0}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-interceptor-3.0-api-%{sver_interceptor_3_0}.jar \
         geronimo-interceptor-3.0-api.jar
popd
touch %{buildroot}%{_javadir}/interceptor_api.jar
touch %{buildroot}%{_javadir}/interceptor_3_0_api.jar
install -m 0644 geronimo-interceptor_3.0_spec-1.0/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-interceptor-3.0-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-interceptor_3.0_spec %{sver_interceptor_3_0} JPP geronimo-interceptor-3.0-api
install -m 0644 \
  geronimo-j2ee-connector_1.5_spec-1.1.1/target/geronimo-j2ee-connector_1.5_spec-1.1.1.jar \
  %{buildroot}%{_javadir}/geronimo-j2ee-connector-1.5-api-%{sver_j2ee_connector_1_5}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-j2ee-connector-1.5-api-%{sver_j2ee_connector_1_5}.jar \
         geronimo-j2ee-connector-1.5-api.jar
popd
touch %{buildroot}%{_javadir}/j2ee-connector.jar
touch %{buildroot}%{_javadir}/j2ee_connector_api.jar
touch %{buildroot}%{_javadir}/j2ee_connector_1_5_api.jar
install -m 0644 geronimo-j2ee-connector_1.5_spec-1.1.1/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-j2ee-connector-1.5-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-j2ee-connector_1.5_spec %{sver_j2ee_connector_1_5} JPP geronimo-j2ee-connector-1.5-api
install -m 0644 \
  geronimo-j2ee-deployment_1.1_spec-1.1/target/geronimo-j2ee-deployment_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-j2ee-deployment-1.1-api-%{sver_j2ee_deployment_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-j2ee-deployment-1.1-api-%{sver_j2ee_deployment_1_1}.jar \
         geronimo-j2ee-deployment-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/j2ee-deployment.jar
touch %{buildroot}%{_javadir}/j2ee_deployment_api.jar
touch %{buildroot}%{_javadir}/j2ee_deployment_1_1_api.jar
install -m 0644 geronimo-j2ee-deployment_1.1_spec-1.1/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-j2ee-deployment-1.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-j2ee-deployment_1.1_spec %{sver_j2ee_deployment_1_1} JPP geronimo-j2ee-deployment-1.1-api
install -m 0644 \
  geronimo-javaee-deployment_1.1MR3_spec-1.0/target/geronimo-javaee-deployment_1.1MR3_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-javaee-deployment-1.1-api-%{sver_javaee_deployment_1_1MR3}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-javaee-deployment-1.1-api-%{sver_javaee_deployment_1_1MR3}.jar \
         geronimo-javaee-deployment-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/javaee_deployment_1_1MR3_api.jar
touch %{buildroot}%{_javadir}/javaee_deployment_api.jar
install -m 0644 geronimo-javaee-deployment_1.1MR3_spec-1.0/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-javaee-deployment-1.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-javaee-deployment_1.1_spec %{sver_javaee_deployment_1_1MR3} JPP geronimo-javaee-deployment-1.1-api
install -m 0644 \
  geronimo-j2ee-jacc_1.0_spec-1.1/target/geronimo-j2ee-jacc_1.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jacc-1.0-api-%{sver_j2ee_jacc_1_0}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-jacc-1.0-api-%{sver_j2ee_jacc_1_0}.jar \
         geronimo-jacc-1.0-api.jar
popd
touch %{buildroot}%{_javadir}/jacc.jar
touch %{buildroot}%{_javadir}/jacc_api.jar
touch %{buildroot}%{_javadir}/jacc_1_0_api.jar
install -m 0644 geronimo-j2ee-jacc_1.0_spec-1.1/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-jacc-1.0-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-j2ee-jacc_1.0_spec %{sver_j2ee_jacc_1_0} JPP geronimo-jacc-1.0-api
install -m 0644 \
  geronimo-jacc_1.1_spec-1.0/target/geronimo-jacc_1.1_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-jacc-1.1-api-%{sver_jacc_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-jacc-1.1-api-%{sver_jacc_1_1}.jar \
         geronimo-jacc-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/jacc_api.jar
touch %{buildroot}%{_javadir}/jacc_1_1_api.jar
install -m 0644 geronimo-jacc_1.1_spec-1.0/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-jacc-1.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-j2ee-jacc_1.1_spec %{sver_jacc_1_1} JPP geronimo-jacc-1.1-api
install -m 0644 \
  geronimo-j2ee-management_1.0_spec-1.1/target/geronimo-j2ee-management_1.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-j2ee-management-1.0-api-%{sver_j2ee_management_1_0}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-j2ee-management-1.0-api-%{sver_j2ee_management_1_0}.jar \
         geronimo-j2ee-management-1.0-api.jar
popd
touch %{buildroot}%{_javadir}/j2ee-management.jar
touch %{buildroot}%{_javadir}/j2ee_management_api.jar
touch %{buildroot}%{_javadir}/j2ee_management_1_0_api.jar
install -m 0644 geronimo-j2ee-management_1.0_spec-1.1/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-j2ee-management-1.0-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-j2ee-management_1.0_spec %{sver_j2ee_management_1_0} JPP geronimo-j2ee-management-1.0-api
install -m 0644 \
  geronimo-j2ee-management_1.1_spec-1.0/target/geronimo-j2ee-management_1.1_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-j2ee-management-1.1-api-%{sver_j2ee_management_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-j2ee-management-1.1-api-%{sver_j2ee_management_1_1}.jar \
         geronimo-j2ee-management-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/j2ee-management.jar
touch %{buildroot}%{_javadir}/j2ee_management_api.jar
touch %{buildroot}%{_javadir}/j2ee_management_1_1_api.jar
install -m 0644 geronimo-j2ee-management_1.1_spec-1.0/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-j2ee-management-1.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-j2ee-management_1.1_spec %{sver_j2ee_management_1_1} JPP geronimo-j2ee-management-1.1-api
install -m 0644 \
  geronimo-javamail_1.3.1_spec-1.3/target/geronimo-javamail_1.3.1_spec-1.3.jar \
  %{buildroot}%{_javadir}/geronimo-javamail-1.3.1-api-%{sver_javamail_1_3_1}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-javamail-1.3.1-api-%{sver_javamail_1_3_1}.jar \
         geronimo-javamail-1.3.1-api.jar
popd
touch %{buildroot}%{_javadir}/javamail_api.jar
touch %{buildroot}%{_javadir}/javamail_1_3_1_api.jar
install -m 0644 geronimo-javamail_1.3.1_spec-1.3/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-javamail-1.3.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-javamail_1.3.1_spec %{sver_javamail_1_3_1} JPP geronimo-javamail-1.3.1-api
install -m 0644 \
  geronimo-javamail_1.4_spec-1.1/target/geronimo-javamail_1.4_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-javamail-1.4-api-%{sver_javamail_1_4}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-javamail-1.4-api-%{sver_javamail_1_4}.jar \
         geronimo-javamail-1.4-api.jar
popd
touch %{buildroot}%{_javadir}/javamail_api.jar
touch %{buildroot}%{_javadir}/javamail_1_4_api.jar
install -m 0644 geronimo-javamail_1.4_spec-1.1/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-javamail-1.4-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-javamail_1.4_spec %{sver_javamail_1_4} JPP geronimo-javamail-1.4-api
install -m 0644 \
  geronimo-jaxr_1.0_spec-1.1/target/geronimo-jaxr_1.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jaxr-1.0-api-%{sver_jaxr_1_0}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-jaxr-1.0-api-%{sver_jaxr_1_0}.jar \
         geronimo-jaxr-1.0-api.jar
popd
touch %{buildroot}%{_javadir}/jaxr.jar
touch %{buildroot}%{_javadir}/jaxr_api.jar
touch %{buildroot}%{_javadir}/jaxr_1_0_api.jar
install -m 0644 geronimo-jaxr_1.0_spec-1.1/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-jaxr-1.0-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-jaxr_1.0_spec %{sver_jaxr_1_0} JPP geronimo-jaxr-1.0-api
install -m 0644 \
  geronimo-jaxrpc_1.1_spec-1.1/target/geronimo-jaxrpc_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jaxrpc-1.1-api-%{sver_jaxrpc_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-jaxrpc-1.1-api-%{sver_jaxrpc_1_1}.jar \
         geronimo-jaxrpc-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/jaxrpc.jar
touch %{buildroot}%{_javadir}/jaxrpc_api.jar
touch %{buildroot}%{_javadir}/jaxrpc_1_1_api.jar
install -m 0644 geronimo-jaxrpc_1.1_spec-1.1/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-jaxrpc-1.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-jaxrpc_1.1_spec %{sver_jaxrpc_1_1} JPP geronimo-jaxrpc-1.1-api
install -m 0644 \
  geronimo-spec-j2ee/target/geronimo-j2ee_1.4_spec-1.2-jar-with-dependencies.jar \
  %{buildroot}%{_javadir}/geronimo-j2ee-1.4-apis-%{version}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-j2ee-1.4-apis-%{version}.jar \
         geronimo-j2ee-1.4-apis.jar
popd
install -m 0644 geronimo-spec-j2ee/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-j2ee-1.4-apis.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-j2ee_1.4_spec %{version} JPP geronimo-j2ee-1.4-apis
install -m 0644 \
  geronimo-jms_1.1_spec-1.1/target/geronimo-jms_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jms-1.1-api-%{sver_jms_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-jms-1.1-api-%{sver_jms_1_1}.jar \
         geronimo-jms-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/jms.jar
touch %{buildroot}%{_javadir}/jms_api.jar
touch %{buildroot}%{_javadir}/jms_1_1_api.jar
install -m 0644 geronimo-jms_1.1_spec-1.1/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-jms-1.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-jms_1.1_spec %{sver_jms_1_1} JPP geronimo-jms-1.1-api
install -m 0644 \
  geronimo-jpa_3.0_spec-1.1.0/target/geronimo-jpa_3.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jpa-3.0-api-%{sver_jpa_3_0}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-jpa-3.0-api-%{sver_jpa_3_0}.jar \
         geronimo-jpa-3.0-api.jar
popd
touch %{buildroot}%{_javadir}/jpa_api.jar
touch %{buildroot}%{_javadir}/jpa_3_0_api.jar
install -m 0644 geronimo-jpa_3.0_spec-1.1.0/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-jpa-3.0-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-jpa_3.0_spec %{sver_jpa_3_0} JPP geronimo-jpa-3.0-api
install -m 0644 \
  geronimo-jsp_2.0_spec-1.1/target/geronimo-jsp_2.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jsp-2.0-api-%{sver_jsp_2_0}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-jsp-2.0-api-%{sver_jsp_2_0}.jar \
         geronimo-jsp-2.0-api.jar
popd
touch %{buildroot}%{_javadir}/jsp.jar
touch %{buildroot}%{_javadir}/jsp_api.jar
touch %{buildroot}%{_javadir}/jsp_2_0_api.jar
install -m 0644 geronimo-jsp_2.0_spec-1.1/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-jsp-2.0-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-jsp_2.0_spec %{sver_jsp_2_0} JPP geronimo-jsp-2.0-api
install -m 0644 \
  geronimo-jsp_2.1_spec-1.0/target/geronimo-jsp_2.1_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-jsp-2.1-api-%{sver_jsp_2_1}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-jsp-2.1-api-%{sver_jsp_2_1}.jar \
         geronimo-jsp-2.1-api.jar
popd
touch %{buildroot}%{_javadir}/jsp.jar
touch %{buildroot}%{_javadir}/jsp_api.jar
touch %{buildroot}%{_javadir}/jsp_2_1_api.jar
install -m 0644 geronimo-jsp_2.1_spec-1.0/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-jsp-2.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-jsp_2.1_spec %{sver_jsp_2_1} JPP geronimo-jsp-2.1-api
install -m 0644 \
  geronimo-jta_1.0.1B_spec-1.1.1/target/geronimo-jta_1.0.1B_spec-1.1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jta-1.0.1B-api-%{sver_jta_1_0_1B}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-jta-1.0.1B-api-%{sver_jta_1_0_1B}.jar \
         geronimo-jta-1.0.1B-api.jar
popd
touch %{buildroot}%{_javadir}/jta.jar
touch %{buildroot}%{_javadir}/jta_api.jar
touch %{buildroot}%{_javadir}/jta_1_0_1B_api.jar
install -m 0644 geronimo-jta_1.0.1B_spec-1.1.1/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-jta-1.0.1B-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-jta_1.0.1B_spec %{sver_jta_1_0_1B} JPP geronimo-jta-1.0.1B-api
install -m 0644 \
  geronimo-jta_1.1_spec-1.1.0/target/geronimo-jta_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jta-1.1-api-%{sver_jta_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-jta-1.1-api-%{sver_jta_1_1}.jar \
         geronimo-jta-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/jta.jar
touch %{buildroot}%{_javadir}/jta_api.jar
touch %{buildroot}%{_javadir}/jta_1_1_api.jar
install -m 0644 geronimo-jta_1.1_spec-1.1.0/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-jta-1.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-jta_1.1_spec %{sver_jta_1_1} JPP geronimo-jta-1.1-api
install -m 0644 \
  geronimo-qname_1.1_spec-1.1/target/geronimo-qname_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-qname-1.1-api-%{sver_qname_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-qname-1.1-api-%{sver_qname_1_1}.jar \
         geronimo-qname-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/qname_api.jar
touch %{buildroot}%{_javadir}/qname_1_1_api.jar
install -m 0644 geronimo-qname_1.1_spec-1.1/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-qname-1.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-qname_1.1_spec %{sver_qname_1_1} JPP geronimo-qname-1.1-api
install -m 0644 \
  geronimo-saaj_1.1_spec-1.1/target/geronimo-saaj_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-saaj-1.1-api-%{sver_saaj_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-saaj-1.1-api-%{sver_saaj_1_1}.jar \
         geronimo-saaj-1.1-api.jar
popd
touch %{buildroot}%{_javadir}/saaj.jar
touch %{buildroot}%{_javadir}/saaj_api.jar
touch %{buildroot}%{_javadir}/saaj_1_1_api.jar
install -m 0644 geronimo-saaj_1.1_spec-1.1/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-saaj-1.1-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-saaj_1.1_spec %{sver_saaj_1_1} JPP geronimo-saaj-1.1-api
install -m 0644 \
  geronimo-servlet_2.4_spec-1.1.1/target/geronimo-servlet_2.4_spec-1.1.1.jar \
  %{buildroot}%{_javadir}/geronimo-servlet-2.4-api-%{sver_servlet_2_4}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-servlet-2.4-api-%{sver_servlet_2_4}.jar \
         geronimo-servlet-2.4-api.jar
popd
touch %{buildroot}%{_javadir}/servlet.jar
touch %{buildroot}%{_javadir}/servlet_api.jar
touch %{buildroot}%{_javadir}/servlet_2_4_api.jar
install -m 0644 geronimo-servlet_2.4_spec-1.1.1/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-servlet-2.4-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-servlet_2.4_spec %{sver_servlet_2_4} JPP geronimo-servlet-2.4-api
install -m 0644 \
  geronimo-servlet_2.5_spec-1.1/target/geronimo-servlet_2.5_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-servlet-2.5-api-%{sver_servlet_2_5}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-servlet-2.5-api-%{sver_servlet_2_5}.jar \
         geronimo-servlet-2.5-api.jar
popd
touch %{buildroot}%{_javadir}/servlet.jar
touch %{buildroot}%{_javadir}/servlet_api.jar
touch %{buildroot}%{_javadir}/servlet_2_5_api.jar
install -m 0644 geronimo-servlet_2.5_spec-1.1/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-servlet-2.5-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-servlet_2.5_spec %{sver_servlet_2_5}.0.1 JPP geronimo-servlet-2.5-api
install -m 0644 \
  geronimo-stax-api_1.0_spec-1.0/target/geronimo-stax-api_1.0_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-stax-1.0-api-%{sver_stax_1_0}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-stax-1.0-api-%{sver_stax_1_0}.jar \
         geronimo-stax-1.0-api.jar
popd
touch %{buildroot}%{_javadir}/stax_api.jar
touch %{buildroot}%{_javadir}/stax_1_0_api.jar
install -m 0644 geronimo-stax-api_1.0_spec-1.0/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-stax-1.0-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-stax_1.0_spec %{sver_stax_1_0} JPP geronimo-stax-1.0-api
install -m 0644 \
  geronimo-ws-metadata_2.0_spec-1.1.1/target/geronimo-ws-metadata_2.0_spec-1.1.1.jar \
  %{buildroot}%{_javadir}/geronimo-ws-metadata-2.0-api-%{sver_ws_metadata_2_0}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-ws-metadata-2.0-api-%{sver_ws_metadata_2_0}.jar \
         geronimo-ws-metadata-2.0-api.jar
popd
touch %{buildroot}%{_javadir}/ws_metadata_api.jar
touch %{buildroot}%{_javadir}/ws_metadata_2_0_api.jar
install -m 0644 geronimo-ws-metadata_2.0_spec-1.1.1/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-ws-metadata-2.0-api.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-ws-metadata_2.0_spec %{sver_ws_metadata_2_0} JPP geronimo-ws-metadata-2.0-api
install -m 0644 \
  geronimo-spec-commonj/target/geronimo-commonj_1.1_spec-null.jar \
  %{buildroot}%{_javadir}/geronimo-commonj-1.1-apis-%{sver_commonj_1_1}.jar
pushd %{buildroot}%{_javadir}
  ln -sf geronimo-commonj-1.1-apis-%{sver_commonj_1_1}.jar \
         geronimo-commonj-1.1-apis.jar
popd
touch %{buildroot}%{_javadir}/commonj_apis.jar
touch %{buildroot}%{_javadir}/commonj_1_1_apis.jar
install -m 0644 geronimo-spec-commonj/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-commonj-1.1-apis.pom
%add_to_maven_depmap org.apache.geronimo.specs geronimo-commonj_1.1_spec %{sver_commonj_1_1} JPP geronimo-commonj-1.1-apis
# Add the parent geronimo-specs pom
cp pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-geronimo-specs.pom
%add_to_maven_depmap org.apache.geronimo.specs specs 1.1 JPP geronimo-specs
# main package jars
install -d -m 0755 %{buildroot}%{_javadir}/geronimo
pushd %{buildroot}%{_javadir}/geronimo
  ln -sf ../geronimo-commonj-1.1-apis-%{version}.jar spec-commonj-1.1-%{version}.jar
  ln -sf spec-commonj-1.1-%{version}.jar spec-commonj-1.1.jar
  ln -sf ../geronimo-jaf-1.0.2-api-%{version}.jar spec-jaf-1.0.2-%{version}.jar
  ln -sf spec-jaf-1.0.2-%{version}.jar spec-jaf-1.0.2.jar
  ln -sf ../geronimo-jaf-1.1-api-%{version}.jar spec-jaf-1.1-%{version}.jar
  ln -sf spec-jaf-1.1-%{version}.jar spec-jaf-1.1.jar
  ln -sf ../geronimo-annotation-1.0-api-%{version}.jar spec-annotation-1.0-%{version}.jar
  ln -sf spec-annotation-1.0-%{version}.jar spec-annotation-1.0.jar
  ln -sf ../geronimo-ejb-2.1-api-%{version}.jar spec-ejb-2.1-%{version}.jar
  ln -sf spec-ejb-2.1-%{version}.jar spec-ejb-2.1.jar
  ln -sf ../geronimo-ejb-3.0-api-%{version}.jar spec-ejb-3.0-%{version}.jar
  ln -sf spec-ejb-3.0-%{version}.jar spec-ejb-3.0.jar
  ln -sf ../geronimo-el-1.0-api-%{version}.jar spec-el-1.0-%{version}.jar
  ln -sf spec-el-1.0-%{version}.jar spec-el-1.0.jar
  ln -sf ../geronimo-interceptor-3.0-api-%{version}.jar spec-interceptor-3.0-%{version}.jar
  ln -sf spec-interceptor-3.0-%{version}.jar spec-interceptor-3.0.jar
  ln -sf ../geronimo-j2ee-connector-1.5-api-%{version}.jar \
    spec-j2ee-connector-1.5-%{version}.jar
  ln -sf spec-j2ee-connector-1.5-%{version}.jar spec-j2ee-connector-1.5.jar
  ln -sf ../geronimo-j2ee-deployment-1.1-api-%{version}.jar \
    spec-j2ee-deployment-1.1-%{version}.jar
  ln -sf spec-j2ee-deployment-1.1-%{version}.jar spec-j2ee-deployment-1.1.jar
  ln -sf ../geronimo-javaee-deployment-1.1-api-%{version}.jar \
    spec-javaee-deployment-1.1-%{version}.jar
  ln -sf spec-javaee-deployment-1.1-%{version}.jar spec-javaee-deployment-1.1.jar
  ln -sf ../geronimo-jacc-1.0-api-%{version}.jar spec-jacc-1.0-%{version}.jar
  ln -sf spec-jacc-1.0-%{version}.jar spec-jacc-1.0.jar
  ln -sf ../geronimo-jacc-1.1-api-%{version}.jar spec-jacc-1.1-%{version}.jar
  ln -sf spec-jacc-1.1-%{version}.jar spec-jacc-1.1.jar
  ln -sf ../geronimo-j2ee-management-1.0-api-%{version}.jar \
    spec-j2ee-management-1.0-%{version}.jar
  ln -sf spec-j2ee-management-1.0-%{version}.jar spec-j2ee-management-1.0.jar
  ln -sf ../geronimo-j2ee-management-1.1-api-%{version}.jar \
    spec-j2ee-management-1.1-%{version}.jar
  ln -sf spec-j2ee-management-1.1-%{version}.jar spec-j2ee-management-1.1.jar
  ln -sf ../geronimo-j2ee-1.4-apis-%{version}.jar spec-j2ee-1.4-%{version}.jar
  ln -sf spec-j2ee-1.4-%{version}.jar spec-j2ee-1.4.jar
  ln -sf ../geronimo-jms-1.1-api-%{version}.jar spec-jms-1.1-%{version}.jar
  ln -sf spec-jms-1.1-%{version}.jar spec-jms-1.1.jar
  ln -sf ../geronimo-jpa-3.0-api-%{version}.jar spec-jpa-3.0-%{version}.jar
  ln -sf spec-jpa-3.0-%{version}.jar spec-jpa-3.0.jar
  ln -sf ../geronimo-jsp-2.0-api-%{version}.jar spec-jsp-2.0-%{version}.jar
  ln -sf spec-jsp-2.0-%{version}.jar spec-jsp-2.0.jar
  ln -sf ../geronimo-jsp-2.1-api-%{version}.jar spec-jsp-2.1-%{version}.jar
  ln -sf spec-jsp-2.1-%{version}.jar spec-jsp-2.1.jar
  ln -sf ../geronimo-jta-1.0.1B-api-%{version}.jar spec-jta-1.0.1B-%{version}.jar
  ln -sf spec-jta-1.0.1B-%{version}.jar spec-jta-1.0.1B.jar
  ln -sf ../geronimo-jta-1.1-api-%{version}.jar spec-jta-1.1-%{version}.jar
  ln -sf spec-jta-1.1-%{version}.jar spec-jta-1.1.jar
  ln -sf ../geronimo-servlet-2.4-api-%{version}.jar spec-servlet-2.4-%{version}.jar
  ln -sf spec-servlet-2.4-%{version}.jar spec-servlet-2.4.jar
  ln -sf ../geronimo-servlet-2.5-api-%{version}.jar spec-servlet-2.5-%{version}.jar
  ln -sf spec-servlet-2.5-%{version}.jar spec-servlet-2.5.jar
  ln -sf ../geronimo-stax-1.0-api-%{version}.jar spec-stax-1.0-%{version}.jar
  ln -sf spec-stax-1.0-%{version}.jar spec-stax-1.0.jar
  ln -sf ../geronimo-ws-metadata-2.0-api-%{version}.jar spec-ws-metadata-2.0-%{version}.jar
  ln -sf spec-ws-metadata-2.0-%{version}.jar spec-ws-metadata-2.0.jar
popd
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jaf-1.0.2
    cp -pr geronimo-activation_1.0.2_spec-1.2/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jaf-1.0.2
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jaf-1.1
    cp -pr geronimo-activation_1.1_spec-1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jaf-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/annotation-1.0
    cp -pr geronimo-annotation_1.0_spec-1.1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/annotation-1.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/commonj-1.1
    cp -pr geronimo-spec-commonj/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/commonj-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/corba-1.0
    cp -pr geronimo-spec-corba/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/corba-1.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/corba-2.3
    cp -pr geronimo-spec-corba-2.3/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/corba-2.3
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/ejb-2.1
    cp -pr geronimo-ejb_2.1_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/ejb-2.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/ejb-3.0
    cp -pr geronimo-ejb_3.0_spec-1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/ejb-3.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/el-1.0
    cp -pr geronimo-el_1.0_spec-1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/el-1.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/interceptor-3.0
    cp -pr geronimo-interceptor_3.0_spec-1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/interceptor-3.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/j2ee-connector-1.5
    cp -pr geronimo-j2ee-connector_1.5_spec-1.1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/j2ee-connector-1.5
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/j2ee-deployment-1.1
    cp -pr geronimo-j2ee-deployment_1.1_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/j2ee-deployment-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/javaee-deployment-1.1
    cp -pr geronimo-javaee-deployment_1.1MR3_spec-1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/javaee-deployment-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/j2ee-management-1.0
    cp -pr geronimo-j2ee-management_1.0_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/j2ee-management-1.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/j2ee-management-1.1
    cp -pr geronimo-j2ee-management_1.1_spec-1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/j2ee-management-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/javamail-1.3.1
    cp -pr geronimo-javamail_1.3.1_spec-1.3/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/javamail-1.3.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/javamail-1.4
    cp -pr geronimo-javamail_1.4_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/javamail-1.4
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jaxrpc-1.1
    cp -pr geronimo-jaxrpc_1.1_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jaxrpc-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jaxr-1.0
    cp -pr geronimo-jaxr_1.0_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jaxr-1.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jms-1.1
    cp -pr geronimo-jms_1.1_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jms-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jpa-3.0
    cp -pr geronimo-jpa_3.0_spec-1.1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jpa-3.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jsp-2.0
    cp -pr geronimo-jsp_2.0_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jsp-2.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jsp-2.1
    cp -pr geronimo-jsp_2.1_spec-1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jsp-2.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jta-1.0.1B
    cp -pr geronimo-jta_1.0.1B_spec-1.1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jta-1.0.1B
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jta-1.1
    cp -pr geronimo-jta_1.1_spec-1.1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jta-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/qname-1.1
    cp -pr geronimo-qname_1.1_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/qname-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/saaj-1.1
    cp -pr geronimo-saaj_1.1_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/saaj-1.1
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/servlet-2.4
    cp -pr geronimo-servlet_2.4_spec-1.1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/servlet-2.4
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/servlet-2.5
    cp -pr geronimo-servlet_2.5_spec-1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/servlet-2.5
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/stax-1.0
    cp -pr geronimo-stax-api_1.0_spec-1.0/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/stax-1.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/ws-metadata-2.0
    cp -pr geronimo-ws-metadata_2.0_spec-1.1.1/target/site/apidocs/* \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/ws-metadata-2.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jacc-1.0
    cp -pr geronimo-j2ee-jacc_1.0_spec-1.1/target/site/apidocs/* \
         %{buildroot}%{_javadocdir}/%{name}-%{version}/jacc-1.0
install -d -m 755 \
       %{buildroot}%{_javadocdir}/%{name}-%{version}/jacc-1.1
    cp -pr geronimo-jacc_1.1_spec-1.0/target/site/apidocs/* \
         %{buildroot}%{_javadocdir}/%{name}-%{version}/jacc-1.1
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} # ghost symlink
# documents
install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jaf-1.0.2
    cp -pr geronimo-activation_1.0.2_spec-1.2/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jaf-1.0.2
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jaf-1.1
    cp -pr geronimo-activation_1.1_spec-1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jaf-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/annotation-1.0
    cp -pr geronimo-annotation_1.0_spec-1.1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/annotation-1.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/commonj-1.1
    cp -pr geronimo-spec-commonj/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/commonj-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/corba-2.3
    cp -pr geronimo-spec-corba-2.3/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/corba-2.3
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/ejb-2.1
    cp -pr geronimo-ejb_2.1_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/ejb-2.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/ejb-3.0
    cp -pr geronimo-ejb_3.0_spec-1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/ejb-3.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/el-1.0
    cp -pr geronimo-el_1.0_spec-1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/el-1.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/interceptor-3.0
    cp -pr geronimo-interceptor_3.0_spec-1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/interceptor-3.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-connector-1.5
    cp -pr geronimo-j2ee-connector_1.5_spec-1.1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-connector-1.5
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-deployment-1.1
    cp -pr geronimo-j2ee-deployment_1.1_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-deployment-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/javaee-deployment-1.1
    cp -pr geronimo-javaee-deployment_1.1MR3_spec-1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/javaee-deployment-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-management-1.0
    cp -pr geronimo-j2ee-management_1.0_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-management-1.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-management-1.1
    cp -pr geronimo-j2ee-management_1.1_spec-1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-management-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/javamail-1.3.1
    cp -pr geronimo-javamail_1.3.1_spec-1.3/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/javamail-1.3.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/javamail-1.4
    cp -pr geronimo-javamail_1.4_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/javamail-1.4
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jaxrpc-1.1
    cp -pr geronimo-jaxrpc_1.1_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jaxrpc-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jaxr-1.0
    cp -pr geronimo-jaxr_1.0_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jaxr-1.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jms-1.1
    cp -pr geronimo-jms_1.1_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jms-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jpa-3.0
    cp -pr geronimo-jpa_3.0_spec-1.1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jpa-3.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jsp-2.0
    cp -pr geronimo-jsp_2.0_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jsp-2.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jsp-2.1
    cp -pr geronimo-jsp_2.1_spec-1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jsp-2.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jta-1.0.1B
    cp -pr geronimo-jta_1.0.1B_spec-1.1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jta-1.0.1B
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jta-1.1
    cp -pr geronimo-jta_1.1_spec-1.1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jta-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/qname-1.1
    cp -pr geronimo-qname_1.1_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/qname-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/saaj-1.1
    cp -pr geronimo-saaj_1.1_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/saaj-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/servlet-2.4
    cp -pr geronimo-servlet_2.4_spec-1.1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/servlet-2.4
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/servlet-2.5
    cp -pr geronimo-servlet_2.5_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/servlet-2.5
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/stax-1.0
    cp -pr geronimo-stax-api_1.0_spec-1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/stax-1.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/ws-metadata-2.0
    cp -pr geronimo-ws-metadata_2.0_spec-1.1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/ws-metadata-2.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jacc-1.0
    cp -pr geronimo-j2ee-jacc_1.0_spec-1.1/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jacc-1.0
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/jacc-1.1
    cp -pr geronimo-jacc_1.1_spec-1.0/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/jacc-1.1
install -d -m 755 \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-1.4
    cp -pr geronimo-spec-j2ee/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}/j2ee-1.4
cp -pr etc/LICENSE.txt \
       %{buildroot}%{_docdir}/%{name}-%{version}
fdupes -s %{buildroot}/%{_javadocdir}/%{name}-%{version}


%post poms
%update_maven_depmap

%postun poms
%update_maven_depmap

%post -n geronimo-commonj-1.1-apis
%{_sbindir}/update-alternatives --install %{_javadir}/commonj_apis.jar commonj_apis %{_javadir}/geronimo-commonj-1.1-apis.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/commonj_1_1_apis.jar commonj_1_1_apis %{_javadir}/geronimo-commonj-1.1-apis.jar 10100

%preun -n geronimo-commonj-1.1-apis
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove commonj_apis %{_javadir}/geronimo-commonj-1.1-apis.jar
    %{_sbindir}/update-alternatives --remove commonj_1_1_apis %{_javadir}/geronimo-commonj-1.1-apis.jar
fi

%post -n geronimo-jaf-1.0.2-api
%{_sbindir}/update-alternatives --install %{_javadir}/jaf.jar jaf %{_javadir}/geronimo-jaf-1.0.2-api.jar 10002
%{_sbindir}/update-alternatives --install %{_javadir}/jaf_api.jar jaf_api %{_javadir}/geronimo-jaf-1.0.2-api.jar 10002
%{_sbindir}/update-alternatives --install %{_javadir}/jaf_1_0_2_api.jar jaf_1_0_2_api %{_javadir}/geronimo-jaf-1.0.2-api.jar 10002

%preun -n geronimo-jaf-1.0.2-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jaf %{_javadir}/geronimo-jaf-1.0.2-api.jar
    %{_sbindir}/update-alternatives --remove jaf_api %{_javadir}/geronimo-jaf-1.0.2-api.jar
    %{_sbindir}/update-alternatives --remove jaf_1_0_2_api %{_javadir}/geronimo-jaf-1.0.2-api.jar
fi

%post -n geronimo-jaf-1.1-api
%{_sbindir}/update-alternatives --install %{_javadir}/jaf.jar jaf %{_javadir}/geronimo-jaf-1.1-api.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/jaf_api.jar jaf_api %{_javadir}/geronimo-jaf-1.1-api.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/jaf_1_1_api.jar jaf_1_1_api %{_javadir}/geronimo-jaf-1.1-api.jar 10100

%preun -n geronimo-jaf-1.1-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jaf %{_javadir}/geronimo-jaf-1.1-api.jar
    %{_sbindir}/update-alternatives --remove jaf_api %{_javadir}/geronimo-jaf-1.1-api.jar
    %{_sbindir}/update-alternatives --remove jaf_1_1_api %{_javadir}/geronimo-jaf-1.1-api.jar
fi

%post -n geronimo-annotation-1.0-api
%{_sbindir}/update-alternatives --install %{_javadir}/annotation_api.jar annotation_api %{_javadir}/geronimo-annotation-1.0-api.jar 10000
%{_sbindir}/update-alternatives --install %{_javadir}/annotation_1_0_api.jar annotation_1_0_api %{_javadir}/geronimo-annotation-1.0-api.jar 10000

%preun -n geronimo-annotation-1.0-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove annotation_api %{_javadir}/geronimo-annotation-1.0-api.jar
    %{_sbindir}/update-alternatives --remove annotation_1_0_api %{_javadir}/geronimo-annotation-1.0-api.jar
fi

%post -n geronimo-corba-1.0-apis
%{_sbindir}/update-alternatives --install %{_javadir}/corba_apis.jar corba_apis %{_javadir}/geronimo-corba-1.0-apis.jar 10000
%{_sbindir}/update-alternatives --install %{_javadir}/corba_1_0_apis.jar corba_1_0_apis %{_javadir}/geronimo-corba-1.0-apis.jar 10000

%preun -n geronimo-corba-1.0-apis
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove corba_apis %{_javadir}/geronimo-corba-1.0-apis.jar
    %{_sbindir}/update-alternatives --remove corba_1_0_apis %{_javadir}/geronimo-corba-1.0-apis.jar
fi

%post -n geronimo-corba-2.3-apis
%{_sbindir}/update-alternatives --install %{_javadir}/corba_apis.jar corba_apis %{_javadir}/geronimo-corba-2.3-apis.jar 20300
%{_sbindir}/update-alternatives --install %{_javadir}/corba_2_3_apis.jar corba_2_3_apis %{_javadir}/geronimo-corba-2.3-apis.jar 20300

%preun -n geronimo-corba-2.3-apis
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove corba_apis %{_javadir}/geronimo-corba-2.3-apis.jar
    %{_sbindir}/update-alternatives --remove corba_2_3_apis %{_javadir}/geronimo-corba-2.3-apis.jar
fi


%post -n geronimo-ejb-2.1-api
%{_sbindir}/update-alternatives --install %{_javadir}/ejb.jar ejb %{_javadir}/geronimo-ejb-2.1-api.jar 20100
%{_sbindir}/update-alternatives --install %{_javadir}/ejb_api.jar ejb_api %{_javadir}/geronimo-ejb-2.1-api.jar 20100
%{_sbindir}/update-alternatives --install %{_javadir}/ejb_2_1_api.jar ejb_2_1_api %{_javadir}/geronimo-ejb-2.1-api.jar 20100

%preun -n geronimo-ejb-2.1-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove ejb %{_javadir}/geronimo-ejb-2.1-api.jar
    %{_sbindir}/update-alternatives --remove ejb_api %{_javadir}/geronimo-ejb-2.1-api.jar
    %{_sbindir}/update-alternatives --remove ejb_2_1_api %{_javadir}/geronimo-ejb-2.1-api.jar
fi

%post -n geronimo-ejb-3.0-api
%{_sbindir}/update-alternatives --install %{_javadir}/ejb.jar ejb %{_javadir}/geronimo-ejb-3.0-api.jar 30000
%{_sbindir}/update-alternatives --install %{_javadir}/ejb_api.jar ejb_api %{_javadir}/geronimo-ejb-3.0-api.jar 30000
%{_sbindir}/update-alternatives --install %{_javadir}/ejb_3_0_api.jar ejb_3_0_api %{_javadir}/geronimo-ejb-3.0-api.jar 30000

%preun -n geronimo-ejb-3.0-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove ejb %{_javadir}/geronimo-ejb-3.0-api.jar
    %{_sbindir}/update-alternatives --remove ejb_api %{_javadir}/geronimo-ejb-3.0-api.jar
    %{_sbindir}/update-alternatives --remove ejb_3_0_api %{_javadir}/geronimo-ejb-3.0-api.jar
fi

%post -n geronimo-el-1.0-api
%{_sbindir}/update-alternatives --install %{_javadir}/el_api.jar el_api %{_javadir}/geronimo-el-1.0-api.jar 10000
%{_sbindir}/update-alternatives --install %{_javadir}/el_1_0_api.jar el_1_0_api %{_javadir}/geronimo-el-1.0-api.jar 10000

%preun -n geronimo-el-1.0-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove el_api %{_javadir}/geronimo-el-1.0-api.jar
    %{_sbindir}/update-alternatives --remove el_1_0_api %{_javadir}/geronimo-el-1.0-api.jar
fi

%post -n geronimo-interceptor-3.0-api
%{_sbindir}/update-alternatives --install %{_javadir}/interceptor_api.jar interceptor_api %{_javadir}/geronimo-interceptor-3.0-api.jar 30000
%{_sbindir}/update-alternatives --install %{_javadir}/interceptor_3_0_api.jar interceptor_3_0_api %{_javadir}/geronimo-interceptor-3.0-api.jar 30000

%preun -n geronimo-interceptor-3.0-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove interceptor_api %{_javadir}/geronimo-interceptor-3.0-api.jar
    %{_sbindir}/update-alternatives --remove interceptor_3_0_api %{_javadir}/geronimo-interceptor-3.0-api.jar
fi


%post -n geronimo-j2ee-connector-1.5-api
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee-connector.jar j2ee-connector %{_javadir}/geronimo-j2ee-connector-1.5-api.jar 10500
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee_connector_api.jar j2ee_connector_api %{_javadir}/geronimo-j2ee-connector-1.5-api.jar 10500
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee_connector_1_5_api.jar j2ee_connector_1_5_api %{_javadir}/geronimo-j2ee-connector-1.5-api.jar 10500

%preun -n geronimo-j2ee-connector-1.5-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove j2ee-connector %{_javadir}/geronimo-j2ee-connector-1.5-api.jar
    %{_sbindir}/update-alternatives --remove j2ee_connector_api %{_javadir}/geronimo-j2ee-connector-1.5-api.jar
    %{_sbindir}/update-alternatives --remove j2ee_connector_1_5_api %{_javadir}/geronimo-j2ee-connector-1.5-api.jar
fi

%post -n geronimo-j2ee-deployment-1.1-api
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee-deployment.jar j2ee-deployment %{_javadir}/geronimo-j2ee-deployment-1.1-api.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee_deployment_api.jar j2ee_deployment_api %{_javadir}/geronimo-j2ee-deployment-1.1-api.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee_deployment_1_1_api.jar j2ee_deployment_1_1_api %{_javadir}/geronimo-j2ee-deployment-1.1-api.jar 10100

%preun -n geronimo-j2ee-deployment-1.1-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove j2ee-deployment %{_javadir}/geronimo-j2ee-deployment-1.1-api.jar
    %{_sbindir}/update-alternatives --remove j2ee_deployment_api %{_javadir}/geronimo-j2ee-deployment-1.1-api.jar
    %{_sbindir}/update-alternatives --remove j2ee_deployment_1_1_api %{_javadir}/geronimo-j2ee-deployment-1.1-api.jar
fi

%post -n geronimo-javaee-deployment-1.1-api
%{_sbindir}/update-alternatives --install %{_javadir}/javaee_deployment_api.jar javaee_deployment_api %{_javadir}/geronimo-javaee-deployment-1.1-api.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/javaee_deployment_1_1MR3_api.jar javaee_deployment_1_1MR3_api %{_javadir}/geronimo-javaee-deployment-1.1-api.jar 10100

%preun -n geronimo-javaee-deployment-1.1-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove javaee_deployment_api %{_javadir}/geronimo-javaee-deployment-1.1-api.jar
    %{_sbindir}/update-alternatives --remove javaee_deployment_1_1MR3_api %{_javadir}/geronimo-javaee-deployment-1.1-api.jar
fi


%post -n geronimo-jacc-1.0-api
%{_sbindir}/update-alternatives --install %{_javadir}/jacc.jar jacc %{_javadir}/geronimo-jacc-1.0-api.jar 10000
%{_sbindir}/update-alternatives --install %{_javadir}/jacc_api.jar jacc_api %{_javadir}/geronimo-jacc-1.0-api.jar 10000
%{_sbindir}/update-alternatives --install %{_javadir}/jacc_1_0_api.jar jacc_1_0_api %{_javadir}/geronimo-jacc-1.0-api.jar 10000

%preun -n geronimo-jacc-1.0-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jacc %{_javadir}/geronimo-jacc-1.0-api.jar
    %{_sbindir}/update-alternatives --remove jacc_api %{_javadir}/geronimo-jacc-1.0-api.jar
    %{_sbindir}/update-alternatives --remove jacc_1_0_api %{_javadir}/geronimo-jacc-1.0-api.jar
fi


%post -n geronimo-jacc-1.1-api
%{_sbindir}/update-alternatives --install %{_javadir}/jacc_api.jar jacc_api %{_javadir}/geronimo-jacc-1.1-api.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/jacc_1_1_api.jar jacc_1_1_api %{_javadir}/geronimo-jacc-1.1-api.jar 10100

%preun -n geronimo-jacc-1.1-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jacc_api %{_javadir}/geronimo-jacc-1.1-api.jar
    %{_sbindir}/update-alternatives --remove jacc_1_1_api %{_javadir}/geronimo-jacc-1.1-api.jar
fi


%post -n geronimo-j2ee-management-1.0-api
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee-management.jar j2ee-management %{_javadir}/geronimo-j2ee-management-1.0-api.jar 10000
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee_management_api.jar j2ee_management_api %{_javadir}/geronimo-j2ee-management-1.0-api.jar 10000
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee_management_1_0_api.jar j2ee_management_1_0_api %{_javadir}/geronimo-j2ee-management-1.0-api.jar 10000

%preun -n geronimo-j2ee-management-1.0-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove j2ee-management %{_javadir}/geronimo-j2ee-management-1.0-api.jar
    %{_sbindir}/update-alternatives --remove j2ee_management_api %{_javadir}/geronimo-j2ee-management-1.0-api.jar
    %{_sbindir}/update-alternatives --remove j2ee_management_1_0_api %{_javadir}/geronimo-j2ee-management-1.0-api.jar
fi


%post -n geronimo-j2ee-management-1.1-api
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee-management.jar j2ee-management %{_javadir}/geronimo-j2ee-management-1.1-api.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee_management_api.jar j2ee_management_api %{_javadir}/geronimo-j2ee-management-1.1-api.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee_management_1_1_api.jar j2ee_management_1_1_api %{_javadir}/geronimo-j2ee-management-1.1-api.jar 10100

%preun -n geronimo-j2ee-management-1.1-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove j2ee-management %{_javadir}/geronimo-j2ee-management-1.1-api.jar
    %{_sbindir}/update-alternatives --remove j2ee_management_api %{_javadir}/geronimo-j2ee-management-1.1-api.jar
    %{_sbindir}/update-alternatives --remove j2ee_management_1_1_api %{_javadir}/geronimo-j2ee-management-1.1-api.jar
fi


%post -n geronimo-javamail-1.3.1-api
%{_sbindir}/update-alternatives --install %{_javadir}/javamail.jar javamail %{_javadir}/geronimo-javamail-1.3.1-api.jar 10301
%{_sbindir}/update-alternatives --install %{_javadir}/javamail_api.jar javamail_api %{_javadir}/geronimo-javamail-1.3.1-api.jar 10301
%{_sbindir}/update-alternatives --install %{_javadir}/javamail_1_3_1_api.jar javamail_1_3_1_api %{_javadir}/geronimo-javamail-1.3.1-api.jar 10301

%preun -n geronimo-javamail-1.3.1-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove javamail %{_javadir}/geronimo-javamail-1.3.1-api.jar
    %{_sbindir}/update-alternatives --remove javamail_api %{_javadir}/geronimo-javamail-1.3.1-api.jar
    %{_sbindir}/update-alternatives --remove javamail_1_3_1_api %{_javadir}/geronimo-javamail-1.3.1-api.jar
fi
# Do not provide javamail as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'

%post -n geronimo-javamail-1.4-api
%{_sbindir}/update-alternatives --install %{_javadir}/javamail.jar javamail %{_javadir}/geronimo-javamail-1.4-api.jar 10400
%{_sbindir}/update-alternatives --install %{_javadir}/javamail_api.jar javamail_api %{_javadir}/geronimo-javamail-1.4-api.jar 10400
%{_sbindir}/update-alternatives --install %{_javadir}/javamail_1_4_api.jar javamail_1_4_api %{_javadir}/geronimo-javamail-1.4-api.jar 10400

%preun -n geronimo-javamail-1.4-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove javamail %{_javadir}/geronimo-javamail-1.4-api.jar
    %{_sbindir}/update-alternatives --remove javamail_api %{_javadir}/geronimo-javamail-1.4-api.jar
    %{_sbindir}/update-alternatives --remove javamail_1_4_api %{_javadir}/geronimo-javamail-1.4-api.jar
fi


%post -n geronimo-jaxr-1.0-api
%{_sbindir}/update-alternatives --install %{_javadir}/jaxr.jar jaxr %{_javadir}/geronimo-jaxr-1.0-api.jar 10000
%{_sbindir}/update-alternatives --install %{_javadir}/jaxr_api.jar jaxr_api %{_javadir}/geronimo-jaxr-1.0-api.jar 10000
%{_sbindir}/update-alternatives --install %{_javadir}/jaxr_1_0_api.jar jaxr_1_0_api %{_javadir}/geronimo-jaxr-1.0-api.jar 10000

%preun -n geronimo-jaxr-1.0-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jaxr %{_javadir}/geronimo-jaxr-1.0-api.jar
    %{_sbindir}/update-alternatives --remove jaxr_api %{_javadir}/geronimo-jaxr-1.0-api.jar
    %{_sbindir}/update-alternatives --remove jaxr_1_0_api %{_javadir}/geronimo-jaxr-1.0-api.jar
fi

%post -n geronimo-jaxrpc-1.1-api
%{_sbindir}/update-alternatives --install %{_javadir}/jaxrpc.jar jaxrpc %{_javadir}/geronimo-jaxrpc-1.1-api.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/jaxrpc_api.jar jaxrpc_api %{_javadir}/geronimo-jaxrpc-1.1-api.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/jaxrpc_1_1_api.jar jaxrpc_1_1_api %{_javadir}/geronimo-jaxrpc-1.1-api.jar 10100

%preun -n geronimo-jaxrpc-1.1-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jaxrpc %{_javadir}/geronimo-jaxrpc-1.1-api.jar
    %{_sbindir}/update-alternatives --remove jaxrpc_api %{_javadir}/geronimo-jaxrpc-1.1-api.jar
    %{_sbindir}/update-alternatives --remove jaxrpc_1_1_api %{_javadir}/geronimo-jaxrpc-1.1-api.jar
fi


%post -n geronimo-jms-1.1-api
%{_sbindir}/update-alternatives --install %{_javadir}/jms.jar jms %{_javadir}/geronimo-jms-1.1-api.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/jms_api.jar jms_api %{_javadir}/geronimo-jms-1.1-api.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/jms_1_1_api.jar jms_1_1_api %{_javadir}/geronimo-jms-1.1-api.jar 10100

%preun -n geronimo-jms-1.1-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jms %{_javadir}/geronimo-jms-1.1-api.jar
    %{_sbindir}/update-alternatives --remove jms_api %{_javadir}/geronimo-jms-1.1-api.jar
    %{_sbindir}/update-alternatives --remove jms_1_1_api %{_javadir}/geronimo-jms-1.1-api.jar
fi

%post -n geronimo-jpa-3.0-api
%{_sbindir}/update-alternatives --install %{_javadir}/jpa_api.jar jpa_api %{_javadir}/geronimo-jpa-3.0-api.jar 30000
%{_sbindir}/update-alternatives --install %{_javadir}/jpa_3_0_api.jar jpa_3_0_api %{_javadir}/geronimo-jpa-3.0-api.jar 30000

%preun -n geronimo-jpa-3.0-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jpa_api %{_javadir}/geronimo-jpa-3.0-api.jar
    %{_sbindir}/update-alternatives --remove jpa_3_0_api %{_javadir}/geronimo-jpa-3.0-api.jar
fi

%post -n geronimo-jsp-2.0-api
%{_sbindir}/update-alternatives --install %{_javadir}/jsp.jar jsp %{_javadir}/geronimo-jsp-2.0-api.jar 20000
%{_sbindir}/update-alternatives --install %{_javadir}/jsp_api.jar jsp_api %{_javadir}/geronimo-jsp-2.0-api.jar 20000
%{_sbindir}/update-alternatives --install %{_javadir}/jsp_2_0_api.jar jsp_2_0_api %{_javadir}/geronimo-jsp-2.0-api.jar 20000

%preun -n geronimo-jsp-2.0-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jsp %{_javadir}/geronimo-jsp-2.0-api.jar
    %{_sbindir}/update-alternatives --remove jsp_api %{_javadir}/geronimo-jsp-2.0-api.jar
    %{_sbindir}/update-alternatives --remove jsp_2_0_api %{_javadir}/geronimo-jsp-2.0-api.jar
fi

%post -n geronimo-jsp-2.1-api
%{_sbindir}/update-alternatives --install %{_javadir}/jsp.jar jsp %{_javadir}/geronimo-jsp-2.1-api.jar 20100
%{_sbindir}/update-alternatives --install %{_javadir}/jsp_api.jar jsp_api %{_javadir}/geronimo-jsp-2.1-api.jar 20100
%{_sbindir}/update-alternatives --install %{_javadir}/jsp_2_1_api.jar jsp_2_1_api %{_javadir}/geronimo-jsp-2.1-api.jar 20100

%preun -n geronimo-jsp-2.1-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jsp %{_javadir}/geronimo-jsp-2.1-api.jar
    %{_sbindir}/update-alternatives --remove jsp_api %{_javadir}/geronimo-jsp-2.1-api.jar
    %{_sbindir}/update-alternatives --remove jsp_2_1_api %{_javadir}/geronimo-jsp-2.1-api.jar
fi


%post -n geronimo-jta-1.0.1B-api
%{_sbindir}/update-alternatives --install %{_javadir}/jta.jar jta %{_javadir}/geronimo-jta-1.0.1B-api.jar 10001
%{_sbindir}/update-alternatives --install %{_javadir}/jta_api.jar jta_api %{_javadir}/geronimo-jta-1.0.1B-api.jar 10001
%{_sbindir}/update-alternatives --install %{_javadir}/jta_1_0_1B_api.jar jta_1_0_1B_api %{_javadir}/geronimo-jta-1.0.1B-api.jar 10001

%preun -n geronimo-jta-1.0.1B-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jta %{_javadir}/geronimo-jta-1.0.1B-api.jar
    %{_sbindir}/update-alternatives --remove jta_api %{_javadir}/geronimo-jta-1.0.1B-api.jar
    %{_sbindir}/update-alternatives --remove jta_1_0_1B_api %{_javadir}/geronimo-jta-1.0.1B-api.jar
fi


%post -n geronimo-jta-1.1-api
%{_sbindir}/update-alternatives --install %{_javadir}/jta.jar jta %{_javadir}/geronimo-jta-1.1-api.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/jta_api.jar jta_api %{_javadir}/geronimo-jta-1.1-api.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/jta_1_1_api.jar jta_1_1_api %{_javadir}/geronimo-jta-1.1-api.jar 10100

%preun -n geronimo-jta-1.1-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jta %{_javadir}/geronimo-jta-1.1-api.jar
    %{_sbindir}/update-alternatives --remove jta_api %{_javadir}/geronimo-jta-1.1-api.jar
    %{_sbindir}/update-alternatives --remove jta_1_1_api %{_javadir}/geronimo-jta-1.1-api.jar
fi

%post -n geronimo-qname-1.1-api
%{_sbindir}/update-alternatives --install %{_javadir}/qname_api.jar qname_api %{_javadir}/geronimo-qname-1.1-api.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/qname_1_1_api.jar qname_1_1_api %{_javadir}/geronimo-qname-1.1-api.jar 10100

%postun -n geronimo-qname-1.1-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove qname_api %{_javadir}/geronimo-qname-1.1-api.jar
    %{_sbindir}/update-alternatives --remove qname_1_1_api %{_javadir}/geronimo-qname-1.1-api.jar
fi

%post -n geronimo-saaj-1.1-api
%{_sbindir}/update-alternatives --install %{_javadir}/saaj.jar saaj %{_javadir}/geronimo-saaj-1.1-api.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/saaj_api.jar saaj_api %{_javadir}/geronimo-saaj-1.1-api.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/saaj_1_1_api.jar saaj_1_1_api %{_javadir}/geronimo-saaj-1.1-api.jar 10100

%preun -n geronimo-saaj-1.1-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove saaj %{_javadir}/geronimo-saaj-1.1-api.jar
    %{_sbindir}/update-alternatives --remove saaj_api %{_javadir}/geronimo-saaj-1.1-api.jar
    %{_sbindir}/update-alternatives --remove saaj_1_1_api %{_javadir}/geronimo-saaj-1.1-api.jar
fi

%post -n geronimo-servlet-2.4-api
%{_sbindir}/update-alternatives --install %{_javadir}/servlet.jar servlet %{_javadir}/geronimo-servlet-2.4-api.jar 20400
%{_sbindir}/update-alternatives --install %{_javadir}/servlet_api.jar servlet_api %{_javadir}/geronimo-servlet-2.4-api.jar 20400
%{_sbindir}/update-alternatives --install %{_javadir}/servlet_2_4_api.jar servlet_2_4_api %{_javadir}/geronimo-servlet-2.4-api.jar 20400

%preun -n geronimo-servlet-2.4-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove servlet %{_javadir}/geronimo-servlet-2.4-api.jar
    %{_sbindir}/update-alternatives --remove servlet_api %{_javadir}/geronimo-servlet-2.4-api.jar
    %{_sbindir}/update-alternatives --remove servlet_2_4_api %{_javadir}/geronimo-servlet-2.4-api.jar
fi

%post -n geronimo-servlet-2.5-api
%{_sbindir}/update-alternatives --install %{_javadir}/servlet.jar servlet %{_javadir}/geronimo-servlet-2.5-api.jar 20500
%{_sbindir}/update-alternatives --install %{_javadir}/servlet_api.jar servlet_api %{_javadir}/geronimo-servlet-2.5-api.jar 20500
%{_sbindir}/update-alternatives --install %{_javadir}/servlet_2_5_api.jar servlet_2_5_api %{_javadir}/geronimo-servlet-2.5-api.jar 20500

%preun -n geronimo-servlet-2.5-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove servlet %{_javadir}/geronimo-servlet-2.5-api.jar
    %{_sbindir}/update-alternatives --remove servlet_api %{_javadir}/geronimo-servlet-2.5-api.jar
    %{_sbindir}/update-alternatives --remove servlet_2_5_api %{_javadir}/geronimo-servlet-2.5-api.jar
fi

%post -n geronimo-stax-1.0-api
%{_sbindir}/update-alternatives --install %{_javadir}/stax_api.jar stax_api %{_javadir}/geronimo-stax-1.0-api.jar 10000
%{_sbindir}/update-alternatives --install %{_javadir}/stax_1_0_api.jar stax_1_0_api %{_javadir}/geronimo-stax-1.0-api.jar 10000

%preun -n geronimo-stax-1.0-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove stax_api %{_javadir}/geronimo-stax-1.0-api.jar
    %{_sbindir}/update-alternatives --remove stax_1_0_api %{_javadir}/geronimo-stax-1.0-api.jar
fi

%post -n geronimo-ws-metadata-2.0-api
%{_sbindir}/update-alternatives --install %{_javadir}/ws_metadata_api.jar ws_metadata_api %{_javadir}/geronimo-ws-metadata-2.0-api.jar 20000
%{_sbindir}/update-alternatives --install %{_javadir}/ws_metadata_2_0_api.jar ws_metadata_2_0_api %{_javadir}/geronimo-ws-metadata-2.0-api.jar 20000

%preun -n geronimo-ws-metadata-2.0-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove ws_metadata_api %{_javadir}/geronimo-ws-metadata-2.0-api.jar
    %{_sbindir}/update-alternatives --remove ws_metadata_2_0_api %{_javadir}/geronimo-ws-metadata-2.0-api.jar
fi

%post -n geronimo-j2ee-1.4-apis
%{_sbindir}/update-alternatives --install %{_javadir}/jaf_api.jar jaf_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10002
%{_sbindir}/update-alternatives --install %{_javadir}/jaf_1_0_2_api.jar jaf_1_0_2_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10002
%{_sbindir}/update-alternatives --install %{_javadir}/commonj_apis.jar commonj_apis %{_javadir}/geronimo-j2ee-1.4-apis.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/commonj_1_1_apis.jar commonj_1_1_apis %{_javadir}/geronimo-j2ee-1.4-apis.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/corba_apis.jar corba_apis %{_javadir}/geronimo-j2ee-1.4-apis.jar 20300
%{_sbindir}/update-alternatives --install %{_javadir}/corba_2_3_apis.jar corba_2_3_apis %{_javadir}/geronimo-j2ee-1.4-apis.jar 20300
%{_sbindir}/update-alternatives --install %{_javadir}/ejb_api.jar ejb_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 20100
%{_sbindir}/update-alternatives --install %{_javadir}/ejb_2_1_api.jar ejb_2_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 20100
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee-connector.jar j2ee-connector %{_javadir}/geronimo-j2ee-1.4-apis.jar 10500
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee_connector_api.jar j2ee_connector_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10500
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee_connector_1_5_api.jar j2ee_1_5_connector_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10500
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee_deployment_api.jar j2ee_deployment_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee_deployment_1_1_api.jar j2ee_deployment_1_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee_management_api.jar j2ee_management_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10000
%{_sbindir}/update-alternatives --install %{_javadir}/j2ee_management_1_0_api.jar j2ee_management_1_0_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10000
%{_sbindir}/update-alternatives --install %{_javadir}/jacc_api.jar jacc_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10000
%{_sbindir}/update-alternatives --install %{_javadir}/jacc_1_0_api.jar jacc_1_0_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10000
%{_sbindir}/update-alternatives --install %{_javadir}/javamail_api.jar javamail_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10301
%{_sbindir}/update-alternatives --install %{_javadir}/javamail_1_3_1_api.jar javamail_1_3_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10301
%{_sbindir}/update-alternatives --install %{_javadir}/jaxr_api.jar jaxr_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10000
%{_sbindir}/update-alternatives --install %{_javadir}/jaxr_1_0_api.jar jaxr_1_0_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10000
%{_sbindir}/update-alternatives --install %{_javadir}/jaxrpc_api.jar jaxrpc_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/jaxrpc_1_1_api.jar jaxrpc_1_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/jms_api.jar jms_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/jms_1_1_api.jar jms_1_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/jsp_api.jar jsp_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/jsp_2_0_api.jar jsp_2_0_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/jta_api.jar jta_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10001
%{_sbindir}/update-alternatives --install %{_javadir}/jta_1_0_1B_api.jar jta_1_0_1B_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10001
%{_sbindir}/update-alternatives --install %{_javadir}/qname_api.jar qname_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/qname_1_1_api.jar qname_1_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/saaj_api.jar saaj_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/saaj_1_1_api.jar saaj_1_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 10100
%{_sbindir}/update-alternatives --install %{_javadir}/servlet_api.jar servlet_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 20400
%{_sbindir}/update-alternatives --install %{_javadir}/servlet_2_4_api.jar servlet_2_4_api %{_javadir}/geronimo-j2ee-1.4-apis.jar 20400

%preun -n geronimo-j2ee-1.4-apis
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jaf_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove jaf_1_0_2_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove commonj_apis %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove commonj_1_1_apis %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove corba_apis %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove corba_2_3_apis %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove ejb_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove ejb_2_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove j2ee-connector %{_javadir}/geronimo-j2ee-connector-1.5-api.jar
    %{_sbindir}/update-alternatives --remove j2ee_connector_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove j2ee_connector_1_5_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove j2ee_deployment_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove j2ee_deployment_1_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove j2ee_management_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove j2ee_management_1_0_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove jacc_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove jacc_1_0_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove javamail_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove javamail_1_3_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove jaxr_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove jaxr_1_0_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove jaxrpc_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove jaxrpc_1_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove jms_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove jms_1_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove jsp_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove jsp_2_0_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove jta_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove jta_1_0_1B_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove qname_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove qname_1_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove saaj_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove saaj_1_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove servlet_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
    %{_sbindir}/update-alternatives --remove servlet_2_4_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
fi

%files
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%dir %{_javadir}/geronimo
%{_javadir}/geronimo/*

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/*

%files poms
%defattr(0644,root,root,0755)
%config %{_mavendepmapfragdir}/*
%{_mavenpomdir}/*

%files -n geronimo-commonj-1.1-apis
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-commonj-1.1-apis*.jar
%ghost %{_javadir}/commonj_1_1_apis.jar
%ghost %{_javadir}/commonj_apis.jar
%doc %{_docdir}/%{name}-%{version}/commonj-1.1/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/commonj-1.1
%dir %{_docdir}/%{name}-%{version}

%files -n geronimo-jaf-1.0.2-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-jaf-1.0.2-api*.jar
%doc %{_docdir}/%{name}-%{version}/jaf-1.0.2/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/jaf-1.0.2
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/jaf.jar
%ghost %{_javadir}/jaf_api.jar
%ghost %{_javadir}/jaf_1_0_2_api.jar

%files -n geronimo-jaf-1.1-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-jaf-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/jaf-1.1/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/jaf-1.1
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/jaf.jar
%ghost %{_javadir}/jaf_api.jar
%ghost %{_javadir}/jaf_1_1_api.jar

%files -n geronimo-annotation-1.0-api
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}-%{version}/annotation-1.0/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/annotation-1.0
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/annotation_api.jar
%ghost %{_javadir}/annotation_1_0_api.jar
%{_javadir}/geronimo-annotation-1.0-api*.jar

%files -n geronimo-corba-1.0-apis
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-corba-1.0-apis*.jar
%ghost %{_javadir}/corba_apis.jar
%ghost %{_javadir}/corba_1_0_apis.jar

%files -n geronimo-corba-2.3-apis
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-corba-2.3-apis*.jar
%doc %{_docdir}/%{name}-%{version}/corba-2.3/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/corba-2.3
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/corba_apis.jar
%ghost %{_javadir}/corba_2_3_apis.jar


%files -n geronimo-ejb-2.1-api
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}-%{version}/ejb-2.1/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/ejb-2.1
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/ejb.jar
%ghost %{_javadir}/ejb_api.jar
%ghost %{_javadir}/ejb_2_1_api.jar
%{_javadir}/geronimo-ejb-2.1-api*.jar

%files -n geronimo-ejb-3.0-api
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}-%{version}/ejb-3.0/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/ejb-3.0
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/ejb.jar
%ghost %{_javadir}/ejb_api.jar
%ghost %{_javadir}/ejb_3_0_api.jar
%{_javadir}/geronimo-ejb-3.0-api*.jar

%files -n geronimo-el-1.0-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-el-1.0-api*.jar
%doc %{_docdir}/%{name}-%{version}/el-1.0/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/el-1.0
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/el_api.jar
%ghost %{_javadir}/el_1_0_api.jar

%files -n geronimo-interceptor-3.0-api
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}-%{version}/interceptor-3.0/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/interceptor-3.0
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/interceptor_api.jar
%ghost %{_javadir}/interceptor_3_0_api.jar
%{_javadir}/geronimo-interceptor-3.0-api*.jar

%files -n geronimo-j2ee-1.4-apis
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-j2ee-1.4-apis*.jar
%doc %{_docdir}/%{name}-%{version}/j2ee-1.4/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/j2ee-1.4
%dir %{_docdir}/%{name}-%{version}

%files -n geronimo-j2ee-connector-1.5-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-j2ee-connector-1.5-api*.jar
%doc %{_docdir}/%{name}-%{version}/j2ee-connector-1.5/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/j2ee-connector-1.5
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/j2ee-connector.jar
%ghost %{_javadir}/j2ee_connector_api.jar
%ghost %{_javadir}/j2ee_connector_1_5_api.jar

%files -n geronimo-j2ee-deployment-1.1-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-j2ee-deployment-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/j2ee-deployment-1.1/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/j2ee-deployment-1.1
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/j2ee-deployment.jar
%ghost %{_javadir}/j2ee_deployment_api.jar
%ghost %{_javadir}/j2ee_deployment_1_1_api.jar

%files -n geronimo-javaee-deployment-1.1-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-javaee-deployment-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/javaee-deployment-1.1/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/javaee-deployment-1.1
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/javaee_deployment_api.jar
%ghost %{_javadir}/javaee_deployment_1_1MR3_api.jar

%files -n geronimo-jacc-1.0-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-jacc-1.0-api*.jar
%doc %{_docdir}/%{name}-%{version}/jacc-1.0/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/jacc-1.0
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/jacc.jar
%ghost %{_javadir}/jacc_api.jar
%ghost %{_javadir}/jacc_1_0_api.jar

%files -n geronimo-jacc-1.1-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-jacc-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/jacc-1.1/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/jacc-1.1
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/jacc_api.jar
%ghost %{_javadir}/jacc_1_1_api.jar

%files -n geronimo-j2ee-management-1.0-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-j2ee-management-1.0-api*.jar
%doc %{_docdir}/%{name}-%{version}/j2ee-management-1.0/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/j2ee-management-1.0
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/j2ee-management.jar
%ghost %{_javadir}/j2ee_management_api.jar
%ghost %{_javadir}/j2ee_management_1_0_api.jar

%files -n geronimo-j2ee-management-1.1-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-j2ee-management-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/j2ee-management-1.1/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/j2ee-management-1.1
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/j2ee-management.jar
%ghost %{_javadir}/j2ee_management_api.jar
%ghost %{_javadir}/j2ee_management_1_1_api.jar

%files -n geronimo-javamail-1.3.1-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-javamail-1.3.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/javamail-1.3.1/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/javamail-1.3.1
%dir %{_docdir}/%{name}-%{version}
# Do not provide it as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
%ghost %{_javadir}/javamail_api.jar
%ghost %{_javadir}/javamail_1_3_1_api.jar

%files -n geronimo-javamail-1.4-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-javamail-1.4-api*.jar
%doc %{_docdir}/%{name}-%{version}/javamail-1.4/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/javamail-1.4
%dir %{_docdir}/%{name}-%{version}
# Do not provide it as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
%ghost %{_javadir}/javamail_api.jar
%ghost %{_javadir}/javamail_1_4_api.jar

%files -n geronimo-jaxr-1.0-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-jaxr-1.0-api*.jar
%doc %{_docdir}/%{name}-%{version}/jaxr-1.0/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/jaxr-1.0
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/jaxr.jar
%ghost %{_javadir}/jaxr_api.jar
%ghost %{_javadir}/jaxr_1_0_api.jar

%files -n geronimo-jaxrpc-1.1-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-jaxrpc-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/jaxrpc-1.1/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/jaxrpc-1.1
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/jaxrpc.jar
%ghost %{_javadir}/jaxrpc_api.jar
%ghost %{_javadir}/jaxrpc_1_1_api.jar

%files -n geronimo-jms-1.1-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-jms-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/jms-1.1/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/jms-1.1
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/jms.jar
%ghost %{_javadir}/jms_api.jar
%ghost %{_javadir}/jms_1_1_api.jar

%files -n geronimo-jpa-3.0-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-jpa-3.0-api*.jar
%doc %{_docdir}/%{name}-%{version}/jpa-3.0/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/jpa-3.0
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/jpa_api.jar
%ghost %{_javadir}/jpa_3_0_api.jar

%files -n geronimo-jsp-2.0-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-jsp-2.0-api*.jar
%doc %{_docdir}/%{name}-%{version}/jsp-2.0/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/jsp-2.0
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/jsp.jar
%ghost %{_javadir}/jsp_api.jar
%ghost %{_javadir}/jsp_2_0_api.jar

%files -n geronimo-jsp-2.1-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-jsp-2.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/jsp-2.1/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/jsp-2.1
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/jsp.jar
%ghost %{_javadir}/jsp_api.jar
%ghost %{_javadir}/jsp_2_1_api.jar

%files -n geronimo-jta-1.0.1B-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-jta-1.0.1B-api*.jar
%doc %{_docdir}/%{name}-%{version}/jta-1.0.1B/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/jta-1.0.1B
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/jta.jar
%ghost %{_javadir}/jta_api.jar
%ghost %{_javadir}/jta_1_0_1B_api.jar

%files -n geronimo-jta-1.1-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-jta-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/jta-1.1/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/jta-1.1
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/jta.jar
%ghost %{_javadir}/jta_api.jar
%ghost %{_javadir}/jta_1_1_api.jar

%files -n geronimo-qname-1.1-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-qname-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/qname-1.1/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/qname-1.1
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/qname_api.jar
%ghost %{_javadir}/qname_1_1_api.jar

%files -n geronimo-saaj-1.1-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-saaj-1.1-api*.jar
%doc %{_docdir}/%{name}-%{version}/saaj-1.1/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/saaj-1.1
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/saaj.jar
%ghost %{_javadir}/saaj_api.jar
%ghost %{_javadir}/saaj_1_1_api.jar

%files -n geronimo-servlet-2.4-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-servlet-2.4-api*.jar
%doc %{_docdir}/%{name}-%{version}/servlet-2.4/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/servlet-2.4
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/servlet.jar
%ghost %{_javadir}/servlet_api.jar
%ghost %{_javadir}/servlet_2_4_api.jar

%files -n geronimo-servlet-2.5-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-servlet-2.5-api*.jar
%doc %{_docdir}/%{name}-%{version}/servlet-2.5/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/servlet-2.5
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/servlet.jar
%ghost %{_javadir}/servlet_api.jar
%ghost %{_javadir}/servlet_2_5_api.jar

%files -n geronimo-stax-1.0-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-stax-1.0-api*.jar
%doc %{_docdir}/%{name}-%{version}/stax-1.0/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/stax-1.0
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/stax_api.jar
%ghost %{_javadir}/stax_1_0_api.jar

%files -n geronimo-ws-metadata-2.0-api
%defattr(0644,root,root,0755)
%{_javadir}/geronimo-ws-metadata-2.0-api*.jar
%doc %{_docdir}/%{name}-%{version}/ws-metadata-2.0/LICENSE.txt
%dir %{_docdir}/%{name}-%{version}/ws-metadata-2.0
%dir %{_docdir}/%{name}-%{version}
%ghost %{_javadir}/ws_metadata_api.jar
%ghost %{_javadir}/ws_metadata_2_0_api.jar

