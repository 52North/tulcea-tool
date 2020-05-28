#!/bin/sh

# Exit on error
set -e

# Dump wq configuration object to file
db/manage.py dump_config --format amd > app/js/data/config.js

# (Re-)generate templates for all registered models
wq maketemplates \
     --django-dir db \
     --input-dir master_templates \
     --template-dir templates

# Build javascript with wq.app
cd app;
wq icons;
wq build $1;

# Force important files through any unwanted server caching
cd ../;
sed -i "s/TulceaTool.js/TulceaTool.js?v="$1"/" htdocs-build/TulceaTool.appcache
sed -i "s/TulceaTool.css/TulceaTool.css?v="$1"/" htdocs-build/TulceaTool.appcache

# Preserve Django's static files (e.g. admin)
if [ -d htdocs/static ]; then
    cp -a htdocs/static htdocs-build/static
fi;

# Replace existing htdocs with new version
rm -rf htdocs;
mv -i htdocs-build/ htdocs;

# Restart Django
touch db/TulceaTool/wsgi.py

# Build PhoneGap application
cd app;
wq phonegap $1
cd ../;
