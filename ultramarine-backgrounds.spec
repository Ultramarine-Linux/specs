%global _disable_source_fetch 0

# key value:
%define _source_refspec b9579c24e29a93c9516bc7333bc74c4148961ec4

%define _source_baseurl https://gitlab.ultramarine-linux.org/dist-pkgs/sources/-/raw/%{_source_refspec}/ultramarine-backgrounds

Name: ultramarine-backgrounds
Version: 34
Release: 2
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
cp -v %{SOURCE200} %{buildroot}/%{_datadir}/backgrounds/ultramarine-linux/

%files
%license COPYING
%dir %{_datadir}/backgrounds/ultramarine-linux/
%{_datadir}/backgrounds/ultramarine-linux/
