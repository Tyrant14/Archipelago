"""
Option definitions for Pokemon Platinum
"""
from dataclasses import dataclass
from typing import Dict, Type

from Options import Choice, DefaultOnToggle, Option, OptionSet, Range, Toggle, FreeText, PerGameCommonOptions

from .data import data


class Goal(Choice):
    """
    Determines what your goal is to consider the game beaten

    Champion: Become the champion and enter the hall of fame
    Rival: Beat the Rival at the Survival Area
    Champion2: Beat the E4 for the Second Time (2nd and beyond are harder than first)
    Cyrus: Beat Cyrus in Celestic Town
    Plate Hunt Goal?: Find all 16 plates to receive the Azure Flute and defeat/catch Arceus at Origin Hall
    """
    display_name = "Goal"
    default = 0
    option_champion = 0
    option_rival = 1
    option_champion2 = 2
    option_cyrus = 3
    option_plate_hunt = 4


class RandomizeBadges(Choice):
    """
    Adds Badges to the pool

    Vanilla: Gym leaders give their own badge
    Shuffle: Gym leaders give a random badge
    Completely Random: Badges can be found anywhere
    """
    display_name = "Randomize Badges"
    default = 2
    option_vanilla = 0
    option_shuffle = 1
    option_completely_random = 2


class RandomizeHms(Choice):
    """
    Adds HMs to the pool

    Vanilla: HMs are at their vanilla locations
    Shuffle: HMs are shuffled among vanilla HM locations
    Completely Random: HMs can be found anywhere
    """
    display_name = "Randomize HMs"
    default = 2
    option_vanilla = 0
    option_shuffle = 1
    option_completely_random = 2


class RandomizeKeyItems(DefaultOnToggle):
    """
    Adds most key items to the pool. These are usually required to unlock
    a location or region (e.g. the 3 Coupons, Works Key, Galactic Key)
    """
    display_name = "Randomize Key Items"


class RandomizeBike(Toggle):
    """
    Adds the bike to the pool
    """
    display_name = "Randomize Bike"


class RandomizeRods(Toggle):
    """
    Adds fishing rods to the pool
    """
    display_name = "Randomize Fishing Rods"


class RandomizeOverworldItems(DefaultOnToggle):
    """
    Adds items on the ground with a Pokeball sprite to the pool
    """
    display_name = "Randomize Overworld Items"


class RandomizeHiddenItems(Toggle):
    """
    Adds hidden items to the pool
    """
    display_name = "Randomize Hidden Items"


class RandomizeNpcGifts(Toggle):
    """
    Adds most gifts received from NPCs to the pool (not including key items or HMs)
    """
    display_name = "Randomize NPC Gifts"


class ItemPoolType(Choice):
    """
    Determines which non-progression items get put into the item pool

    Shuffled: Item pool consists of shuffled vanilla items
    Diverse Balanced: Item pool consists of random items approximately proportioned
    according to what they're replacing (i.e. more pokeballs, fewer X items, etc...)
    Diverse: Item pool consists of uniformly random (non-unique) items
    """
    display_name = "Item Pool Type"
    default = 0
    option_shuffled = 0
    option_diverse_balanced = 1
    option_diverse = 2


class HiddenItemsRequireDowsingMachine(DefaultOnToggle):
    """
    The Dowsing Machine is logically required to pick up hidden items
    """
    display_name = "Require Dowsing Machine"


class DarkCavesRequireFlash(DefaultOnToggle):
    """
    The cave beneath Cycling Road logically requires Flash
    """
    display_name = "Require Flash"


class FoggyRoutesRequireDefog(DefaultOnToggle):
    """
    The route to Celestic Town logically requires Defog
    """
    display_name = "Require Defog"

