<div align="center">
    <img align="center" src="https://img.shields.io/badge/Python-white?style=for-the-badge&logo=python&logoColor=yellow">
    <img align="center" src="https://img.shields.io/badge/Flask-white?style=for-the-badge&logo=flask&logoColor=black">    
    <img align="center" src="https://img.shields.io/badge/Javascript-white?style=for-the-badge&logo=javascript&logoColor=yellow">
    <img align="center" src="https://img.shields.io/badge/HTML5-white?style=for-the-badge&logo=html5&logoColor=orange">
    <img align="center" src="https://img.shields.io/badge/CSS3-white?style=for-the-badge&logo=css3&logoColor=blue">
    <img align="center" src="https://img.shields.io/badge/tailwindcss-white?style=for-the-badge&logo=tailwindcss&logoColor=blue">
    <img align="center" src="https://img.shields.io/badge/Mongodb-white?style=for-the-badge&logo=mongodb&logoColor=green">   
</div>

<br>

# The Red Boar Inn - **v.0.1.6** -> [link](https://app-redboarinn.herokuapp.com/)


<div align="center">
  
  *Profile Template - v.0.1.6*
  
  <img style="width: 900px" src="img/template_profile.png">

  *Arena Template - v.0.1.6*

  <img style="width: 900px" src="img/template_arena.png">
</div>


<br>


## About

The Red Boar Inn is a project in development that mixes **RPG, MMO and the SIMPLICITY** of running in any browser.

For this project I want the player to be able to interact and leave their mark on the game's history

The main idea is to allow you to create different types of gameplay choices and follow along.

This type of game is my personal choice, about what I would like to play, but it is not limited to that,
as the community grows I will accept suggestions for implementations.

> **"The freedom to participate in arena events, explore the world, create unique items to use or sell, help other players fight a common enemy, or stop for a while at the tavern and have a drink with the bard."**

<br>


## Story

**Dragonspear City** is the heart of this world, and this is where we find ourselves,
walking through the gates in search of adventure..

There are many adventurers, merchants and gypsies who arrive in this city, people of all types and ages,
with different ideas of living, always looking for something.


**If you like battles**, you'll find countless people here to challenge and prove your strength; Look for the gladiator guild next to the town hall.


**Looking for good items?**

You can go to market in the west district. You can find many items and even craft your own, because the king is famous for funding new craftsmen.


Well, **if you're the type who likes to get slapped with monsters**, the Adventurer's Guild is in the South district.
You can get your quests there.

Be careful what you accept,
believe it! every day I see the most bizarre things walking through this gate.


**You need to know the red boar inn.**

The red boar inn is the most famous inn in these lands and is for anyone who likes gold, adventure and a good beer.
This city is a world, I'll let you discover it for yourself.


**See you at the red boar inn!**



## Requirements

