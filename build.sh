#!/bin/bash
bundle install
bundle exec vendor/bundle/ruby/3.1.0/bin/jekyll build
cp _site/* ../output/ -R
