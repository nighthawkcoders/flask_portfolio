## [Flask Portfolio Starter](https://nighthawkcodingsociety.com/projectsearch/details/Flask%20Portfolio%20Starter)
Runtime link: https://portfolio.nighthawkcodingsociety.com/
### Idea
Starter code should be fun and practical.

#### Week 0
|Contributor| Links to Commits  |
|---|---|
| Sanjay  |  [About Page](https://github.com/SimonBrunzell/flask_portfolio/commit/35bd15cff37a527274e25a305ca8c6ccde16d00b)<br/> [About Page PT 2](https://github.com/SimonBrunzell/flask_portfolio/commit/e900e68e8917848690659b15b8aec711a6f68938#diff-9593e34db94aca426d593f1f46c03f1c73307157df159e66ca8e092c1aac655f) <br/> [About Page API](https://github.com/SimonBrunzell/flask_portfolio/commit/e900e68e8917848690659b15b8aec711a6f68938#diff-b10564ab7d2c520cdd0243874879fb0a782862c3c902ab535faabe57d5a505e1) <br/> [Base.html Changes](https://github.com/SimonBrunzell/flask_portfolio/commit/e900e68e8917848690659b15b8aec711a6f68938#diff-76445280ac812dc6e42103e56c567a6b21eb2fc8f5d5c87554cf985da0a6a9ab)|
| Evan  |   |
| Leah  |  [started work on a sidebar](https://github.com/SimonBrunzell/flask_portfolio/commit/2944fbaf4efe0845bd2a22f301329bd0fd3a0192) <br/> [made the sidebar on every page](https://github.com/SimonBrunzell/flask_portfolio/commit/6cce5e051f31bc74651bc102ae69d981a1d3c099) <br/> [sidebar margin doesn't cover body](https://github.com/SimonBrunzell/flask_portfolio/commit/5c31638a550e0ca91232962d9c1b1e5145e84b96) <br/> [editing sidebar for scrolling](https://github.com/SimonBrunzell/flask_portfolio/commit/d2d7547e5ea74d2e4e10f70925e46058fd3182ca) <br/> [starting on my about page](https://github.com/SimonBrunzell/flask_portfolio/commit/062eb7af7c5d4fc19ff56ce826df7073a2d6c06e) <br/> [putting the picture onto my about page](https://github.com/SimonBrunzell/flask_portfolio/commit/1b816cd2b4bdd27922ccde1e59fbb80b923687e0) |
| Simon  |   |
| Vunsh  |   |


### Visual thoughts
#### Organize with Bootstrap menu 
#### Add some color and fun through VANTA Visuals (birds, halo, solar, net)
#### Show some practical and fun links (hrefs) like Twitter, Git, Youtube
#### Show project specific links (hrefs) per page

### Implementation progress (August 13th, 2021)
#### Project entry point is main.py, this enables Flask Web App and provides capability to renders templates (HTML files)
#### The main.py is the  Web Server Gateway Interface, essentially it contains a HTTP route and HTML file relationship.  The Python code constructs WSGI relationships for index, kangaroos, walruses, and hawkers.
#### The project structure contains many directories and files.  The template directory (containing html files) and static directory (containing js files) are common standards for HTML coding.  Static files can be pictures and videos, in this project they are mostly javascript backgrounds.
#### WSGI templates: index.html, kangaroos.html, ... are aligned with routes in main.py.
#### Other templates support WSGI templates.  The base.html template contains common Head, Style, Body, Script definitions.  WSGI templates often "include" or "extend" these templates.  This is a way to reuse code.
#### The VANTA javascript statics (backgrounds) are shown and defaulted in base.html (birds), but are block replaced as needed in other templates (solar, net, ...)
#### The Bootstrap Navbar code is in navbar.html. The base.html code includes navbar.html.  The WSGI html files extend base.html files.  This is a process of management and correlation to optimize code management.  For instance, if the menu changes discovery of navbar.html is easy, one change reflects on all WSGI html files. 
#### Jinja2 variables usage is to isolate data and allow redefinitions of attributes in templates.  Observe "{% set variable = %}" syntax for definition and "{{ variable }}" for reference.
#### The base.html uses combination of Bootstrap grid styling and custom CSS styling.  Grid styling in observe with the "<Col-3>" markers.  A Bootstrap Grid has a width of 12, thus four "Col-3" markers could fit on a Grid row.
#### A key purpose of this project is to embed links to other content.  The "href=" definition embeds hyperlinks into the rendered HTML.  The base.html file shows usage of "href={{github}}", the "{{github}}" is a Jinja2 variable.  Jinja2 variables are pre-processed by Python, a variable swap with value, before being sent to the browser.

### IDE management (things that happened beyond plan)
#### Recall on ".gitignore" solution to the pains of temporary files.  Start a ".gitignore" and avoid promoting temporary files to Git, for instance IDE xml files.
#### A project needs to establish a "requirements.txt" to keep track of Python packages used by the project.  This help in other IDEs and Deployment.  IntelliJ has menu Tool -> Sync Python Requirements to start file. 
