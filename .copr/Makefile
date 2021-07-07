CUR_VERSION := $(shell cat VERSION)
NEXT_VERSION := $(shell echo $(CUR_VERSION) | awk -F. '{printf("%d.%d.%d", $$1, $$2, $$3+1)}')
COMMIT_HASH := $(shell cat .git/HEAD | awk '{print ".git/"$$2}' | xargs cat | cut -c -7)

srpm:
	dnf install -y automake autoconf wget
	echo $(NEXT_VERSION) > VERSION
	./autogen.sh
	echo $(CUR_VERSION) > VERSION
	make dist
	sed -e "s/@PACKAGE_VERSION@/$(NEXT_VERSION)/g" -e "s/@COMMIT_HASH@/$(COMMIT_HASH)/g" $(spec).in > $(spec)
	rpmbuild -bs $(spec) --define '_topdir .copr' --define '_sourcedir .'
	mv .copr/SRPMS/insights-client-*.src.rpm $(outdir)