"""
This is currently not supported for Platinum beyond default
class EliteFourRequirement(Choice):
    Sets the requirements to challenge the elite four

    Badges: Obtain some number of badges
    "Gyms: Defeat some number of gyms

    display_name = "Elite Four Requirement"
    default = 0
    option_badges = 0
    option_gyms = 1



class EliteFourCount(Range):
    Sets the number of badges/gyms required to challenge the elite four
    display_name = "Elite Four Count"
    range_start = 0
    range_end = 8
    default = 8
    
 Sets the requirements to challenge Cyrus at Celestic Ruins

    Badges: Obtain some number of badges
    "Gyms: Defeat some number of gyms

    display_name = "Cyrus Requirement"
    default = 0
    option_badges = 0
    option_gyms = 1



class CyrusCount(Range):
    Sets the number of badges/gyms required to challenge the elite four
    display_name = "Cyrus Count"
    range_start = 0
    range_end = 4
    default = 4
    
class PlateHunt(Toggle):
   
    Sets whether plates need to be found to satisfy the Plate Hunt win condition.
    
    display_name = "Azure Flute needs Plates"


class PlateHunt(Range):
    
    Sets the number of Plates that must be found for the Azure Flute to defeat/catch Arceus.
    
    display_name = "Plate Hunt Count"
    range_start = 1
    range_end = 16
    default = 6


class Plates(OptionSet):
   
    Sets which Plates found can contribute to the Plate Hunt goal.
    
    display_name = "Allowed Plates"
    valid_keys = [
        "Fist Plate",
        "Sky Plate",
        "Toxic Plate",
        "Earth Plate",
        "Stone Plate",
        "Insect Plate",
        "Spooky Plate",
        "Iron Plate",
        "Flame Plate",
        "Splash Plate",
        "Meadow Plate",
        "Zap Plate",
        "Mind Plate",
        "Icicle Plate",
        "Draco Plate",
        "Dread Plate"
    ]
    default = valid_keys.copy()
"""

class RandomizeWildPokemon(Choice):
    """
    Randomizes wild pokemon encounters (grass, caves, water, fishing)

    Vanilla: Wild encounters are unchanged
    Match Base Stats: Wild pokemon are replaced with species with approximately the same bst
    Match Type: Wild pokemon are replaced with species that share a type with the original
    Match Base Stats and Type: Apply both Match Base Stats and Match Type
    Completely Random: There are no restrictions
    """
    display_name = "Randomize Wild Pokemon"
    default = 0
    option_vanilla = 0
    option_match_base_stats = 1
    option_match_type = 2
    option_match_base_stats_and_type = 3
    option_completely_random = 4


class AllowWildLegendaries(DefaultOnToggle):
    """
    Wild encounters can be replaced by legendaries. Only applied if Randomize Wild Pokemon is not Vanilla.
    """
    display_name = "Allow Wild Legendaries"


class RandomizeStarters(Choice):
    """
    Randomizes the starter pokemon in Professor Rowan's bag

    Vanilla: Starters are unchanged
    Match Base Stats: Starters are replaced with species with approximately the same bst
    Match Type: Starters are replaced with species that share a type with the original
    Match Base Stats and Type: Apply both Match Base Stats and Match Type
    Completely Random: There are no restrictions
    """
    display_name = "Randomize Starters"
    default = 0
    option_vanilla = 0
    option_match_base_stats = 1
    option_match_type = 2
    option_match_base_stats_and_type = 3
    option_completely_random = 4


class AllowStarterLegendaries(DefaultOnToggle):
    """
    Starters can be replaced by legendaries. Only applied if Randomize Starters is not Vanilla.
    """
    display_name = "Allow Starter Legendaries"


class RandomizeTrainerParties(Choice):
    """
    Randomizes the parties of all trainers.

    Vanilla: Parties are unchanged
    Match Base Stats: Trainer pokemon are replaced with species with approximately the same bst
    Match Type: Trainer pokemon are replaced with species that share a type with the original
    Match Base Stats and Type: Apply both Match Base Stats and Match Type
    Completely Random: There are no restrictions
    """
    display_name = "Randomize Trainer Parties"
    default = 0
    option_vanilla = 0
    option_match_base_stats = 1
    option_match_type = 2
    option_match_base_stats_and_type = 3
    option_completely_random = 4


class AllowTrainerLegendaries(DefaultOnToggle):
    """
    Enemy trainer pokemon can be replaced by legendaries. Only applied if Randomize Trainer Parties is not Vanilla.
    """
    display_name = "Allow Trainer Legendaries"


class RandomizeStaticEncounters(Choice):
    """
    Randomizes static encounters (Rayquaza, hidden Kekleons, fake Voltorb pokeballs, etc...)

    Vanilla: Static encounters are unchanged
    Shuffle: Static encounters are shuffled between each other
    Match Base Stats: Static encounters are replaced with species with approximately the same bst
    Match Type: Static encounters are replaced with species that share a type with the original
    Match Base Stats and Type: Apply both Match Base Stats and Match Type
    Completely Random: There are no restrictions
    """
    display_name = "Randomize Static Encounters"
    default = 0
    option_vanilla = 0
    option_shuffle = 1
    option_match_base_stats = 2
    option_match_type = 3
    option_match_base_stats_and_type = 4
    option_completely_random = 5

