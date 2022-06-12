
# Ladder Royale Bot

## Project Introduction

This project provides the backend for the [@LadderRoyale](https://twitter.com/LadderRoyale), a Twitter bot that tracks Clash Royale's leaderboard. The backend is currently being run in an EC2 t2.Micro instance from AWS. Any feature additions will need to fit within this constrant, at least for the time being.

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

#### Set up local variables
Create a file name `.env` and include API keys from both [Clash Royale](https://developer.clashroyale.com/#/) and [Twitter](https://developer.twitter.com/en). The structure for these variables is given inside `main.py`.

#### Running the script
First open the crontab configuration file using:
```bash
  crontab -e
```
Add
```bash
	*/15 * * * *       cd /home/ec2-user/Ladder-Api/topladderbot && /usr/bin/python3 /home/ec2-user/Ladder-Api/topladderbot/main.py
```
to the configuration file. (The default text editor is VIM)
File directories depend on your setup. The delay between running the scripts is set to 15 minutes, which is just slightly more then it takes to run the script.

## Help or questions

Feel free to email me with ideas or questions:
<woolsey@student.ubc.ca>

## License

[GPL V3](https://choosealicense.com/licenses/gpl-3.0/)

