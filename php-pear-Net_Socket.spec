%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Socket
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - network socket interface
Summary(pl):	%{_pearname} - interfejs gniazd sieciowych
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	aaa5e47d8e27e2ab3cba1e377f28eeef
URL:		http://pear.php.net/package/Net_Socket/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_Socket is a class interface to TCP sockets. It provides blocking
and non-blocking operation, with different reading and writing modes
(byte-wise, block-wise, line-wise and special formats like network
byte-order ip addresses).

This class has in PEAR status: %{_status}.

%description -l pl
Net_Socket to klasa z interfejsem do gniazd TCP. Umo�liwia operacje
blokuj�ce i nieblokuj�ce, z r�nymi trybami odczytu i zapisu
(bajtowym, blokowym, liniowym i specjalnymi formatami, jak bajty w
kolejno�ci adres�w sieciowych).

Ta klasa ma w PEAR status: %{_status}.

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
