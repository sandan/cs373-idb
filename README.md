cs373-idb
=========

Group Name:       The Austinites
Group Members:    Stephen Ridings, Mark Sandan, Jesus Hernandez, Carlos Rodriguez, Sheeyla Garcia, Kyle Nicola
Proposed project: Austin City Limits (ACL)
Example Pages:    Artists, Sponsors and Events



There will be three phases.

Phase I Features:
-   Collect data on ten artists, ten sponsors, and all the events (7).
    Identify common attributes of the data and insure that every data item has a value for that attribute.
    Make sure to collect enough information to make it a rich experience.
-   Create a RESTful API using Apiary. Log into Apiary with your GitHub credentials and connect Apiary to your private repos.
    Think carefully about the types and format of the requests and responses, primary keys, foreign key constraints, and validations.
-   Create a set of Django models to represent the data and that corresponds to the API.
    Think carefully about the types of the models and about the many-to-many relationships between artists, sponsors, and events.
-   Create a set of unit tests of the Django models.
-   Create a static HTML page for three unique artists, three unique sponsors, and three unique events that displays all of the data collected.
    The pages must be served by Django on PythonAnywhere using Django templates to embed the static content into HTML.
    Design the splash page well. Design the navigation well.
    Use Twitter Bootstrap to present information in an organized way. Make sure to embed the different media. Make sure that everything that can be linkable is.
    Create a responsive design that looks good on mobile devices.
-   Write an initial technical report.
    The audience comprises other software developers, as opposed to users.
    For this phase make it at least 10 pages.
    Document the RESTful API and the Django models well.
    Format the report clearly, attractively, and consistently, using good headers, figures, and grammar.



The pages MUST contain the following:

Splash Page Features:
- the group name
- the group members
- a way to navigate to the nine static HTML pages

Artist Page Features:
- name, members, genre, label(s), origin, date and time, citations, external links
* small artist description (iTunes, Spotify, Wikipedia, etc.)
- embedded images (e.g. Bing, Flickr, Google)
- embedded videos (e.g. Youtube, Google, Vimeo)
- embedded maps (e.g. Google Maps)
- embedded social network feeds (e.g. Facebook, Twitter)
- sponsors
- events

Sponsor Page Features:
- name, business type, location, history, CEO, contact info, citations, external links
- embedded images, logo (e.g. Bing, Flickr, Google)
- embedded videos, ad (e.g. Youtube, Google, Vimeo)
- embedded maps, HQ (e.g. Google Maps)
- embedded social network feeds (e.g. Facebook, Twitter)
- artists
- events

Event Page Features:
- name, kind, location, citations, external links
- embedded images (e.g. Bing, Flickr, Google)
- embedded videos (e.g. Youtube, Google, Vimeo)
- embedded maps (e.g. Google Maps, location during festival)
- embedded social network feeds (e.g. Facebook, Twitter)
- artists
- sponsors



The technical report MUST contain the following:
- Title:        The group name, the group members.
- Introduction: What is the problem? What are the use cases?
- Design:       RESTful API, Django models.
- Tests:        unit tests of the Django models.
- Other:        Proof-read your report. Get another group to read it. Read it aloud. 
                Create diagrams with captions.
                Create sections and subsections effectively.



Groups:
- Pick a project leader for the group. A group member can only be project leader once.
- Once the grader has graded the project, that will be the project grade.
- The project leader will always receive the project grade.
- The project leader can add or subtract up to 10 points to or from any member of the group in exchange for
  adding or subtracting the same amount of points from the other member(s) of the group.
- For example, the leader could add 10 points to person A, and subtract 5 points from person B and person C.
- The leader will report those adjustments in the Google Form.



Requirements:
-   Estimate time to completion.
-   Create a public Git repository at GitHub, named cs373-idb.
-   Add these requirements to the issue tracker at GitHub, at least 10 issues.
    Add at least 10 more issues, one for each bug or feature, both open and closed with a good description and a label.
-   Clone your public code repo onto your local directory.
-   Make at least 5 commits, one for each bug or feature.
    If you cannot describe your changes in a sentence, you are not committing often enough.
    Make meaningful commit messages identifying the corresponding issue in the issue tracker (see here).
-   Write unit tests in tests.py that test corner cases and failure cases until you have an average of 3 tests for each Django model     call, confirm the expected failures, and add, commit, and push to the public code repo.
-   Implement and debug the simplest possible solution with assertions that check pre-conditions, post-conditions, argument validity,     and return-value validity, until all tests pass, and add, commit, and push to the private code repo.
-   Run pydoc on models.py, which will create models.html, that then documents the interfaces to your models.
    Create inline comments if you need to explain the why of a particular implementation.
    Use a consistent coding convention with good variable names, good indentation, blank lines, and blank spaces.
-   Create a log of your commits in IDB.log.
-   Obtain the git SHA with git rev-parse HEAD
-   Fill in the Google Form.
-   It is your responsibility to protect your code from the rest of the students in the class. If your code gets out, you are as         guilty as the recipient of academic dishonesty.



Requirements for getting a non-zero grade.
[ 5 pts] GitHub public repo with a log of the commits.
[ 5 pts] GitHub issue tracker with issues from requirements and more.
[10 pts] RESTful API at Apiary.
[10 pts] Set of Django models.
[10 pts] Website using Django and Twitter Bootstrap at PythonAnywhere.
[10 pts] Average of 3 unit tests per Django model call.
[ 5 pts] Pydoc documentation.
[10 pts] Technical Report, double-spaced, 10 pages.
[ 5 pts] Google Form with time estimate.



Files:
  apiary.apib
  models.html
  Report.pdf
  tests.out
  tests.py
