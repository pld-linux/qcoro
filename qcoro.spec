#
# TODO Qt6
# Conditional build:
%bcond_with	tests		# build with tests
%define		qtver		5.15.2
Summary:	QCoro - Coroutines for Qt5 and Qt6
Name:		qcoro
Version:	0.8.0
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://github.com/danvratil/qcoro/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	e7f7b073a42c863e123612243f2045bd
URL:		https://github.com/danvratil/qcoro
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.15.9
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Qml-devel >= 5.15.9
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5WebSockets-devel
BuildRequires:	Qt5Widgets-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The QCoro library provides set of tools to make use of C++20
coroutines with Qt.

%package devel
Summary:	Header files for %{name} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{name}.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%ghost %{_libdir}/libQCoro5Core.so.0
%attr(755,root,root) %{_libdir}/libQCoro5Core.so.*.*.*
%ghost %{_libdir}/libQCoro5DBus.so.0
%attr(755,root,root) %{_libdir}/libQCoro5DBus.so.*.*.*
%ghost %{_libdir}/libQCoro5Network.so.0
%attr(755,root,root) %{_libdir}/libQCoro5Network.so.*.*.*
%ghost %{_libdir}/libQCoro5Qml.so.0
%attr(755,root,root) %{_libdir}/libQCoro5Qml.so.*.*.*
%ghost %{_libdir}/libQCoro5Quick.so.0
%attr(755,root,root) %{_libdir}/libQCoro5Quick.so.*.*.*
%ghost %{_libdir}/libQCoro5WebSockets.so.0
%attr(755,root,root) %{_libdir}/libQCoro5WebSockets.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/qcoro5
%{_libdir}/cmake/QCoro5
%{_libdir}/cmake/QCoro5Core
%{_libdir}/cmake/QCoro5Coro
%{_libdir}/cmake/QCoro5DBus
%{_libdir}/cmake/QCoro5Network
%{_libdir}/cmake/QCoro5Qml
%{_libdir}/cmake/QCoro5Quick
%{_libdir}/cmake/QCoro5WebSockets
%{_libdir}/libQCoro5Core.so
%{_libdir}/libQCoro5DBus.so
%{_libdir}/libQCoro5Network.so
%{_libdir}/libQCoro5Qml.so
%{_libdir}/libQCoro5Quick.so
%{_libdir}/libQCoro5WebSockets.so
%{_libdir}/qt5/mkspecs/modules/qt_QCoroCore.pri
%{_libdir}/qt5/mkspecs/modules/qt_QCoroCoro.pri
%{_libdir}/qt5/mkspecs/modules/qt_QCoroDBus.pri
%{_libdir}/qt5/mkspecs/modules/qt_QCoroNetwork.pri
%{_libdir}/qt5/mkspecs/modules/qt_QCoroQml.pri
%{_libdir}/qt5/mkspecs/modules/qt_QCoroQuick.pri
%{_libdir}/qt5/mkspecs/modules/qt_QCoroWebSockets.pri
