---
layout: default
title: Baiju Muthukadan
---

### Recent Blog Posts

<ul class="posts">
  {% for post in site.posts limit:7 %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

### Other Sites & Pages

<ul class="posts">
  <li><a href="http://baijum.blogspot.in">My old blog:</a> My old blog in Blogger.</li>
  <li><a href="http://golang.muthukadan.net">Golang book:</a> A Comprehensive Guide to Go Programming.</li>
  <li><a href="http://muthukadan.net/docs/zca.html">ZCA book:</a> A Comprehensive Guide to Zope Component Architecture.</li>
  <li><a href="http://selenium-python.readthedocs.org">Selenium with Python:</a> Using Selenium Webdriver with Python.</li>
</ul>
