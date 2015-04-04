[![Build Status](https://travis-ci.org/charity-coin/directory.svg?branch=master)](https://travis-ci.org/charity-coin/directory)

# charitycoin
Charitycoin is an open, crowd-sourced index of registered 501(c)(3) nonprofits and their Bitcoin addresses.

[View the current list of nonprofits](https://raw.githubusercontent.com/charitycoin/directory/master/dist/all.json) in the ```dist``` directory.

## structure
The ```orgs``` directory contains JSON files for nonprofits. Each nonprofit has its own file, and includes at a minimum the organization's EIN, its bitcoin address and a "confirmation" URL that contains the address. The confirmation URL is usually a page on the organization's site.

For example, the ```.json``` file describing the Apache Foundation, looks like this:

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

## verification
A simple python script, ```test.py``` grabs the markup from the url listed in the "confirmation" field in each entry. The script checks that the address is present in the markup. For the moment, I manually check that the organization's domain name matches the one listed on [guidestar](http://www.guidestar.org/). TravisCI runs the script. If there's a missmatch, the build will be labeled as "failing". There may be better ways to do this.

## contributing
There are 1.2 million nonprofits and this index contains a lot less than that. If you know of an organization that accepts bitcion but is not indexed, please open an issue or a pull request.

Also, I welcome any feedback, in the form of messages, issues, and the like. I think this is an important problem to solve, but I'm open to the idea that there are better ways to solve it.

## thanks
Special thanks to the [Machinecoin Project](http://www.machinecoin.org/)!
