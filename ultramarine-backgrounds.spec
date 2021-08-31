%global _disable_source_fetch 0

# key value:
%define _source_refspec 0a5dcc45768b5d0440e11c8152f6ca5a3cea1b84

%define _source_baseurl https://gitlab.ultramarine-linux.org/dist-pkgs/sources/-/raw/%{_source_refspec}/ultramarine-backgrounds

Name: ultramarine-backgrounds
Version: 34
Release: 3
BuildArch: noarch
# details for the artworks' licenses can be seen in the COPYING file
License: CC-BY-SA and CC0
Summary: Ultramarine Linux backgrounds

# licensing information
Source0: %{_source_baseurl}/COPYING

# CC0 artworks
Source100: %{_source_baseurl}/cc0/blue-ocean.jpg
Source101: %{_source_baseurl}/cc0/silhouette-of-mountain.jpg
Source102: %{_source_baseurl}/cc0/by-ren-ran.jpg
Source103: %{_source_baseurl}/cc0/blue-and-green-abstract-painting.jpg
Source104: %{_source_baseurl}/cc0/A-curved-facade-covered-in-white-latticework-photo.jpg
Source105: %{_source_baseurl}/cc0/white-and-gray-optical-illusion-photo.jpg

# CC-BY-SA artworks
Source200: %{_source_baseurl}/cc-by-sa/star-trails.jpg

%description
This package contains desktop backgrounds for the Ultramarine Linux default theme.

%prep

%build

%install
mkdir -p %{buildroot}/%{_datadir}/licenses/%{name}/
cp -v %{SOURCE0} %{buildroot}/%{_datadir}/licenses/%{name}/

mkdir -p %{buildroot}/%{_datadir}/backgrounds/ultramarine-linux/default
cp -v %{SOURCE100} %{buildroot}/%{_datadir}/backgrounds/ultramarine-linux/default/
cp -v %{SOURCE101} %{buildroot}/%{_datadir}/backgrounds/ultramarine-linux/
cp -v %{SOURCE102} %{buildroot}/%{_datadir}/backgrounds/ultramarine-linux/
cp -v %{SOURCE103} %{buildroot}/%{_datadir}/backgrounds/ultramarine-linux/
cp -v %{SOURCE104} %{buildroot}/%{_datadir}/backgrounds/ultramarine-linux/
cp -v %{SOURCE105} %{buildroot}/%{_datadir}/backgrounds/ultramarine-linux/
cp -v %{SOURCE200} %{buildroot}/%{_datadir}/backgrounds/ultramarine-linux/

%files
%license COPYING
%dir %{_datadir}/backgrounds/ultramarine-linux/
%{_datadir}/backgrounds/ultramarine-linux/
