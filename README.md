
# Ladder Royale Bot

## Project Introduction

This project provides the backend for the [@LadderRoyale](https://twitter.com/LadderRoyale) on Twitter. The backend is currently being run in an EC2 t2.Micro instance from AWS. Any feature additions will need to fit within this constrant, at least for the time being.

## Next Steps
- Currently, the API functions given by Supercell for Clash Royale only allow for information to be pulled from local leaderboards (country level). This bot gets around this by looping through all possible countries, but this is less than ideal.
- The bot currently only serves one function. In the future, I would like to add addtional features that provide Twitter users with more information provided by the [Clash Royale API](https://developer.clashroyale.com/#/documentation "Requires signin"). 


## Installation
This project runs on Python with a few additional libraries. These can be installed using [pip](https://pypi.org/project/pip/).
#### Download project

```bash
  git pull https://github.com/j1mmr/topladderbot.git
```

#### Install dependencies
```bash
  pip3 install python-env
  pip3 install tweepy
  pip3 install urllib3
```

#### Set up local Variables
Create a file name `.env` and include API keys from both [Clash Royale](https://developer.clashroyale.com/#/) and [Twitter](https://developer.twitter.com/en). The structure for these variables is given inside `main.py`.

#### Run
Simply run the program with:
```bash
  python3 main.Python
```
Leave the terminal window open to keep the bot running.
## Help or questions

Feel free to email me with ideas or questions:
<woolsey@student.ubc.ca>
## License

[GPL V3](https://choosealicense.com/licenses/gpl-3.0/)

