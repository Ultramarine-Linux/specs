%define debug_package %{nil}

# codename data
%if %{fedora} == 34
%global release_name lazuli
%endif

%if %{fedora} == 35
%global release_name phingkan
%endif

%if %{fedora} == 36
%global is_rawhide 1
%global release_name aozora
%endif

# rawhide
%if %{is_rawhide}
%define releasever rawhide
%else
%define releasever %{fedora}
%endif


# product information
%define product_family Ultramarine Linux
#%%define variant_titlecase Server
#%%define variant_lowercase server

# distribution name and version
%define dist_name Ultramarine Linux
%define dist_code %{release_name}
%define dist_relver %{?fedora}
%define dist_version %{dist_relver}

Name: ultramarine-release
Version: %{dist_relver}
Release: 0.3
License: MIT
BuildArch: noarch
Summary: %{dist_name} release files

Provides: ultramarine-release = %{version}-%{release}
Provides: ultramarine-release-variant = %{version}-%{release}

# for Fedora compatibility
Provides: fedora-release = %{version}-%{release}
Provides: fedora-release-variant = %{version}-%{release}

Obsoletes: redhat-release
Provides: redhat-release
Provides: system-release
Provides: system-release(%{version})

Provides: fedora-release-nonproduct = %{version}
Obsoletes: fedora-release-nonproduct <= 23-0.3
Provides: fedora-release-standard = 22-0.8
Provides: fedora-release-standard < 22-0.8

## libdnf wants this
Provides: base-module(platform:f%{version})

Requires: ultramarine-release-common = %{version}-%{release}
Requires: ultramarine-repos(%{version})

BuildRequires: redhat-rpm-config > 121-1
BuildRequires: systemd-rpm-macros

# source files goes *here*:
Source0: LICENSE
Source1: Ultramarine-Legal-README.txt
###

%description
Ultramarine Linux release files such as various /etc/ files that define the release
and systemd preset files that determine which services are enabled by default.

%package common
Summary: Ultramarine Linux release files

Requires: ultramarine-release-variant = %{version}-%{release}
Requires: ultramarine-release-identity = %{version}-%{release}
Requires: ultramarine-repos(%{version})
Suggests: ultramarine-release

%if %{is_rawhide}
Provides: system-release(releasever) = %{releasever}
%endif

Conflicts: generic-release

%description common
Release files common to all Editions and Spins of Ultramarine Linux

# (basic)
%package identity-basic
Summary: Package providing the basic Ultramarine Linux identity

RemovePathPostfixes: .basic
Provides: ultramarine-release-identity = %{version}-%{release}
Conflicts: ultramarine-release-identity
# as always, Fedora compatibility
Provides: fedora-release-identity = %{version}-%{release}
Conflicts: fedora-release-identity

%description identity-basic
Provides the necessary files for a Ultramarine Linux installation that is not identifying
itself as a particular Edition or Spin.

# cyber
%package cyber
Summary: Base package for Ultramarine Linux Cyber-specific default configurations

RemovePathPostfixes: .cyber
Provides: ultramarine-release = %{version}-%{release}
Provides: ultramarine-release-variant = %{version}-%{release}
Provides: system-release
Provides: system-release(%{version})
Provides: base-module(platform:f%{version})
Requires: ultramarine-release-common = %{version}-%{release}
Requires: ultramarine-repos-cyber
# as always, Fedora compatibility
Provides: fedora-release = %{version}-%{release}
Provides: fedora-release-variant = %{version}-%{release}

Recommends: ultramarine-release-identity-cyber

%description cyber
Provides a base package for Ultramarine Linux Cyber-specific configuration files to
depend on as well as Cyber Desktop system defaults.

## identity
%package identity-cyber
Summary: Package providing the identity for Ultramarine Linux Cyber

RemovePathPostfixes: .cyber
Provides: ultramarine-release-identity = %{version}-%{release}
Conflicts: ultramarine-release-identity
# as always, Fedora compatibility
Provides: fedora-release-identity = %{version}-%{release}
Conflicts: fedora-release-identity

%description identity-cyber
Provides the necessary files for an Ultramarine Linux installation that is identifying
itself as Ultramarine Linux Cyber.

# cutefish
%package cutefish
Summary: Base package for Ultramarine Linux Cutefish-specific default configurations

RemovePathPostfixes: .cutefish
Provides: ultramarine-release = %{version}-%{release}
Provides: ultramarine-release-variant = %{version}-%{release}
Provides: system-release
Provides: system-release(%{version})
Provides: base-module(platform:f%{version})
Requires: ultramarine-release-common = %{version}-%{release}
Requires: ultramarine-repos-cutefish
# as always, Fedora compatibility
Provides: fedora-release = %{version}-%{release}
Provides: fedora-release-variant = %{version}-%{release}

