from ..controllers.arena_controller import arena
from ..controllers.auth_controller import auth
from ..controllers.craft_controller import craft
from ..controllers.home_controller import home
from ..controllers.inventory_controller import inventory
from ..controllers.market_controller import market
from ..controllers.message_controller import message
from ..controllers.options_controller import options
from ..controllers.profile_controller import profile
from ..controllers.tavern_controller import tavern
from ..controllers.world_controller import world


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
