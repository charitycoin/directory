[![Build Status](https://magnum.travis-ci.com/adrianparsons/nonprofits.svg?token=PvC2GdudTSxt3yZ7aRn1&branch=master)](https://magnum.travis-ci.com/adrianparsons/nonprofits)

# charitycoin
Charitycoin is an open, crowd-sourced index of registered 501(c)(3) nonprofits and their associated Bitcoin addresses.

## structure
The ```orgs``` directory contains JSON files for nonprofits. Each nonprofit has its own file, and includes at a minimum the organizations EIN, its bitcoin address and a "confirmation" URL that contains the address. The confirmation URL is usually the a page on the organization's site.

For example, the file ```orgs/41-6031039.json```, describing the Apache Foundation, looks like this:

```
{
	"ein": "41-6031039",
	"name" : "APACHE FOUNDATION",
	"payments" : {
		"bitcoin" : {
			"address" : "1BtjAzWGLyAavUkbw3QsyzzNDKdtPXk95D",
			"confirmation" : "http://www.apache.org/foundation/contributing.html"
		}
	}
}
```

A test script, ```test.py``` scrapes the confirmation urls and looks for the associated address (or in the case of coinbase, the coinbase url). 

## contributing
There are 1.2 million nonprofits and this index contains a lot less than that. If you know of an organization that is not indexed, please open an issue, or even better, a pull request. Pull requests should pass the test in ```test.py```.

Second, I welcome any feedback, in the form of messages, issues, and the like. I think this is an important problem to solve, but I'm open to the idea that there are better ways to solve it.
