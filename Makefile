RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

all:
	mkdir -p build
	${RPMBUILD} -ba observatory-dome-server.spec
	${RPMBUILD} -ba observatory-dome-client.spec
	${RPMBUILD} -ba python3-warwick-observatory-dome.spec
	${RPMBUILD} -ba onemetre-dome-data.spec
	${RPMBUILD} -ba clasp-dome-data.spec
	${RPMBUILD} -ba superwasp-dome-data.spec
	mv build/noarch/*.rpm .
	rm -rf build
