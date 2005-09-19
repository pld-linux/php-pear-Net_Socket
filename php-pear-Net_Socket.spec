%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Socket
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - network socket interface
Summary(pl):	%{_pearname} - interfejs gniazd sieciowych
Name:		php-pear-%{_pearname}
Version:	1.0.6
Release:	1.2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f961deffb093a58eb4c48478de1b27ed
URL:		http://pear.php.net/package/Net_Socket/
BuildRequires:	rpm-php-pearprov >= 4.4.2-10.2
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_Socket is a class interface to TCP sockets. It provides blocking
and non-blocking operation, with different reading and writing modes
(byte-wise, block-wise, line-wise and special formats like network
byte-order ip addresses).

In PEAR status of this package is: %{_status}.

%description -l pl
Net_Socket to klasa z interfejsem do gniazd TCP. Umo¿liwia operacje
blokuj±ce i nieblokuj±ce, z ró¿nymi trybami odczytu i zapisu
(bajtowym, blokowym, liniowym i specjalnymi formatami, jak bajty w
kolejno¶ci adresów sieciowych).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
