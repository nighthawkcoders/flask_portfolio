## [Flask Portfolio Starter](https://nighthawkcodingsociety.com/projectsearch/details/Flask%20Portfolio%20Starter)
Runtime link: https://portfolio.nighthawkcodingsociety.com/
### Idea
Starter code show be fun and practical.
### Visual thoughts
#### - [ ] Organize with Bootstrap menu 
#### - [ ] Add some color and fun through VANTA Visuals (birds, halo, solar, net)
#### Show some practical and fun links (hrefs) like Twitter, Git, Youtube
#### Show project specific links (hrefs) per page
### Technicals used
#### Project contains main.py to enable flask and renders templates
#### Multiple routes in main.py (index, kangaroos, walruses, hawkers)
#### Project contains template and static directories for HTML coding
#### Individual templates: index.html, kangaroos.html, ... are aligned with routes in website
#### Individual templates extend base.html for common Head, Style, Body, Script "layout"
#### VANTA statics (backgrounds) are defaulted in base.html, but are block replaced as needed in templates
#### Bootstrap Navbar isolation (navbar.html) allows easy correlation to main.py route changes
#### Jinja2 variables usage is to isolate data and allow redefinitions with templates
#### The base.html uses combination of Bootstrap grid styling and custom CSS styling
#### Main purpose of project is to embed href links to access project specifics
### Other IDE management things that pop early
#### Learning about .gitignore so we don't promote temporary files to Git, for instance IntelliJ xml files
#### Start understand requirements.txt and use it to keep track of Python packages used by the project, Tool -> Sync Python Requirements