CUR_VERSION := $(shell cat VERSION)
NEXT_VERSION := $(shell echo $(CUR_VERSION) | awk -F. '{printf("%d.%d.%d", $$1, $$2, $$3+1)}')

srpm:
	dnf install -y automake autoconf wget
	echo $(NEXT_VERSION) > VERSION
	./autogen.sh
	echo $(CUR_VERSION) > VERSION
	make dist
	rpmbuild -bs $(spec) --define '_topdir .copr' --define '_sourcedir .' --define 'insights_client_version $(NEXT_VERSION)'
	mv .copr/SRPMS/insights-client-*.src.rpm $(outdir)
