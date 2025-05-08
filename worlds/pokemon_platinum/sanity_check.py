"""
Looks through data object to double-check it makes sense. Will fail for missing or duplicate definitions or
duplicate claims and give warnings for unused and unignored locations or warps.
"""
import logging
from typing import List

from .data import data


_ignorable_locations = {
  
    # Event islands
   
}

_ignorable_warps = {

    # Department store elevator
   


    # Event islands
    
 



    # Multiplayer rooms
   
    
    

    # Unused content
    
    
}


def validate_regions() -> bool:
    error_messages: List[str] = []
    warn_messages: List[str] = []
    failed = False

    def error(message: str) -> None:
        nonlocal failed
        failed = True
        error_messages.append(message)

    def warn(message: str) -> None:
        warn_messages.append(message)

    # Check regions
    for name, region in data.regions.items():
        for region_exit in region.exits:
            if region_exit not in data.regions:
                error(f"Pokemon Platinum: Region [{region_exit}] referenced by [{name}] was not defined")

    # Check warps
    for warp_source, warp_dest in data.warp_map.items():
        if warp_source in _ignorable_warps:
            continue

        if warp_dest is None:
            error(f"Pokemon Platinum: Warp [{warp_source}] has no destination")
        elif not data.warps[warp_dest].connects_to(data.warps[warp_source]) and not data.warps[warp_source].is_one_way:
            error(f"Pokemon Platinum: Warp [{warp_source}] appears to be a one-way warp but was not marked as one")

    # Check locations
    claimed_locations = [location for region in data.regions.values() for location in region.locations]
    claimed_locations_set = set()
    for location_name in claimed_locations:
        if location_name in claimed_locations_set:
            error(f"Pokemon Platinum: Location [{location_name}] was claimed by multiple regions")
        claimed_locations_set.add(location_name)

    for location_name in data.locations:
        if location_name not in claimed_locations and location_name not in _ignorable_locations:
            warn(f"Pokemon Platinum: Location [{location_name}] was not claimed by any region")

    warn_messages.sort()
    error_messages.sort()

    for message in warn_messages:
        logging.warning(message)
    for message in error_messages:
        logging.error(message)

    logging.debug("Pokemon Platinum sanity check done. Found %s errors and %s warnings.", len(error_messages), len(warn_messages))

    return not failed
