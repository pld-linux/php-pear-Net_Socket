%include	/usr/lib/rpm/macros.php
%define		_pearname	Net_Socket
Summary:	Net_Socket - Network Socket Interface
Summary(pl):	Net_Socket - Interfejs socketów sieciowych
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
BuildRequires:	rpm-php-pearprov
URL:		http://pear.php.net/
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
cd %{_pearname}-%{version}

install -d $RPM_BUILD_ROOT%{php_pear_dir}/Net

install *.php			$RPM_BUILD_ROOT%{php_pear_dir}/Net

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/Net
%{php_pear_dir}/Net/*.php
