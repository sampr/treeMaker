import sys
import json

class Person:

	def __init__(self, last_name="", first_name="", relationship="", spouse_last="", spouse_first="", birth_date="", birth_place="", immigration_year="", death_date="", death_place="", cemetery="", marriage_date="", marriage_place="", occupations=""):
		self.last_name = last_name
		self.first_name = first_name
		self.relationship = relationship
		self.spouse_last = spouse_last
		self.spouse_first = spouse_first
		self.birth_date = birth_date
		self.birth_place = birth_place
		self.immigration_year = immigration_year
		self.death_date = death_date
		self.death_place = death_place
		self.cemetery = cemetery
		self.marriage_date = marriage_date
		self.marriage_place = marriage_place
		self.occupations = occupations

	def print_member(self):
		print("Name: {}, {}".format(self.last_name, self.first_name))
		print("Relationship: {}".format(self.relationship))
		print("Spouse Name: {}, {}".format(self.spouse_last, self.spouse_first))
		print("Birth: {}, {}".format(self.birth_date, self.birth_place))
		if self.immigration_year != "":
			print("Immigration year: {}".format(self.immigration_year))
		if self.death_date != "x":
			print("Death: {}".format(self.death_date, self.death_place))
			print("Cemetary: {}".format(self.cemetery))
		if self.spouse_last == "x" or self.spouse_last == "":
			print("Marriage: {}, {}".format(self.marriage_date, self.marriage_place))
		print("Occupations:")
		for i in range(len(self.occupations)):
			print(self.occupations[i][0], self.occupations[i][1])

#Continuously take input for each person and add to map
def readIn():

	family = []

	while True:

		last_name = input("Enter last name: ")

		if last_name == "quit":
			break

		first_name = input("Enter first name: ")
		relationship = input("Enter relationship: ")
		spouse_last = input("Enter spouse's last name: ")
		spouse_first = input("Enter spouse's first name: ")
		birth_date = input("Enter birth date: ")
		birth_place = input("Enter birth place: ")
		immigration_year = input("Enter immigration year: ")
		death_date = input("Enter death date: ")
		death_place = input("Enter death place: ")
		cemetery = input("Enter cemetery: ")
		marriage_date = input("Enter marriage date: ")
		marriage_place = input("Enter marriage place: ")
		occupations = []
		while True:
			year = input("Enter occupation year: ")
			if year == "quit":
				break
			occupation = input("Enter occupation for {}: ".format(year))
			occupations.append((year, occupation))

		member = Person(last_name, first_name, relationship, spouse_last, spouse_first, birth_date, birth_place, immigration_year, death_date, death_place, cemetery, marriage_date, marriage_place, occupations)

		family.append(member)

	return family


def toJson():

	#Write map to json and export to file

	return 0


def main():

	familyData = readIn()

	for person in familyData:
		person.print_member()

	return 0

if __name__ == '__main__':
    main()