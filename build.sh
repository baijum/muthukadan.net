#!/bin/bash
bundle install --path vendor/bundle
bundle exec vendor/bundle/ruby/2.3.0/bin/jekyll build
