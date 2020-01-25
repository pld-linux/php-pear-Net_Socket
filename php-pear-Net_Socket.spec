%define		status		stable
%define		pearname	Net_Socket
Summary:	%{pearname} - network socket interface
Summary(pl.UTF-8):	%{pearname} - interfejs gniazd sieciowych
Name:		php-pear-%{pearname}
Version:	1.2.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	7969d584a23e7695a3ae0399fc555fb3
URL:		http://pear.php.net/package/Net_Socket/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_Socket is a class interface to TCP sockets. It provides blocking
and non-blocking operation, with different reading and writing modes
(byte-wise, block-wise, line-wise and special formats like network
byte-order ip addresses).

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Net_Socket to klasa z interfejsem do gniazd TCP. Umożliwia operacje
blokujące i nieblokujące, z różnymi trybami odczytu i zapisu
(bajtowym, blokowym, liniowym i specjalnymi formatami, jak bajty w
kolejności adresów sieciowych).

Ta klasa ma w PEAR status: %{status}.

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
%{php_pear_dir}/Net/*.php
