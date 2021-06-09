srpm:
	dnf install -y automake autoconf wget
	./autogen.sh
	make dist
	rpmbuild -bs $(spec) --define '_topdir .copr' --define '_sourcedir .'
	mv .copr/SRPMS/insights-client-*.src.rpm $(outdir)
