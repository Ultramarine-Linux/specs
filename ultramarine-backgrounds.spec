Name: ultramarine-backgrounds
Version: 34
Release: 1
BuildArch: noarch
# details for the artworks' licenses can be seen in the COPYING file
License: CC-BY-SA and CC0
Summary: Ultramarine Linux backgrounds

# licensing information
Source0: COPYING

# CC0 artworks
Source100: blue-ocean.jpg
Source101: silhouette-of-mountain.jpg
Source102: by-ren-ran.jpg

# CC-BY-SA artworks
Source200: star-trails.jpg

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