Recommends: ultramarine-release-identity-cutefish

%description cutefish
Provides a base package for Ultramarine Linux Cutefish-specific configuration files to
depend on as well as Cutefish Desktop system defaults.

## identity
%package identity-cutefish
Summary: Package providing the identity for Ultramarine Linux Cutefish

RemovePathPostfixes: .cutefish
Provides: ultramarine-release-identity = %{version}-%{release}
Conflicts: ultramarine-release-identity
# as always, Fedora compatibility
Provides: fedora-release-identity = %{version}-%{release}
Conflicts: fedora-release-identity

%description identity-cutefish
Provides the necessary files for an Ultramarine Linux installation that is identifying
itself as Ultramarine Linux Cutefish.

# budgie
%package budgie
Summary: Base package for Ultramarine Linux Budgie-specific default configurations

RemovePathPostfixes: .budgie
Provides: ultramarine-release = %{version}-%{release}
Provides: ultramarine-release-variant = %{version}-%{release}
Provides: system-release
Provides: system-release(%{version})
Provides: base-module(platform:f%{version})
Requires: ultramarine-release-common = %{version}-%{release}
Requires: ultramarine-repos-budgie
# as always, Fedora compatibility
Provides: fedora-release = %{version}-%{release}
Provides: fedora-release-variant = %{version}-%{release}

Recommends: ultramarine-release-identity-budgie

%description budgie
Provides a base package for Ultramarine Linux Budgie-specific configuration files to
depend on as well as Budgie Desktop system defaults.

## identity
%package identity-budgie
Summary: Package providing the identity for Ultramarine Linux Budgie

RemovePathPostfixes: .budgie
Provides: ultramarine-release-identity = %{version}-%{release}
Conflicts: ultramarine-release-identity
# as always, Fedora compatibility
Provides: fedora-release-identity = %{version}-%{release}
Conflicts: fedora-release-identity

%description identity-budgie
Provides the necessary files for an Ultramarine Linux installation that is identifying
itself as Ultramarine Linux Budgie.

%prep
# sed -i 's|@@VERSION@@|%%{version}|g' <readme file>

%build

%install
install -d %{buildroot}%{_prefix}/lib
echo "Ultramarine Linux release %{version} (%{dist_code})" > %{buildroot}%{_prefix}/lib/ultramarine-release
echo "cpe:/o:ultramarine:ultramarinelinux:%{version}" > %{buildroot}%{_prefix}/lib/system-release-cpe
# as always, Fedora compatibility
pushd %{buildroot}%{_prefix}/lib
ln -nvfs ultramarine-release %{buildroot}%{_prefix}/lib/fedora-release

# symlink the release identifiers
install -d %{buildroot}%{_sysconfdir}
ln -s ../usr/lib/ultramarine-release %{buildroot}%{_sysconfdir}/ultramarine-release
ln -s ../usr/lib/fedora-release %{buildroot}%{_sysconfdir}/fedora-release
ln -s ../usr/lib/system-release-cpe %{buildroot}%{_sysconfdir}/system-release-cpe
ln -s fedora-release %{buildroot}%{_sysconfdir}/redhat-release
ln -s fedora-release %{buildroot}%{_sysconfdir}/system-release

