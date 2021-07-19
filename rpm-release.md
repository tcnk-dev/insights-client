# Releasing The Insights Client RPM
## 1. Creating Source Tarball Release
To create the insights-client source tarball, clone the repository and run the following command:
```
./autogen.sh; make dist
```

This will automatically download the latest `insights-core` egg, and create a tar.gz archive suitable for creating an RPM.

The generated tar.gz should also be uploaded to Github as a release.

To tag for a release, use the current value of the VERSION file and tag the current commit. Then push tags to origin (Gitlab).
```
git tag $(cat VERSION)
git push origin master --tags
```
You can now draft a release on Github with this tag. Attach the generated tar.gz to the release.

After pushing the tags, increment the VERSION file as needed (usually, incrementing the release by 1). Then commit the new VERSION.
```
git checkout -b release-bump
awk -F . '{printf("%d.%d.%d\n", $1, $2, $3+1) > "VERSION";}' VERSION
git add VERSION; git commit -m "post-release version bump"; git push origin release-bump
```
Open a new pull request on Gitlab to commit the new VERSION.

## 2. Bugzilla Approvals
## 3. Pushing to Brew
## 4. Errata Process