# Bibblio Recommendations

![Bibblio](https://cdn-images-1.medium.com/fit/c/200/200/0*Qw1J3jqJtMhsU9D-.png)

[Bibblio’s](http://www.bibblio.org/) content recommendation system increases engagement on your pages by suggesting other relevant content from across your site.

No dubious ads. No spam. No fake news. Just your content showcased in smart recommendation modules and thoughtfully positioned on your pages to improve their discovery.

Visit [Bibblio API Documentation](https://bibblio.docs.apiary.io/#) for more information.

```
Once enriched, the content you store with Bibblio can be discovered and explored
via meaningful recommendations and semantic connections between content items.
When retrieving recommendations you will need to specify the contentItemId
for the content item you would like to base the recommendations upon. We will
provide a list of other content items that are related, as well as a list of
reasons for each recommendation.
```

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

## Setup
Add to ```XBLOCK_SETTINGS``` inside ```lms.env.json``` the following
```
"XBLOCK_SETTINGS": {
        "bibblio": {
            "recommendation_key": "xxxxxxxx"
        }
    }
```

Then add your ```xblock``` on ```Advanced Settings``` of the course as ```bibblio``` in ```Advanced Module List```

## Notes
To use the feature of auto ingesting content we need to add a customUniqueIdenfier when
creating a new Content Item in Bibblio.
