## Radiology System

### App Folders and Their Descriptions

| Folder      | Description |
| ----------- | ----------- |
| reject_analysis      | the second main parent directory containing the cache and config folders, as well as other configuration files of the app     |
| templates   | Contains views of the django app        |
| media   | Contains app media files (videos and audios)       |
| static   | Contains assets folder      |
| assets   | Contains css, js and images folders       |
| virtualenv   | Contains include, lib, Scripts folders and virtual environment configurations of the app      |
| requirements   | Contains base, development, staging, and production package requirements of the app       |
| utils   | Contains model and other base classes that can be inherited and used by other classes      |
| general_setup   | Contains management, migrations, models, views, admin, and services for the system administrator to setup app data related to jobs, holidays, examination types, educational levels, sub-departments      |
| accounts   | Contains custom user authentication (sign_in), sign_out and signed_out views,        |
| administrative_staff   |         |
| all_staff   | Contains all staff profile model, view, urls        |
| dashboard   |         |
| extraneous   | Contains views external to the site - error404 page        |
| facility   | Contains rooms and machines        |
| launch   | Launch screen with options to login as admin or staff        |
| patients   | Contains patient models, views, urls        |
| radiology_staff   | Contains radiology staff models, views, urls       |
| reject_analysis   | Contains views, models, urls, &c. for the analysis page of the acquired images        |
| helpfuls    | Contains filters and helpful lists       |
|    |         |
|    |         |
|    |         |



### App Files and Their Descriptions

| File      | Description |
| --------- | ----------- |
| README.md      | Contains descriptions of all project folders and files       |
| env_template   | a template for setting up local environment variables        |
| manage.py   | Django's command-line utility for administrative tasks making use of the dev, stage, or prod config files       | database       |
| wsgi.py   | The Web Server Gateway Interface presents a calling convention for web servers to forward requests to the website, making use of the dev, stage, or prod config files.        |
| utils/MyModel.py   | Contains a base class, MyModel to be inherited and used by every other model in the app       |
| env_template     | Contains default environment viriables       |
| utils/filters   | Contains filtered database values and filter functions        |
| utils/constants   | Contains global constants       |
| utils/helpers   | Contains helper functions for models and services in the app         |
| utils/matplotbase   | Contains functions for plotting graphs        |
|    |         |
|    |         |


### Files to create in dev/prod mode

| File      | Description |
| --------- | ----------- |
| .env      | Contains app environment viriables      |
| debug.log   | Contains code bugs in debug mode.         |
| .gitignore   | Contains names of files to exclude from git push        |
|    |         |
|    |         |


### App Color Palette
* Blue shades - #0074CC, #418EEA, #65A9FF, #86C5FF, #004392
* Pink shades - #C3456A, #FF7C9D
* Grey shades - #404756, #A4ABBD


### Resources
*  To understand the app structure, you may watch the first 30 mins of [this video](https://www.youtube.com/watch?v=IsAjtRfw8ps "App Structure").
