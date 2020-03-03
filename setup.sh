#!/bin/bash

apt update && apt upgrade -y
apt install -y curl wget libpq-dev python3-dev gem ruby ruby-dev build-essential libssl-dev libffi-dev python-dev python-virtualenv python-pip git redis-server libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev tcl8.6-dev tk8.6-dev python-tk

gem install sass

apt install wkhtmltopdf