# create the common os-release file
%{lua:
  function starts_with(str, start)
   return str:sub(1, #start) == start
  end
}
%define starts_with(str,prefix) (%{expand:%%{lua:print(starts_with(%1, %2) and "1" or "0")}})
%if %{starts_with "a%{release}" "a0"}
  %global prerelease \ Prerelease
%endif
 
cat << EOF >> os-release
NAME="Ultramarine Linux"
VERSION="%{dist_version} (%{release_name}%{?prerelease})"
ID=ultramarine
ID_LIKE=fedora
VERSION_ID=%{dist_version}
VERSION_CODENAME="%{release_name}"
PLATFORM_ID="platform:f%{dist_version}"
PRETTY_NAME="Ultramarine Linux %{dist_version} (%{release_name}%{?prerelease})"
ANSI_COLOR="0;38;2;60;110;180"
LOGO=ultramarine-logo
CPE_NAME="cpe:/o:ultramarine:ultramarinelinux:%{dist_version}"
HOME_URL="https://example.org/to-be-added/homeurl"
DOCUMENTATION_URL="https://example.org/to-be-added/documentation-for-%{dist_version}"
SUPPORT_URL="https://example.org/to-be-added/supporturl"
BUG_REPORT_URL="https://example.org/to-be-added/bugtracker"
PRIVACY_POLICY_URL="https://example.org/to-be-added/privacypolicies"
EOF
 
# create the common /etc/issue
echo "\S" > %{buildroot}%{_prefix}/lib/issue
echo "Kernel \r on an \m (\l)" >> %{buildroot}%{_prefix}/lib/issue
echo >> %{buildroot}%{_prefix}/lib/issue
ln -s ../usr/lib/issue %{buildroot}%{_sysconfdir}/issue
 
# create /etc/issue.net
echo "\S" > %{buildroot}%{_prefix}/lib/issue.net
echo "Kernel \r on an \m (\l)" >> %{buildroot}%{_prefix}/lib/issue.net
ln -s ../usr/lib/issue.net %{buildroot}%{_sysconfdir}/issue.net
 
# create /etc/issue.d
mkdir -p %{buildroot}%{_sysconfdir}/issue.d
 
mkdir -p %{buildroot}%{_swidtagdir}

# cyber
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.cyber
echo "VARIANT=\"Cyber\"" >> %{buildroot}%{_prefix}/lib/os-release.cyber
echo "VARIANT_ID=cyber" >> %{buildroot}%{_prefix}/lib/os-release.cyber
sed -i -e "s|(%{release_name}%{?prerelease})|(%{release_name}%{?prerelease}) Cyber|g" %{buildroot}%{_prefix}/lib/os-release.cyber
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Cyber/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.cyber

# cutefish
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.cutefish
echo "VARIANT=\"Cutefish\"" >> %{buildroot}%{_prefix}/lib/os-release.cutefish
echo "VARIANT_ID=cutefish" >> %{buildroot}%{_prefix}/lib/os-release.cutefish
sed -i -e "s|(%{release_name}%{?prerelease})|(%{release_name}%{?prerelease}) Cutefish|g" %{buildroot}%{_prefix}/lib/os-release.cutefish
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Cutefish/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.cutefish

# budgie
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.budgie
echo "VARIANT=\"Budgie\"" >> %{buildroot}%{_prefix}/lib/os-release.budgie
echo "VARIANT_ID=budgie" >> %{buildroot}%{_prefix}/lib/os-release.budgie
sed -i -e "s|(%{release_name}%{?prerelease})|(%{release_name}%{?prerelease}) Budgie|g" %{buildroot}%{_prefix}/lib/os-release.budgie
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Budgie/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.budgie

# symlink /etc/os-release
ln -s ../usr/lib/os-release %{buildroot}%{_sysconfdir}/os-release

# set up the dist tag macros
install -d -m 755 %{buildroot}%{_rpmconfigdir}/macros.d
cat >> %{buildroot}%{_rpmconfigdir}/macros.d/macros.dist << EOF
# dist macros.
 
%%__bootstrap         ~bootstrap
%if 0%{?eln}
%%rhel              %{rhel_dist_version}
%%el%{rhel_dist_version}                1
# Although eln is set in koji tags, we put it in the macros.dist file for local and mock builds.
%%eln              %{eln}
%%dist                %%{!?distprefix0:%%{?distprefix}}%%{expand:%%{lua:for i=0,9999 do print("%%{?distprefix" .. i .."}") end}}.el%%{eln}%%{?with_bootstrap:%{__bootstrap}}
%else
%%fedora              %{dist_version}
%%fc%{dist_version}                1
%%dist                %%{!?distprefix0:%%{?distprefix}}%%{expand:%%{lua:for i=0,9999 do print("%%{?distprefix" .. i .."}") end}}.fc%%{fedora}%%{?with_bootstrap:%{__bootstrap}}
%endif
EOF

# install licenses
mkdir -p licenses
install -pm 0644 %{SOURCE1} licenses/LICENSE
install -pm 0644 %{SOURCE2} licenses/Fedora-Legal-README.txt
 
# Default system wide
install -Dm0644 %{SOURCE10} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE11} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE12} -t %{buildroot}%{_prefix}/lib/systemd/user-preset/
# The same file is installed in two places with identical contents
install -Dm0644 %{SOURCE13} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE13} -t %{buildroot}%{_prefix}/lib/systemd/user-preset/
 
# Create distro-level SWID tag file
install -d %{buildroot}%{_swidtagdir}
sed -e "s#\$version#%{bug_version}#g" -e 's/<!--.*-->//;/^$/d' %{SOURCE19} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-%{bug_version}.swidtag
install -d %{buildroot}%{_sysconfdir}/swid/swidtags.d
ln -s %{_swidtagdir} %{buildroot}%{_sysconfdir}/swid/swidtags.d/fedoraproject.org

### TODO: FINISH