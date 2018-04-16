# Simple UI to simulate HS moves
from graphics import *
from hearthstone.enums import BlockType, CardType, PlayState, State, Step, Zone


class HsUI:
	WINDOW_HEIGHT = 600
	WINDOW_WIDTH = 1000
	WINDOW_TITLE = "Hearthstone SIM"
	CARD_WIDTH = 100
	CARD_HEIGHT = 90
	CARD_SEPARATOR = 50
	ZONE_SEPARATOR = 120
	START_X = 10
	START_Y = 10

	def __init__(self, game):
		self.game = game

	def print_ui(self):

		"""
			Very simple "print UI" -> prints to console
		"""
		print ('\n### Player 1 with %r mana ###' % self.game.player1.max_mana)
		print ('# Hand #')
		print(self.game.player1.hand)
		print('\n# Field #')
		print(self.game.player1.field)

		print ('\n### Player 2 with %r mana ###' % self.game.player2.max_mana)
		print ('# Hand #')
		print(self.game.player2.hand)
		print('\n# Field #')
		print(self.game.player2.field)

	def print_gui(self):
		"""
			Simple GUI -> Uses simple python graphics library created by John Zelle
			http://mcsp.wartburg.edu/zelle/python/graphics.py
		"""

		win = GraphWin(self.WINDOW_TITLE, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

		# Player 1 stats
		card_pos = 0
		zone = 0
		for player in self.game.players:
			self.draw_player(player, card_pos, zone, win)
			card_pos = card_pos+1

		# Player 1 hand
		card_pos = 0
		zone = zone + 1
		for card in self.game.player1.hand:
			self.draw_card(card, card_pos, zone, win)
			card_pos = card_pos+1

		# Player 1 field
		card_pos = 0
		zone = zone + 1
		for card in self.game.player1.field:
			self.draw_card(card, card_pos, zone, win)
			card_pos = card_pos+1

		# Player 2 field
		card_pos = 0
		zone = zone + 1
		for card in self.game.player2.field:
			self.draw_card(card, card_pos, zone, win)
			card_pos = card_pos+1

		# Player 2 hand
		card_pos = 0
		zone = zone + 1
		for card in self.game.player2.hand:
			self.draw_card(card, card_pos, zone, win)
			card_pos = card_pos+1

		win.getMouse()
		win.close()

	def draw_card(self, card, card_pos, zone, win):
		top_left_point = Point(
							self.START_X + card_pos * (self.CARD_WIDTH + self.CARD_SEPARATOR),
							self.START_Y + zone * self.ZONE_SEPARATOR)
		bottom_right_point = Point(
							self.START_X + card_pos * (self.CARD_WIDTH + self.CARD_SEPARATOR) +
							self.CARD_WIDTH, self.START_Y + self.CARD_HEIGHT + zone * self.ZONE_SEPARATOR)

		rect = Rectangle(top_left_point, bottom_right_point)
		rect.draw(win)

		# Cost is top left
		cost = Text(
				Point(
					self.START_X + card_pos * (self.CARD_WIDTH + self.CARD_SEPARATOR) + 5,
					self.START_Y + zone * self.ZONE_SEPARATOR + 5), card.cost)

		# Atk is bottom left
		if card.type == CardType.SPELL:
			atk = Text(
					Point(
						self.START_X + card_pos * (self.CARD_WIDTH + self.CARD_SEPARATOR) + 5,
						self.START_Y + self.CARD_HEIGHT + zone * self.ZONE_SEPARATOR - 5), 0)
		else:
			atk = Text(
					Point(
						self.START_X + card_pos * (self.CARD_WIDTH + self.CARD_SEPARATOR) + 5,
						self.START_Y + self.CARD_HEIGHT + zone * self.ZONE_SEPARATOR - 5), card.atk)

		# Health is bottom right
		if card.type == CardType.WEAPON:
			health = Text(
						Point(
							self.START_X + card_pos * (self.CARD_WIDTH + self.CARD_SEPARATOR) + self.CARD_WIDTH - 5,
							self.START_Y + self.CARD_HEIGHT + zone * self.ZONE_SEPARATOR - 5), card.durability)
		elif card.type != CardType.SPELL:
			health = Text(
						Point(
							self.START_X + card_pos * (self.CARD_WIDTH + self.CARD_SEPARATOR) + self.CARD_WIDTH - 5,
							self.START_Y + self.CARD_HEIGHT + zone * self.ZONE_SEPARATOR - 5), card.health)
		else:
			health = Text(
						Point(
							self.START_X + card_pos * (self.CARD_WIDTH + self.CARD_SEPARATOR) + self.CARD_WIDTH - 5,
							self.START_Y + self.CARD_HEIGHT + zone * self.ZONE_SEPARATOR - 5), 0)
		# Name is centered
		name = Text(
				Point(
					self.START_X + card_pos * (self.CARD_WIDTH + self.CARD_SEPARATOR) + self.CARD_WIDTH / 2,
					self.START_Y + zone * self.ZONE_SEPARATOR + self.CARD_HEIGHT / 2), card)

		# Draw card data on canvas #TODO need to un-hardcode font size
		cost.setSize(8)
		cost.draw(win)
		atk.setSize(8)
		atk.draw(win)
		health.setSize(8)
		health.draw(win)
		name.setSize(8)
		name.draw(win)

	def draw_player(self, player, card_pos, zone, win):
		top_left_point = Point(
							self.START_X + card_pos * (self.CARD_WIDTH + self.CARD_SEPARATOR),
							self.START_Y + zone * self.ZONE_SEPARATOR)
		bottom_right_point = Point(
								self.START_X + card_pos * (self.CARD_WIDTH + self.CARD_SEPARATOR) +
								self.CARD_WIDTH, self.START_Y + self.CARD_HEIGHT + zone * self.ZONE_SEPARATOR)

		rect = Rectangle(top_left_point, bottom_right_point)
		rect.draw(win)

		if player == self.game.current_player:
			top_left_point = Point(
								self.START_X + card_pos * (self.CARD_WIDTH + self.CARD_SEPARATOR) - 2,
								self.START_Y + zone * self.ZONE_SEPARATOR - 2)
			bottom_right_point = Point(
									self.START_X + card_pos * (self.CARD_WIDTH + self.CARD_SEPARATOR) +
									self.CARD_WIDTH + 2, self.START_Y + self.CARD_HEIGHT + zone * self.ZONE_SEPARATOR + 2)

			rect = Rectangle(top_left_point, bottom_right_point)
			rect.draw(win)

		# Attack is bottom left
		atk = Text(
				Point(
					self.START_X + card_pos * (self.CARD_WIDTH + self.CARD_SEPARATOR) + 5,
					self.START_Y + self.CARD_HEIGHT + zone * self.ZONE_SEPARATOR - 5), player.hero.atk)

		# Armor is top right
		armor = Text(
					Point(
						self.START_X + card_pos * (self.CARD_WIDTH + self.CARD_SEPARATOR) + self.CARD_WIDTH - 5,
						self.START_Y + zone * self.ZONE_SEPARATOR + 5), player.hero.armor)

		# Health is bottom right
		health = Text(
					Point(
						self.START_X + card_pos * (self.CARD_WIDTH + self.CARD_SEPARATOR) + self.CARD_WIDTH - 5,
						self.START_Y + self.CARD_HEIGHT + zone * self.ZONE_SEPARATOR - 5), player.hero.health)

		# Name is centered top
		name = Text(Point(self.START_X + card_pos * (self.CARD_WIDTH + self.CARD_SEPARATOR) + self.CARD_WIDTH / 2,
						  self.START_Y + zone * self.ZONE_SEPARATOR + 5), player.name)

		mana = Text(
					Point(
						self.START_X + card_pos * (self.CARD_WIDTH + self.CARD_SEPARATOR) + self.CARD_WIDTH / 2,
						self.START_Y + zone * self.ZONE_SEPARATOR + 15), 'Mana = %d' % player.mana)

		# Draw card data on canvas #TODO need to un-hardcode font size
		atk.setSize(8)
		atk.draw(win)
		armor.setSize(8)
		armor.draw(win)
		health.setSize(8)
		health.draw(win)
		name.setSize(8)
		name.draw(win)
		mana.setSize(8)
		mana.draw(win)

	def draw_character_attack(self, player, character, target):
		# index = player.field.index(character)
		# TBD
		pass
