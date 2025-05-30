"""
Logic rule definitions for Pokemon Platinum
"""
from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

from .data import data
from .options import EliteFourRequirement, CyrusRequirement, Goal

if TYPE_CHECKING:
    from . import PokemonPlatinumWorld


# Rules are organized by town/route/dungeon and ordered approximately
# by when you would first reach that place in a vanilla playthrough.
def set_rules(world: "PokemonPlatinumWorld") -> None:
    def can_cut(state: CollectionState):
        return state.has("HM01 Cut", world.player) and state.has("Forest Badge", world.player)

    def can_surf(state: CollectionState):
        return state.has("HM03 Surf", world.player) and state.has("Fen Badge", world.player)

    def can_strength(state: CollectionState):
        return state.has("HM04 Strength", world.player) and state.has("Mine Badge", world.player)

    def can_flash(state: CollectionState):
        return state.has("HM05 Defog", world.player) and state.has("Relic Badge", world.player)

    def can_rock_smash(state: CollectionState):
        return state.has("HM06 Rock Smash", world.player) and state.has("Coal Badge", world.player)

    def can_waterfall(state: CollectionState):
        return state.has("HM07 Waterfall", world.player) and state.has("Beacon Badge", world.player)

    def can_dive(state: CollectionState):
        return state.has("HM08 Rock Climb", world.player) and state.has("Icicle Badge", world.player)

    def has_acro_bike(state: CollectionState):
        return state.has("Bike", world.player)
    
    def defeated_n_gym_leaders(state: CollectionState, n: int) -> bool:
        return sum([state.has(event, world.player) for event in [
            "EVENT_DEFEAT_ROARK",
            "EVENT_DEFEAT_GARDENIA",
            "EVENT_DEFEAT_FANTINA",
            "EVENT_DEFEAT_MAYLENE",
            "EVENT_DEFEAT_WAKE",
            "EVENT_DEFEAT_BYRON",
            "EVENT_DEFEAT_CANDICE",
            "EVENT_DEFEAT_VOLKNER"
        ]]) >= n

    def get_entrance(entrance: str):
        return world.multiworld.get_entrance(entrance, world.player)

    def get_location(location: str):
        if location in data.locations:
            location = data.locations[location].label

        return world.multiworld.get_location(location, world.player)

    victory_event_name = "EVENT_DEFEAT_CHAMPION"
    if world.options.goal == Goal.option_barry:
        victory_event_name = "EVENT_DEFEAT_BARRY"
    elif world.options.goal == Goal.option_cyrus:
        victory_event_name = "EVENT_DEFEAT_CYRUS"

    world.multiworld.completion_condition[world.player] = lambda state: state.has(victory_event_name, world.player)

    # Sky
    if world.options.fly_without_badge:
        set_rule(
            get_entrance("REGION_TWINLEAF_TOWN/MAIN -> REGION_SKY"),
            lambda state: state.has("HM02 Fly", world.player)
        )
    else:
        set_rule(
            get_entrance("REGION_TWINLEAF_TOWN/MAIN -> REGION_SKY"),
            lambda state: state.has("HM02 Fly", world.player) and state.has("Cobble Badge", world.player)
        )
    set_rule(
        get_entrance("REGION_SKY -> REGION_TWINLEAF_TOWN/MAIN"),
        lambda state: state.has("EVENT_VISITED_TWINLEAF_TOWN", world.player)
    )
    set_rule(
        get_entrance("REGION_SKY -> REGION_SANDGEM_TOWN/MAIN"),
        lambda state: state.has("EVENT_VISITED_SANDGEM_TOWN", world.player)
    )
    set_rule(
        get_entrance("REGION_SKY -> REGION_JUBILIFE_CITY/MAIN"),
        lambda state: state.has("EVENT_VISITED_JUBILIFE_CITY", world.player)
    )
    set_rule(
        get_entrance("REGION_SKY -> REGION_OREBURGH_CITY/MAIN"),
        lambda state: state.has("EVENT_VISITED_OREBURGH_CITY", world.player)
    )
    set_rule(
        get_entrance("REGION_SKY -> REGION_FLOAROMA_TOWN/MAIN"),
        lambda state: state.has("EVENT_VISITED_FLOAROMA_TOWN", world.player)
    )
    set_rule(
        get_entrance("REGION_SKY -> REGION_ETERNA_CITY/MAIN"),
        lambda state: state.has("EVENT_VISITED_ETERNA_CITY", world.player)
    )
    set_rule(
        get_entrance("REGION_SKY -> REGION_HEARTHOME_CITY/MAIN"),
        lambda state: state.has("EVENT_VISITED_HEARTHOME_CITY", world.player)
    )
    set_rule(
        get_entrance("REGION_SKY -> REGION_SOLACEON_TOWN/MAIN"),
        lambda state: state.has("EVENT_VISITED_SOLACEON_TOWN", world.player)
    )
    set_rule(
        get_entrance("REGION_SKY -> REGION_VEILSTONE_CITY/MAIN"),
        lambda state: state.has("EVENT_VISITED_VEILSTONE_CITY", world.player)
    )
    set_rule(
        get_entrance("REGION_SKY -> REGION_PASTORIA_CITY/MAIN"),
        lambda state: state.has("EVENT_VISITED_PASTORIA_CITY", world.player)
    )
    set_rule(
        get_entrance("REGION_SKY -> REGION_CELESTIC_TOWN/MAIN"),
        lambda state: state.has("EVENT_VISITED_CELESTIC_TOWN", world.player)
    )
    set_rule(
        get_entrance("REGION_SKY -> REGION_CANALAVE_CITY/MAIN"),
        lambda state: state.has("EVENT_VISITED_CANALAVE_CITY", world.player)
    )
    set_rule(
        get_entrance("REGION_SKY -> REGION_SNOWPOINT_CITY/MAIN"),
        lambda state: state.has("EVENT_VISITED_SNOWPOINT_CITY", world.player)
    )
    set_rule(
        get_entrance("REGION_SKY -> REGION_SUNYSHORE_CITY/MAIN"),
        lambda state: state.has("EVENT_VISITED_SUNYSHORE_CITY", world.player)
    )
    set_rule(
        get_entrance("REGION_SKY -> REGION_POKEMON_LEAGUE/SOUTH"),
        lambda state: state.has("EVENT_VISITED_POKEMON_LEAGUE", world.player)
    )
    set_rule(
        get_entrance("REGION_SKY -> REGION_FIGHT_AREA/MAIN"),
        lambda state: state.has("EVENT_VISITED_FIGHT_AREA", world.player)
    )
    set_rule(
        get_entrance("REGION_SKY -> REGION_RESORT_AREA/MAIN"),
        lambda state: state.has("EVENT_VISITED_RESORT_AREA", world.player)
    )
    set_rule(
        get_entrance("REGION_SKY -> REGION_SURVIVAL_AREA/MAIN"),
        lambda state: state.has("EVENT_VISITED_SURVIVAL_AREA", world.player)
    )

    # Oreburgh Gate
    set_rule(
        get_entrance("REGION_OREBURGH_GATE_1F/MAIN -> REGION_OREBURGH_GATE_B1F/MAIN"),
        hm_rules["HM06 ROCK SMASH"]
    )
   
    # Route 207
    set_rule(
        get_entrance("REGION_ROUTE207/SOUTH_BELOW_SLOPE -> REGION_ROUTE_207/MAIN_ABOVE_SLOPE"),
        lambda state: has_bike(state) 
    )
    
    # Ravaged Path
    set_rule(
        get_entrance("REGION_RAVAGED_PATH/SOUTH -> REGION_RAVAGED_PATH/EAST"),
        hm_rules["HM06 ROCK SMASH"]
    )
    set_rule(
        get_entrance("REGION_RAVAGED_PATH/EAST -> REGION_RAVAGED_PATH/SOUTH"),
        hm_rules["HM06 ROCK SMASH"]
    )
    # Route 205 (Galactic Grunts)
    set_rule(
        get_entrance("REGION_ROUTE205/SOUTH_BELOW_GRUNTS -> REGION_ROUTE205/SOUTH_ABOVE_GRUNTS"),
        lambda state: state.has("EVENT_DEFEAT_MARS_VALLEY_WINDWORKS", world.player)
    )

    # Eterna Forest
    set_rule(
        get_entrance("REGION_ETERNA_FOREST/MAIN -> REGION_ETERNA_FOREST/NORTH"),
        hm_rules["HM01 Cut"]
    )
    # Eterna City
    set_rule(
        get_entrance("REGION_ETERNA_CITY/MAIN -> REGION_ETERNA_CITY/NORTH"),
        hm_rules["HM01 Cut"]
    )
    set_rule(
        get_entrance("REGION_ETERNA_FOREST/NORTH -> REGION_ETERNA_FOREST/MAIN"),
        hm_rules["HM01 Cut"]
    )
    # Route 206 (Cut)
    
    # Mount Coronet South (1F) (surf/rock climb/strength)
    
    # Hearthome City
    
    # Route 210(South) (Secretpotion/Psyducks)
    
  

    # Celestic Town

    if world.options.cyrus_requirement == cyrusRequirement.option_badges:
        set_rule(
            get_entrance("REGION_CELESTIC_TOWN/MAIN -> MAP_CELESTIC_RUINS/MAIN"),
            lambda state: state.has_group("Badges", world.player, world.options.cyrus_count.value)
        )
    else:
        set_rule(
            get_entrance("REGION_CELESTIC_TOWN/MAIN -> MAP_CELESTIC_RUINS/MAIN"),
            lambda state: defeated_n_gym_leaders(state, world.options.cyrus_count.value)
        )
   

    # Route 218
    set_rule(
        get_entrance("REGION_ROUTE218/EAST -> REGION_ROUTE218/WATER"),
        hm_rules["HM03 Surf"]
    )
    set_rule(
        get_entrance("REGION_ROUTE218/WEST -> REGION_ROUTE218/WATER"),
        hm_rules["HM03 Surf"]
    )
    
    # Mount Coronet (1F)
    
    # Sunyshore City (Talk to volkner in lighthouse to get into his gym)
    
    # Sunyshore City -> Route 223
    
    # Victory Road (1F)
    
    # Pokemon League
    


  
    # NPC Gifts
    if world.options.npc_gifts:
        #  Town
        set_rule(
            get_location(""),
            lambda state: state.has("", world.player) and state.has("", world.player)
        )

    # Add Dowsing Machine requirement to hidden items
    if world.options.require_itemfinder:
        for location in world.multiworld.get_locations(world.player):
            if location.tags is not None and "Hidden_Item" in location.tags:
                add_rule(
                    location,
                    lambda state: state.has("Dowsing Machine", world.player)
                )

    # Add Flash requirements to dark caves
    if world.options.require_flash:
        # WayWard Cave
        add_rule(
            get_entrance("MAP_WAYWARD_CAVE:0"),
            can_flash
        )
      
