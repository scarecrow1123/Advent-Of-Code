import re, itertools
shop_lines = open("shop.txt").read().splitlines()
weapons = {}
armors = {}
rings = {}
boss = {
  "hits": 109,
  "damage": 8,
  "armor": 2
    }
player = {
  "hits": 100,
  "damage": 0,
  "armor": 0
    }
player_hits = 100 
boss_hits = 109
combos = []
def update_shop(container, item):  
  name = item.split(" ")[0]
  meta = re.findall(r'\d+', item)
  container[name] = {}
  container[name]["cost"] = int(meta[0])
  container[name]["damage"] = int(meta[1])
  container[name]["armor"] = int(meta[2])
curr_container = weapons
for line in shop_lines:
  if "Weapons:" in line:
    curr_container = weapons
    continue
  if "Armor:" in line:
    curr_container = armors
    continue
  elif "Rings:" in line:
    curr_container = rings
    continue
  update_shop(curr_container, line)
weapon_list = weapons.keys()
armor_list = armors.keys()
armor_list.append("")
ring_list = rings.keys()
def get_total_cost(combo):
  combo_weapons = combo["weapon"]
  combo_armors = combo["armor"]
  combo_rings = combo["rings"]
  return sum([weapons[x]["cost"] for x in combo_weapons]) + sum([armors[x]["cost"] for x in combo_armors]) + sum([rings[x]["cost"] for x in combo_rings])

def get_ring_cost(ring_combo):
  return sum([rings[x]["cost"] for x in ring_combo])

def get_combo(weapon, armor, ring_combo):
  if armor != '':
    total_cost = weapons[weapon]["cost"] + armors[armor]["cost"] + get_ring_cost(ring_combo)
  else:
    total_cost = weapons[weapon]["cost"] + get_ring_cost(ring_combo)
  return {"weapon": [weapon], "armor": [armor], "rings": ring_combo, "total_cost": total_cost}

def init_combo():    
  global combos
  for weapon in weapon_list:
    combos.append(get_combo(weapon, '', []))
    armor_combos = itertools.combinations(armor_list, 1)
    for armor in armor_combos:
      combos.append(get_combo(weapon, armor[0], []))
      ring_count = 1
      while ring_count < 3:
        ring_choice_combos = itertools.combinations(rings, ring_count)
        for ring_combo in ring_choice_combos:
          combos.append(get_combo(weapon,armor[0], [x for x in ring_combo]))
        ring_count += 1

maxcost = 0
mincost = 99999999
def play(combos):
  global mincost
  global maxcost
  for combo in combos:
    player = {
        "hits": 100,
        "armor": 0,
        "damage": 0
        }
    boss = {
        "hits": 109,
        "armor": 2,
        "damage": 8
        }
    for i in combo["armor"]:
      if i != '':
        player["armor"] += armors[i]["armor"]
    for i in combo["weapon"]:
      if i != '':
        player["damage"] += weapons[i]["damage"]
    for i in combo["rings"]:
      player["armor"] += rings[i]["armor"]
      player["damage"] += rings[i]["damage"]
    turn = 1
    while player["hits"] > 0 and boss["hits"] > 0:
      if turn%2 == 0:
        loss = boss["damage"] - player["armor"]
        if loss < 0:
          loss = 1
        player["hits"] -= loss
      else:
        loss = player["damage"] - boss["armor"]
        if loss < 0:
          loss = 1
        boss["hits"] -= loss
      turn += 1
    if boss["hits"] <= 0:
      if combo["total_cost"] < mincost:
        mincost = combo["total_cost"]
    elif player["hits"] <= 0:
      if combo["total_cost"] > maxcost:
        maxcost = combo["total_cost"]
init_combo()
play(combos)
print mincost
print maxcost
