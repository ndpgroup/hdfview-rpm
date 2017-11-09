Name:		hdfview
Version:	3.0.0
Release:	1%{?dist}
Summary:	HDFView is a visual tool written in Java for browsing and editing HDF files

#Group:		
License:	Copyright 2006-2017 by The HDF Group
URL:		https://s3.amazonaws.com/hdf-wordpress-1/wp-content/uploads/manual/HDFView-3.0-centos7.tar.gz
Source0:	HDFView-3.0-centos7.tar.gz

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	java >= 1:1.7.0

%define __jar_repack %{nil}


%description
HDFView is a visual tool written in Java for browsing and editing HDF (HDF5 and HDF4) files. Using HDFView, you can:
 * View a file hierarchy in a tree structure
 * Create new files, add or delete groups and datasets
 * View and modify the content of a dataset
 * Add, delete and modify attributes
HDFView uses the Java HDF Object Package, which implements HDF4 and HDF5 data objects in an object-oriented form.


%prep
%setup -q -c


%build
mkdir -p %{name}
offset=`grep -m 1 -a gunzip HDFView-%{version}-Linux.sh | cut -d ' ' -f 3`
tail -n $offset HDFView-%{version}-Linux.sh | tar -zxpf - --exclude=jre --strip-components=2 -C %{name}
sed -i "s|@JAVABIN@|/usr/bin|" %{name}/%{name}.sh
sed -i "s|@INSTALLDIR@|/opt/%{name}|" %{name}/%{name}.sh


%install
#sh -x ./HDFView-3.0.0-Linux.sh --skip-license --exclude-subdir --prefix=$RPM_BUILD_ROOT/opt
mkdir -p $RPM_BUILD_ROOT/opt
tar -cf - %{name} | tar -xpf - -C $RPM_BUILD_ROOT/opt
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
ln -s /opt/%{name}/%{name}.sh $RPM_BUILD_ROOT/%{_bindir}/%{name}

%files
%defattr(-,root,root
%doc README.txt
%doc COPYING
%doc /opt/%{name}/share/doc
%doc /opt/%{name}/share/samples
%attr(755,root,root) /opt/%{name}/%{name}.sh
%dir /opt/%{name}/lib
%attr(755,root,root) /opt/%{name}/lib/*.so
/opt/%{name}/lib/*.jar
%{_bindir}/%{name}


%changelog
* Wed Nov 08 2017 James E. Flemer <james.flemer@ndpgroup.com> - 3.0.0-1
- Initial spec
