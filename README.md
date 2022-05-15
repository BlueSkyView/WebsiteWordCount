## Dependencies

**Requests** - used for accessing an external website

To install Requests, simply run this simple command in your terminal of choice:
~~~
$ python -m pip install requests
~~~


**BeautifulSoup4** - Used for parsing the text that is retrieved from a given website

To install, simply run
~~~
pip install beautifulsoup4
~~~

The user should have Python 3.9+ installed on their computer in order to run everything included here.


## Layout

The user should be running everything off of main.py, which will ask the user to enter in a website.  After entering the
website, it will attempt to connect to the website, and throw an error if there are connection issues (invalid website, or 
it returns a status of anything other than 200.)  If thi succeeds, it will give the user the ability to ask to return the
dictionary in sorted order based on the counts of the words found on the webpage.



## Assumptions and Thought Process/Additional Info

Python was chosen as there exists some very useful libraries and tools for parsing 
through websites, such as BeautifulSoup.  Additionally, for the purposes of this exercise, it's a language that is
pretty quick to develop something in a short period of time, and is a language that I'm familiar with.  Have listed
some additional assumptions and thoughts below

1) For the purposes of this exercise, I ran it on a local machine, and am assuming that this will be the case for the testing of if as well.  If this were to be run on a web application, the code could be deployed onto a remote machine/server somewhere, and there would also need to be some sort of web UI or other element to make the request to the remote machine to execute the code.
2) I am assuming for the purposes of the exercise that the goal of this is to pull primarily visible text.  IE we do not want non visible text pulled into the results that are returned
3) I am assuming that we do not care about the case of the word, and we do not need to normalize for if a word is plural or not.  The words "The" and "the" will be counted as effectively the same word.  On the other end of the spectrum, we would count "dog" and "dogs" as two independent words as one is plural and one is singular.
4) This will only be run on English language websites.  Given the use of a space as a delimiter, this would not work for certain other langauges (Chinese, etc.)
5) This will only be used for websites which are available without requiring a login.  If a website request requires a login, that functionality is not supported by this at this point in time, although it is something that could be added in.
6) This will only be used for websites where the entire text from the website/thing that we are retrieving can be fit in memory.  If we wanted to extend this to also account for larger pieces of data that could not fit in memory, we would need to have a way of streaming in the data, or otherwise chunking it into smaller pieces that could fit within memory.
7) I've decided to give the user the ability to return a dictionary in either ascending or descending order based on the frequency of the words that appear.  This could easily be updated to also give the user other options, such as ordering it alphabetically based on the key of the dictionary returned.  I've decided to allow the user to enter non-valid input here, and simply return the dictionary as initiially constructed, as opposed to asking the user to enter in a valid response.



In general, the primary bottlenecks in this process are 1) connecting to the website and grabbing data, depending on the size
of the page and 2) going through the text and getting the counts.  Due to this, I've included a dictionary that will store the
prior results of going to a web page.  This is going on the assumption that a user may call the program on the same webpage multiple 
times within a given session.  If this were to be used in a more realistic scenario, we could potentially want to 
take a look at when the page was last visited (websites don't generally change that often, depending on the site.  A main page like www.bbc.com/news 
will change frequently, but a specific article on the BBC News website would be relatively static over time)  Additionally, in a more
realistic scenario, we wouldn't simply store previously accessed results on a local machine, or simply as a variable in the class, but we could store it either in database,
or store very frequently accesssed websites in a cache to quickly return the results to a given user.  For storing the original text in the 
lookup for text results -> dictionary frequency, I could have also just calculate a hash based on the raw text and use that as the lookup
in the dictionary, which would save storage space as well.  However, writing to a database would also add in some additional
dependencies, like network dependencies, ensuring the db is up and operational, etc. Some of these could be mitigated by having
a set up that would help reduce this (duplicate databases, having a main one, and backup ones, Read vs write db, etc.)




## Testing
I've included unit tests for the functions in the document_parser.py file, testing for a variety of test cases.  For testing the website_fetcher.py file, I have not included any
testing, but if I had additional time, I would look to test this out as well.  For testing this, I could run tests using a mock request framework, which would call upon
an HTML file that could be stored locally.  The advantage of this is that it would take out the networking component in the testing methodology (internet issues, or issues with the test website would not 
mean that I cannot test the core functionality that is involved.) and generally allow me to test things in a more consistent way and remove variables to account for.

For testing, a good test case could be "https://techcrunch.com/2022/05/14/this-week-in-apps-google-i-o-wraps-a-new-arcore-api-twitter-deal-drama/", as it has a lot of text, and also has photos on the website and is fairly representative of how an average website may look like on the internet today.  There is also a variety of different punctuation types (?,!,., etc.) and has some ALL CAPS words and normal caps for words at the start of sentences.  This allows it to test that functionality within the program to handle these cases. 