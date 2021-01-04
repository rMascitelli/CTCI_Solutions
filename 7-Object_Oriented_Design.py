# Chapter 7 - OO Design
queuelib = __import__('3-Stacks_and_Queues')

# Example - Restaurant Class

class Guest:
	def __init__(self, name):
		if(not(isinstance(name, string))):
			print("Invalid name provided")
		else:
			self.name = name

class Party:
	def __init__(self, guest):
		self.guests = [guest]
		self.reservationID = None
		self.tableID = None

	def add(self, guest):
		self.guests += [guest]

	def makeReservation(self, time):
		print("Trying to make reservation for", time)
		r.serviceReservation(time, self)								# TODO: There should be a better way to call methods across classes, this feels dangerous

	def requestTable(self):
		print("Making request for table")
		r.serviceReservation(None, self)

# TODO: Implement part 2 - Ordering + Receiving Food
#			- Need another queue `tableID waiting_food[]`
#			- Implement a server() thread, and another queue `tableID chef_waiting[]` to show which tables food is ready
# 		Implement part 3 - Finishing + Freeing a table
#			- One more final queue `tableID waiting_bill[]`
class Restaurant:

	# num_tables defines number of each type of table
	# Tables of 4, 8, and 12 will be created
	def __init__(self, num_tables):

		# Create all freeTables[] queues
		# table size = 4 + 4s
		# table ID = table_size + table_num (ex- 121, 122, 123)
		freeTables = []
		for s in range(0, 3):					# Only 3 table sizes right now (4, 8, 12)
			temp = queuelib.Queue(int(str(4 + 4*s) + "1"))
			for i in range(1, num_tables):
				temp.enQueue(int(str(4 + 4*s) + str(i)))

			freeTables.append(temp)

		self.freeTables = freeTables									# Array of Queues containing TableIDs
		self.waiting = [Queue(None), Queue(None), Queue(None)]			# Array of Queues (of Party) to show which Parties are waiting currently
		self.reservations = {											# Dict of Time:Party[] to keep track of reservations for a specific time
			"5:30" : Queue(None), 
			"6:00" : Queue(None),
			"6:30" : Queue(None)
		}

	# Called by instance of Party, time=None means the reservation is being made on the spot (not in advance)
	def serviceReservation(self, time=None, party):
		resID = 0 				# TODO: Need some logic to create a reservationID ... do I even need reservationIDs?
		party.reservationID = resID

		if(time == None):
			self.waiting[len(party.guests) // 4].enQueue(party)				# Place this party in the appropriate waiting[] index
		else:
			self.reservations[time].enQueue(party)

	# Runs periodically at every reservation time, and adds Party to self.waiting[]
	def reservationSystem(self, time):
		print("Thread that checks self.reservations and updates waiting[], also creates reservations") 
		for party in self.reservations[time]:
			self.waiting[len(party.guests) // 4].enQueue(party)


	def host(self):
		print("Thread that checks freeTables for open spots, then checks waiting[] for next appropriate guest")
		for table_size in range(0, len(self.freeTables)):
			for t in table_size:
				t_id = t.deQueue()									# Pop an element from the queues in freeTables[]
				party = self.waiting[table_size].deQueue()			# Pop a party from the waiting[] queue
				if(party != None):
					print(party.guests[0], "party of", len[party.guests], " !")					
					party.tableID = t_id							# Now the party has a tableID (meaning they've been seated)

r = Restaurant(3)