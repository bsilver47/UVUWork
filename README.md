# UVUWork
This Repository holds some of the projects I programmed while working for the ERP Software Services (ESS) team at Utah Valley University.

## ellucianDownloadAndUpdate.py
The purpose of this program is to allow a member of the ESS team to update a spreadsheet of every package that has been or needs to be updated when preparing to implement new updates provided by Ellucian. This is done by utilizing Playwright to download an Excel file from Ellucian's website containing a list of updates since the last time an update was performed. The program then Extracts the data from that file, Transforms it to a usable and workable format, then it Loads it into a master spreadsheet. This process of data processing is commonly referred to as ETL, and more information about how this is performed and implemented is contained in the file itself.

## drawingAPIs.py
With this program, I was charged with the task of helping members of my team learn Python through creation of a dedicated application that can serve as an example of formatting and functionality. This file utilizes an API from NOAA, as a part of their Weather Service. Additionally, TKinter is used to display this data in a Graphic User Interface (GUI).

## weatherPage
Similar to drawingAPIs.py, weatherPage utilizes the same API from NOAA and displays it in a GUI. The difference is, weatherPage utilizes Django instead of TKinter. Django is a web framework that has a number of specialties but, in this case, is utilized to demonstrate simple use of variables and some of the ways that Django can display processed data in a simple web app. In addition to this information, the hello/index.html page displays a number of iframes that serve to display information in card and banner formats.
Another point of note is that, in addition to the dependencies referenced in each file, hello/index.html utilizes Bootstrap and, in this case, is aided by django-bootstrap-v5.
