#!/usr/bin/env python
import os


def major_version():
    if not os.path.exists("/etc/redhat-release"):
        return -1
    with open("/etc/redhat-release") as fp:
        r = fp.read().strip()

    release = r.split("release")[1].strip()
    return release.split()[0].split(".")[0]


if __name__ == "__main__":
    print(major_version())
