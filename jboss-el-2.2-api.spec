%global pkg_name jboss-el-2.2-api
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global namedreltag .20120212git2fabd8
%global namedversion %{version}%{?namedreltag}

Name: %{?scl_prefix}%{pkg_name}
Version: 1.0.1
Release: 0.7%{namedreltag}.13%{?dist}
Summary: Expression Language 2.2 API
License: CDDL or GPLv2 with exceptions
URL: http://www.jboss.org

# git clone git://github.com/jboss/jboss-el-api_spec.git jboss-el-2.2-api
# cd jboss-el-2.2-api
# git archive --format=tar --prefix=jboss-el-2.2-api-1.0.1/ 2fabd8013214d50b03a65853673c111bdf39e87f | xz > jboss-el-2.2-api-1.0.1.20120212git2fabd8.tar.xz
Source0: %{pkg_name}-%{namedversion}.tar.xz

BuildRequires: %{?scl_prefix}jboss-specs-parent
BuildRequires: %{?scl_prefix_java_common}javapackages-tools
BuildRequires: %{?scl_prefix}maven-local
BuildRequires: %{?scl_prefix}maven-compiler-plugin
BuildRequires: %{?scl_prefix}maven-enforcer-plugin
BuildRequires: %{?scl_prefix}maven-install-plugin
BuildRequires: %{?scl_prefix}maven-jar-plugin
BuildRequires: %{?scl_prefix}maven-javadoc-plugin


BuildArch: noarch


%description
Expression Language 2.2 API classes.


%package javadoc
Summary: Javadocs for %{pkg_name}


%description javadoc	
This package contains the API documentation for %{pkg_name}.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
mvn-rpmbuild install javadoc:aggregate
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
install -pm 644 target/jboss-el-api_2.2_spec-%{version}-SNAPSHOT.jar %{buildroot}%{_javadir}/%{pkg_name}.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{pkg_name}.pom

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# Dependencies map:
%add_maven_depmap JPP-%{pkg_name}.pom %{pkg_name}.jar -a "javax.el:el-api"
%{?scl:EOF}


%files -f .mfiles
%doc LICENSE
%doc README


%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE
%doc README


%changelog
* Mon Feb 08 2016 Michal Srb <msrb@redhat.com> - 1.0.1-0.7.20120212git2fabd8.13
- Fix BR on maven-local & co.

* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 1.0.1-0.7.20120212git2fabd8.12
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.0.1-0.7.20120212git2fabd8.11
- maven33 rebuild

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.0.1-0.7.20120212git2fabd8.10
- Mass rebuild 2015-01-13

* Wed Jan 07 2015 Michal Srb <msrb@redhat.com> - 1.0.1-0.7.20120212git2fabd8.9
- Migrate to .mfiles

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.0.1-0.7.20120212git2fabd8.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-0.7.20120212git2fabd8.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-0.7.20120212git2fabd8.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-0.7.20120212git2fabd8.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-0.7.20120212git2fabd8.4
- Remove requires on java

* Mon Feb 17 2014 Michal Srb <msrb@redhat.com> - 1.0.1-0.7.20120212git2fabd8.3
- SCL-ize BR/R

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-0.7.20120212git2fabd8.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-0.7.20120212git2fabd8.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0.1-0.7.20120212git2fabd8
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.6.20120212git2fabd8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.1-0.5.20120212git2fabd8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jul 24 2012 Juan Hernandez <juan.hernandez@redhat.com> - 1.0.1-0.4.20120212git2fabd8
- Added maven-enforcer-plugin build time dependency

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.3.20120212git2fabd8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 14 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-0.2.20120212git2fabd8
- Added additional POM mapping: javax.el:el-api

* Mon Mar 12 2012 Juan Hernandez <juan.hernandez@redhat.com> 1.0.1-0.1.20120212git2fabd8
- Packaging after license cleanup upstream

* Fri Feb 24 2012 Juan Hernandez <juan.hernandez@redhat.com> 1.0.0-2
- Cleanup of the spec file

* Wed Feb 1 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.0-1
- Initial packaging

