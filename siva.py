# Basically use the url to determine what is shown and resolve the foward protocol image to convert node
# Needs signin - just import cookies in future
url='https://www.bungie.net/en/net/sim'
shape_to_link_LUT = {
	'triangle' : '/pubstatic/StaticPages/Sim/images/a7eb6b9d-895e-47ac-8e18-ca4dad62c6ac.png',
	'square'   : '/pubstatic/StaticPages/Sim/images/3c34f4f5-1914-4d30-a331-6b3fa4515d48.png',
	'diamond'  : '/pubstatic/StaticPages/Sim/images/3cf5d852-3a7a-45ce-9fa1-b1ec00f372d0.png',
	'circle'   : '/pubstatic/StaticPages/Sim/images/3692a247-d100-499d-be20-4934a272944b.png'
}

circle_to_square__square_to_diamond__diamond_to_triangle__triangle_to_circle_fifth_spot = '/pubstatic/StaticPages/Sim/images/13f9271e-58a6-462e-9507-de1c7dcc6962.png'
position_of_xbox_protocol = 5

#after solve image = class_name='ir'[0]
#my node = class_name='ir'[1]
#my fowarding protocol = class_name='ir'[2]
my_xbox_node = ['triangle', 'square', 'triangle', 'circle', 'diamond']
fowarded_xbox_node = []
counter=0
for shape in my_xbox_node:
	#making use of my known protocol: 5th spot circle_to_square__square_to_diamond__diamond_to_triangle__triangle_to_circle_fifth_spot
	if counter+1 == position_of_xbox_protocol:
		if shape is 'triangle':
			fowarded_xbox_node.append('circle')
		if shape is 'circle':
			fowarded_xbox_node.append('square')
		if shape is 'square':
			fowarded_xbox_node.append('diamond')
		if shape is 'diamond':
			fowarded_xbox_node.append('triangle')
	else:
		fowarded_xbox_node.append(shape)
	counter+=1
print '@ZWeed4U (XBOX): '+str(fowarded_xbox_node)

my_psn_node = ['diamond', 'square', 'diamond', 'circle', 'triangle']
circle_to_triangle__triangle_to_diamond__diamond_to_square__square_to_circle_second_spot = '/pubstatic/StaticPages/Sim/images/f4719173-3ec0-4eff-8a9c-4641495ece86.png'
position_of_psn_protocol = 2
fowarded_psn_node = []
counter=0
for shape in my_psn_node:
	#making use of my known protocol: 2nd spot circle_to_triangle__triangle_to_diamond__diamond_to_square__square_to_circle_second_spot
	if counter+1 == position_of_psn_protocol:
		if shape is 'triangle':
			fowarded_psn_node.append('diamond')
		if shape is 'circle':
			fowarded_psn_node.append('triangle')
		if shape is 'square':
			fowarded_psn_node.append('circle')
		if shape is 'diamond':
			fowarded_psn_node.append('square')
	else:
		fowarded_psn_node.append(shape)
	counter+=1
print '@ZWeed4-U (PSN): '+str(fowarded_psn_node)