"""
class RandomizeTypes(Choice):
   
    Randomizes the type(s) of every pokemon. Each species will have the same number of types.

    Vanilla: Types are unchanged
    Shuffle: Types are shuffled globally for all species (e.g. every Water-type pokemon becomes Fire-type)
    Completely Random: Each species has its type(s) randomized
    Follow Evolutions: Types are randomized per evolution line instead of per species
    
    display_name = "Randomize Types"
    default = 0
    option_vanilla = 0
    option_shuffle = 1
    option_completely_random = 2
    option_follow_evolutions = 3
"""

class RandomizeAbilities(Choice):
    """
    Randomizes abilities of every species. Each species will have the same number of abilities.

    Vanilla: Abilities are unchanged
    Completely Random: Each species has its abilities randomized
    Follow Evolutions: Abilities are randomized, but if a pokemon would normally retain its ability
    when evolving, the random ability will also be retained
    """
    display_name = "Randomize Abilities"
    default = 0
    option_vanilla = 0
    option_completely_random = 1
    option_follow_evolutions = 2


class AbilityBlacklist(OptionSet):
    """
    A list of abilities which no pokemon should have if abilities are randomized.
    For example, you could exclude Wonder Guard and Arena Trap like this:
    ["Wonder Guard", "Arena Trap"]
    """
    display_name = "Ability Blacklist"
    valid_keys = frozenset([ability.label for ability in data.abilities])


class LevelUpMoves(Choice):
    """
    Randomizes the moves a pokemon learns when they reach a level where they would learn a move.
    Your starter is guaranteed to have a usable damaging move.

    Vanilla: Learnset is unchanged
    Randomized: Moves are randomized
    Start with Four Moves: Moves are randomized and all Pokemon know 4 moves at level 1
    """
    display_name = "Level Up Moves"
    default = 0
    option_vanilla = 0
    option_randomized = 1
    option_start_with_four_moves = 2


class MoveMatchTypeBias(Range):
    """
    Sets the probability that a learned move will be forced match one of the types of a pokemon.

    If a move is not forced to match type, it will roll for Normal type bias.
    """
    display_name = "Move Match Type Bias"
    range_start = 0
    range_end = 100
    default = 0


class MoveNormalTypeBias(Range):
    """
    After it has been decided that a move will not be forced to match types, sets the probability that a learned move
    will be forced to be the Normal type.

    If a move is not forced to be Normal, it will be completely random.
    """
    display_name = "Move Normal Type Bias"
    range_start = 0
    range_end = 100
    default = 0


class HmCompatibility(Choice):
    """
    Modifies the compatibility of HMs

    Vanilla: Compatibility is unchanged
    Fully Compatible: Every species can learn any HM
    Completely Random: Compatibility is 50/50 for every HM (does not remain consistent across evolution)
    """
    display_name = "HM Compatibility"
    default = 1
    option_vanilla = 0
    option_fully_compatible = 1
    option_completely_random = 2


class TmCompatibility(Choice):
    """
    Modifies the compatibility of TMs

    Vanilla: Compatibility is unchanged
    Fully Compatible: Every species can learn any TM
    Completely Random: Compatibility is 50/50 for every TM (does not remain consistent across evolution)
    """
    display_name = "TM Compatibility"
    default = 0
    option_vanilla = 0
    option_fully_compatible = 1
    option_completely_random = 2

"""
class TmMoves(Toggle):
    Randomizes the moves taught by TMs
    
    display_name = "TM Moves"
"""


class ReusableTms(Toggle):
    """
    Sets TMs to not break after use (they remain sellable)
    """
    display_name = "Reusable TMs"


class MinCatchRate(Range):
    """
    Sets the minimum catch rate a pokemon can have. Any pokemon with a catch rate below this floor will have it raised to this value.

    Legendaries are often in the single digits
    Fully evolved pokemon are often double digits
    Pidgey is 255
    """
    display_name = "Minimum Catch Rate"
    range_start = 3
    range_end = 255
    default = 3


class GuaranteedCatch(Toggle):
    """
    Every throw is guaranteed to catch a wild pokemon (Catch rate set to maximum)
    """
    display_name = "Guaranteed Catch"


