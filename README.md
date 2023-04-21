# basic_url_shortener
URL Shortener Django Project

This is a Django-based web application that allows you to shorten URLs.
When a URL is submitted, the application reduces the URL to a short code that can be used to access the original URL.

Prerequisites

This project requires Python 3.7 or higher and Django 3.0 or higher.

Usage

To use the URL shortener, enter the URL you want to shorten in the form on the home page and submit it. The application will generate a short code 
for the URL and store it in the database. The short code can be used to access the original URL.

The model/schema used in this application is:

ShortURL

    long_url
    shortened

The application uses Django's shortcut redirect function to redirect to the original URL when a short code is entered in the address bar.


# This project was made for the needs of this exercise during the DCI bootkamp
Design a URL shortener in Django. When a URL is submitted, reduce the url to something that is short.

One approach we can take is this:
Given a url like https://www.spiegel.de/politik/deutschland/ampelkoalition-streitet-ueber-aussenpolit[…]gruenen-und-das-f-wort-a-2d3155ad-52f1-4bd3-92fd-9ffbaf78040b should be stored in the database as: https://localhost:8000/url/abcd432143 the abcd432143 will be a randomly generated string.
The model/schema could look like this:
ShortURL

- long_url
- shortened
Django’s shortcut redirect function can be used to visit an external website. In your django test, confirm that a redirect in deed took place.
If you include helper or utility functions in Python, write unit tests for them too.