- Python 3.10
- Connection with [Mongodb atlas](https://account.mongodb.com/account/login)


## Scope Basis

- [x] Homepage
  - [x] About
  - [x] Updates 
  - [x] Login
  - [x] Create Account
  - [x] Recover Account
> - Gameplay
>   - [ ] Arena (45% **tests**)
>   - [ ] Craft 
>   - [ ] Inventory (50% - **tests**)
>   - [ ] Marketplace
>   - [ ] Profile (65%)
>   - [x] Tavern (**tests**)
>   - [ ] World
> - Others
>   - [ ] Friends
>   - [ ] Notifications
>   - [ ] Posts 


## To use this project

Clone this project
```console
git clone https://github.com/Fernando-Medeiros/Web-Game-FLask.git
```

Create the virtual environment
```console
virtualenv .venv
```

Activate .venv
```console
# Linux
source .venv/bin/activate
# Windows Power Shell
./.venv/bin/activate.ps1
```

Install dependencies
```console
pip install -r requirements.txt
```

Start localhost
```console
# Debug
flask run
# Gunicorn
gunicorn app:'create_app()'
```

## Structure
```console
.
├── app
│   ├── backend
│   │   ├── database.py
│   │   ├── flash_messages.py
│   │   ├── game
│   │   │   ├── arena.py
│   │   │   ├── equipment.py
│   │   │   ├── inventory.py
│   │   │   ├── profile.py
│   │   │   ├── status.py
│   │   │   ├── tavern.py
│   │   │   └── vocation.py
│   │   └── home
│   │       ├── auth_admin.py
│   │       ├── auth_create.py
│   │       ├── auth_login.py
│   │       ├── auth_recover.py
│   │       ├── home_page.py
│   │       └── updates_page.py
│   ├── controllers
│   │   ├── arena_controller.py
│   │   ├── auth_controller.py
│   │   ├── craft_controller.py
│   │   ├── home_controller.py
│   │   ├── inventory_controller.py
│   │   ├── market_controller.py
│   │   ├── message_controller.py
│   │   ├── options_controller.py
│   │   ├── profile_controller.py
│   │   ├── tavern_controller.py
│   │   └── world_controller.py
│   ├── extensions
│   │   ├── blueprints.py
│   │   └── models.py
│   ├── forms
│   │   ├── form_login.py
│   │   ├── form_new_account.py
│   │   ├── form_recover_password.py
│   │   └── form_settings.py
│   ├── __init__.py
│   ├── inventory.sqlite3
│   ├── models
│   │   ├── items
│   │   │   ├── collectable.py
│   │   │   ├── consumable.py
│   │   │   ├── equipment.py
│   │   │   └── weapon.py
│   │   ├── log.json
│   │   ├── post.json
│   │   ├── user.json
│   │   └── user.py
│   ├── static
│   │   ├── img
│   │   │   ├── favicon.ico
│   │   │   ├── icons
│   │   │   ├── items
│   │   │   │   ├── armor
│   │   │   │   ├── axe
│   │   │   │   ├── book
│   │   │   │   ├── boot
│   │   │   │   ├── bow
│   │   │   │   ├── craft
│   │   │   │   ├── dagger
│   │   │   │   ├── food
│   │   │   │   ├── glove
│   │   │   │   ├── hat
│   │   │   │   ├── helmet
│   │   │   │   ├── jewel
│   │   │   │   ├── key
│   │   │   │   ├── necklace
│   │   │   │   ├── potion
│   │   │   │   ├── ring
│   │   │   │   ├── robe
│   │   │   │   ├── scroll
│   │   │   │   ├── shield
│   │   │   │   ├── spellbook
│   │   │   │   ├── stick
│   │   │   │   ├── sword
│   │   │   │   └── tool
│   │   │   ├── pictures
│   │   │   └── sprites
│   │   │       ├── man
│   │   │       └── woman
│   │   └── js
│   │       ├── game
│   │       │   ├── arena.js
│   │       │   └── menu.js
│   │       └── home
│   │           ├── auth_create.js
│   │           ├── navbar.js
│   │           └── updates.js
│   └── views
│       ├── game
│       │   ├── alert.html
│       │   ├── arena
│       │   │   └── arena.html
│       │   ├── base.html
│       │   ├── craft
│       │   │   └── craft.html
│       │   ├── footer.html
│       │   ├── inventory
│       │   │   └── inventory.html
│       │   ├── market
│       │   │   └── market.html
│       │   ├── message
│       │   │   ├── friend.html
│       │   │   ├── message.html
│       │   │   └── notification.html
│       │   ├── navbar_left.html
│       │   ├── navbar_top.html
│       │   ├── options
│       │   │   └── options.html
│       │   ├── profile
│       │   │   ├── profile.html
│       │   │   └── sub
│       │   │       ├── equipment.html
│       │   │       ├── job.html
│       │   │       ├── settings.html
│       │   │       ├── skills.html
│       │   │       ├── status.html
│       │   │       └── vocation.html
│       │   ├── tavern
│       │   │   └── tavern.html
│       │   └── world
│       │       └── world.html
│       └── home
│           ├── alert.html
│           ├── base.html
│           ├── footer.html
│           ├── navbar.html
│           └── views
│               ├── about.html
│               ├── auth
│               │   ├── auth_token.html
│               │   ├── create.html
│               │   ├── login.html
│               │   ├── new_password.html
│               │   ├── send_email.html
│               │   └── template_email_recover.html
│               ├── home.html
│               └── updates.html
├── docs
│   ├── img
│   └── README.md
├── LICENSE
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── fbd93876bf45_.py
├── Procfile
├── requirements_test.txt
├── requirements.txt
├── runtime.txt
├── settings.toml
└── setup.py
```



## Credits

<img style="width: 50px" src="img/hypnos_art.png">

[hypnos_art](https://twitter.com/Hypnos_art?s=09) - Character sprites are exclusive artwork commissioned and licensed by Hypnos_Art


<img style="width: 50px" src="img/ionicons.png">

[ionicons](https://ionic.io/ionicons) - Most of the icons used are licensed by Ionicons


<img style="width: 50px" src="img/liuzishan.png">

[Liuzishan](https://www.freepik.com/author/liuzishan) - The images used are free to use, and are being mentioned along with the license on the site.



## License

[License - MIT](../LICENSE)

> **important:** You can use character sprites, just mention this project and artist and it will be of great help. \O/