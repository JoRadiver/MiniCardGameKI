class Playable:
	pass

class Carrier:
	pass
	
class Effect:
	pass
	
class Ability:
	def __init__(self):
		pass
	def on_update(self):
		pass
	pass
	
class Weareable:
	pass
	
class TurnModifier:
	def __init__(self, damage, health, abilities, effects):
		self.damage = damage
		self.health = health
		self.abilities = abilities
		self.effects = effects
	
class Unit(Playable):
	def __init__(self, name, damage, health, abilities, effects):
		self.name = name
		self.start_damage = damage
		self.perma_damage_modifier = 0
		self.perma_health_modifier = 0
		self.turn_hp_modifier = 0
		self.turn_damage_modifier = 0
		self.start_health = health
		self.abilities = abilities
		self.effects = effects
		self.weareables = []
	def on_update(self):
		for effect in self.effects:
			effect.on_update()
		for weareable in self.weareables:
			weareable.on_update()
	def on_played(self):
		pass
	def on_start_turn(self):
		pass
	def on_end_turn(self):
		pass
	def on_end_fight(self):
		pass
	def on_death(self):
		pass
	def on_draw(self):
		pass
	def permanent_modify(self):
		pass
	def carry(self):
		pass
	
	
	