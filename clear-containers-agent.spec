Name     : clear-containers-agent
Version  : 7c3836846c8a65c42be775c30b0e4f3f1515dddd
Release  : 7
URL      : https://github.com/clearcontainers/agent/archive/master/7c3836846c8a65c42be775c30b0e4f3f1515dddd.tar.gz
Source0  : https://github.com/clearcontainers/agent/archive/master/7c3836846c8a65c42be775c30b0e4f3f1515dddd.tar.gz
Summary  : Clear Containers Agent
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause MIT
BuildRequires : go
BuildRequires : pkgconfig(systemd)

%description
Clear Containers Agent.

%prep
%setup -q -n agent-master

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export GOPATH="${PWD}/gopath/"
mkdir -p "${GOPATH}/src/github.com/clearcontainers/"
ln -sf "${PWD}" "${GOPATH}/src/github.com/clearcontainers/agent"
cd "${GOPATH}/src/github.com/clearcontainers/agent"
make


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/cc-agent
/usr/lib/systemd/system/clear-containers.service
/usr/lib/systemd/system/clear-containers.target
