%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       Socket
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Network Socket Interface
Summary(pl):	%{_pearname} - Interfejs socketów sieciowych
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	f2b5f199a8586b855a549c2dccfbbd81
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_Socket is a class interface to TCP sockets. It provides blocking
and non-blocking operation, with different reading and writing modes
(byte-wise, block-wise, line-wise and special formats like network
byte-order ip addresses).

%description -l pl
Net_Socket to klasa z interfejsem do gniazd TCP. Umo¿liwia operacje
blokuj±ce i nieblokuj±ce, z ró¿nymi trybami odczytu i zapisu
(bajtowym, blokowym, liniowym i specjalnymi formatami, jak bajty w
kolejno¶ci adresów sieciowych).

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