class ExpModifier(Range):
    """
    Multiplies gained experience by a percentage

    100 is default
    50 is half
    200 is double
    etc...
    """
    display_name = "Exp Modifier"
    range_start = 0
    range_end = 1000
    default = 100


class BlindTrainers(Toggle):
    """
    Causes trainers to not start a battle with you unless you talk to them
    """
    display_name = "Blind Trainers"


class BetterShops(Toggle):
    """
    Pokemarts sell every item that can be obtained in a pokemart (except mail, which is still unique to the relevant city)
    """
    display_name = "Better Shops"


class RemoveRoadblocks(OptionSet):
    """
    Removes specific Checks that normally stand in your way until certain events are completed.

    This can open up the world a bit and make your playthrough less linear, but careful how many you remove.

    Possible values are:
    "Jubilife City Poketch"
    "Eterna Forest Galactic Grunts"
    "Solaceon Town Psyducks"
    "Route 222 Lady"
    "Canalave City Battlers"
    "Hearthome City NPCs" -- maybe?

    """
    display_name = "Remove Roadblocks"
    valid_keys = frozenset([
        "Jubilife City Poketch"
        "Eterna Forest Galactic Grunts"
        "Solaceon Town Psyducks"
        "Route 222 Lady"
        "Canalave City Battlers"
    ])


class FreeFlyLocation(Toggle):
    """
    Enables flying to one random location when Mom gives you the running shoes (excluding cities reachable with no items)
    """
    display_name = "Free Fly Location"


class FlyWithoutBadge(DefaultOnToggle):
    """
    Fly does not require the Feather Badge to use in the field
    """
    display_name = "Fly Without Badge"


class TurboA(Toggle):
    """
    Holding A will advance most text automatically
    """
    display_name = "Turbo A"


class ReceiveItemMessages(Choice):
    """
    Determines whether you receive an in-game notification when receiving an item. Items can still only be received in the overworld.

    All: Every item shows a message
    Progression: Only progression items show a message
    None: All items are added to your bag silently (badges will still show)
    """
    display_name = "Receive Item Messages"
    default = 0
    option_all = 0
    option_progression = 1
    option_none = 2


class UnlockFramerate(Choice):
    default = 1
    display_name = "Unlock the Framerate"
    option_no = 0
    option_yes = 1


class EasterEgg(FreeText):
    """
    ???
    """
    default = "Example Passphrase"


@dataclass
class PokemonPlatinumOptions(PerGameCommonOptions):
    goal: Goal

    badges: RandomizeBadges
    hms: RandomizeHms
    key_items: RandomizeKeyItems
    bikes: RandomizeBike
    rods: RandomizeRods
    overworld_items: RandomizeOverworldItems
    hidden_items: RandomizeHiddenItems
    npc_gifts: RandomizeNpcGifts
    item_pool_type: ItemPoolType

    require_itemfinder: HiddenItemsRequireDowsingMachine
    require_flash: DarkCavesRequireFlash
    #elite_four_requirement: EliteFourRequirement
    #elite_four_count: EliteFourCount

    wild_pokemon: RandomizeWildPokemon
    allow_wild_legendaries: AllowWildLegendaries
    starters: RandomizeStarters
    allow_starter_legendaries: AllowStarterLegendaries
    trainer_parties: RandomizeTrainerParties
    allow_trainer_legendaries: AllowTrainerLegendaries
    static_encounters: RandomizeStaticEncounters
    #types: RandomizeTypes
    abilities: RandomizeAbilities
    ability_blacklist: AbilityBlacklist

    level_up_moves: LevelUpMoves
    move_match_type_bias: MoveMatchTypeBias
    move_normal_type_bias: MoveNormalTypeBias
    tm_compatibility: TmCompatibility
    hm_compatibility: HmCompatibility
    #tm_moves: TmMoves
    reusable_tms: ReusableTms

    min_catch_rate: MinCatchRate
    guaranteed_catch: GuaranteedCatch
    exp_modifier: ExpModifier
    blind_trainers: BlindTrainers
    better_shops: BetterShops

    remove_roadblocks: RemoveRoadblocks
    free_fly_location: FreeFlyLocation
    fly_without_badge: FlyWithoutBadge

    turbo_a: TurboA
    receive_item_messages: ReceiveItemMessages

    unlock_framerate: UnlockFramerate

    easter_egg: EasterEgg
