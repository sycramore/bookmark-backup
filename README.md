# bookmark-backup
Download your bookmarks as *html*-file and save them locally in a folder.

## Usage
* Export your bookmarks to html. An explanation for Chrome can be found [here](https://support.google.com/chrome/answer/96816?hl=en)
* Install dependencies in Python (bs4, etc)
* Change two path variables to the global path where your html bookmarks list lies.
* Execute download.py script in python.

## Notes
The script does not curl recursively on the bookmarked pages and only downloads the specific url in the bookmarked html.
