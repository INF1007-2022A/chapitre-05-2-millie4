#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	sous_total = 0
	for a in data:
		sous_total += a[1] * a[2]
	taxes = sous_total * 0.15
	total = sous_total + taxes
	
	'''
	valeurs = [sous_total, taxes, total]
	new_valeurs = []
	for v in valeurs:
		v = round(v, 2)
		if v == int(v) : v = str(v) + ".00"
		elif (v * 10) == int(v * 10) : v = str(v) + "0"
		new_valeurs.append(v)
	
	'''
	return f'''{name}\nSOUS TOTAL {sous_total : >10.2f} $\nTAXES {taxes : >15.2f} $\nTOTAL {total : >15.2f} $'''


def format_number(number, num_dec):
	number = str(number)[::-1]
	formated_num = ""
	dec_count = 3 - num_dec % 3 #commencer les groupes de trois pour que ca arrive au point
	count = 0
	for i in range(0, len(number)):
		#pour les digits après la virgule
		if i < num_dec:
			if dec_count % 3 == 0:
				#ajouter espaces à tous les trois chiffres
				formated_num += " "
			formated_num += number[i] #ajouter le digit à la string finale
			dec_count += 1
		#pour le point (et éviter l'espace avant le point)
		if i == num_dec:
			if formated_num[-1] == " ":
				formated_num = formated_num[:-1] #delete l'espace avant le point s'il y en a un
			formated_num += number[i]
		#pour les digits avant la virgule (et éviter espace après le point)
		if i > num_dec:
			if count % 3 == 0 and count != 0 and number[i] != "-": 
				#ajouter un espace à tous les trois chiffres
				#sauf avant le - et apres le point
				formated_num += " " 
			formated_num += number[i]
			count += 1
	return formated_num[::-1]

def get_triangle(num_rows):
	cadre = 1 + num_rows * 2
	result = "+" * (cadre - 2)
	nbr_a = 1
	for i in range(1,num_rows):
		if i != 1: nbr_a += 2
		result += "\n" + "+" + " " * int((cadre - nbr_a - 4) * 0.5) + "A" * nbr_a +  " " * int((cadre - nbr_a - 4) * 0.5) + "+"
	result += "\n" + "+" * (cadre - 2)
	return result

if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-120345.67891, 5))

	print(get_triangle(2))
	print(get_triangle(9))
