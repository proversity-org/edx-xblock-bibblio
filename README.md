# Bibblio Recommendations

Visit http://bibblio.org for more information.

## Installation

```
$ sudo su edxapp -s /bin/bash
$ cd ~ && source edxapp_env
$ cd /edx/app/edxapp/edx-platform
$ pip install -U -e git+https://github.com/proversity-org/edx-xblock-bibblio#egg=edx-xblock-bibblio
$ exit && /edx/bin/supervisorctl restart edxapp:
```

or add to the end of `edx-platform/requirements/edx/github.txt`

```
git+https://github.com/proversity-org/edx-xblock-bibblio#egg=edx-xblock-bibblio
```