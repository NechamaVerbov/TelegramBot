# {Teachilde}
<https://t.me/teachild_bot>

{Parent-child learning bot: The parent can advance his child's knowledge by assigning specific tasks and following the progress via reports } 

* {Nechama Verbov}
* {Chedva Edry}
* {Michal Ratner}
* {Tirza Rubinstain}

{OPTIONAL: MORE PROJECT INFO HERE}

## Screenshots

![SCREESHOT DECSRIPTION](screenshots/shopping-list-bot-1.png)

## How to Run This Bot
### Prerequisites
* Python 3.7
* pipenv
* mongoDB


### Setup
* Clone this repo from github
* Install dependencies: `pipenv install`
* Get a BOT ID from the [botfather](https://telegram.me/BotFather).
* Create a `secret_settings.py` file:

        BOT_TOKEN = "your-bot-token-here"

### Run
To run the bot use:

    pipenv run python bot.py

### Running tests
First make sure to install all dev dependencies:

    pipenv install --dev

To run all test  use:

    pipenv run pytest

(Or just `pytest` if running in a pipenv shell.)

## Credits and References
* [Telegram Docs](https://core.telegram.org/bots)
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
* [mongoDB Documentation] (https://www.mongodb.com/) 
* [w3resource](https://www.w3resource.com/) 

