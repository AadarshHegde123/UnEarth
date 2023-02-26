import pygal

world_map =  pygal.maps.world.SupranationalWorld()
  
# set the title of map
world_map.title = 'UnEarth'
  
# adding the continents
world_map.add('Africa', [('africa')])
world_map.add('North america', [('north_america')])
world_map.add('Oceania', [('oceania')])
world_map.add('South america', [('south_america')])
world_map.add('Asia', [('asia')])
world_map.add('Europe', [('europe')])
world_map.add('Antartica', [('antartica')])
  
# save into the file
world_map.render_to_file('Map.svg')


