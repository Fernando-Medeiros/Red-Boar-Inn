from ..controllers.auth_controller import auth
from ..controllers.home_controller import home

from ..controllers.world_controller import world
from ..controllers.arena_controller import arena
from ..controllers.market_controller import market
from ..controllers.profile_controller import profile
from ..controllers.craft_controller import craft
from ..controllers.tavern_controller import tavern
from ..controllers.inventory_controller import inventory
from ..controllers.options_controller import options

from ..controllers.message_controller import message


def register_routes(app):

    routes = [

        auth,
        home,
        world,
        arena,
        market,
        profile,
        craft,
        tavern,
        inventory,
        options,

        message        
    ]

    for route in routes:

        app.register_blueprint(route)
