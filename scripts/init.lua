-- entry point for all lua code of the pack
-- more info on the lua API: https://github.com/black-sliver/PopTracker/blob/master/doc/PACKS.md#lua-interface
ENABLE_DEBUG_LOG = true
-- get current variant
local variant = Tracker.ActiveVariantUID
-- check variant info
IS_ITEMS_ONLY = variant:find("itemsonly")
for _, var in ipairs({"vanilla_v", "vanilla_h"}) do
    if variant:find(var) then
        IS_VANILLA = true
        break
    end
end
for _, var in ipairs({"vanilla_v", "archipelago_v"}) do
    if variant:find(var) then
        IS_VERTICAL = true
        break
    end
end

print("-- Example Tracker --")
print("Loaded variant: ", variant)
if ENABLE_DEBUG_LOG then
    print("Debug logging is enabled!")
end

-- Utility Script for helper functions etc.
ScriptHost:LoadScript("scripts/utils.lua")

-- Logic
ScriptHost:LoadScript("scripts/logic/logic.lua")

-- Custom Items
ScriptHost:LoadScript("scripts/custom_items/class.lua")
ScriptHost:LoadScript("scripts/custom_items/progressiveTogglePlus.lua")
ScriptHost:LoadScript("scripts/custom_items/progressiveTogglePlusWrapper.lua")

-- Items
Tracker:AddItems("items/items.jsonc")
Tracker:AddItems("items/red_souls.jsonc")
Tracker:AddItems("items/blue_souls.jsonc")
Tracker:AddItems("items/yellow_souls.jsonc")
Tracker:AddItems("items/grey_souls.jsonc")

if not IS_ITEMS_ONLY then -- <--- use variant info to optimize loading
    -- Maps
    Tracker:AddMaps("maps/maps.jsonc")
    -- Locations
    if not IS_VANILLA then
        Tracker:AddLocations("locations/locations.jsonc")
    else
        Tracker:AddLocations("locations/backend_v.jsonc")
        Tracker:AddLocations("locations/frontend_v.jsonc")
    end
end

-- Layout
Tracker:AddLayouts("layouts/items.jsonc")
Tracker:AddLayouts("layouts/broadcast.jsonc")
if IS_VERTICAL then
    Tracker:AddLayouts("var_vertical/layouts/tracker.jsonc")
else
    Tracker:AddLayouts("layouts/tracker.jsonc")
end

-- AutoTracking for Poptracker
if PopVersion and PopVersion >= "0.18.0" then
    ScriptHost:LoadScript("scripts/autotracking.lua")
end
