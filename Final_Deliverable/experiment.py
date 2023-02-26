from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import pygal
import numpy as np

app = Flask(__name__)

app.secret_key = '3dhsue7rhgdgdtte89dihTydvFSFYDFYDJDBgshjdgz67ii87'

world_map =  pygal.maps.world.World()

world_map.title = ''
  
# world_map.add('Africa', [('africa')])
# world_map.add('North america', [('north_america')])
# world_map.add('Oceania', [('oceania')])
# world_map.add('South america', [('south_america')])
# world_map.add('Asia', [('asia')])
# world_map.add('Europe', [('europe')])
# world_map.add('Antartica', [('antartica')])

country_ids = ['af', 'ax', 'al', 'dz', 'as', 'ad', 'ao', 'ai', 'aq', 'ag', 'ar', 'am', 'aw', 'au', 'at', 'az', 'bs', 'bh', 'bd', 'bb', 'by', 'be', 'bz', 'bj', 'bm', 'bt', 'bo', 'bq', 'ba', 'bw', 'bv', 'br', 'io', 'bn', 'bg', 'bf', 'bi', 'cv', 'kh', 'cm', 'ca', 'ky', 'cf', 'td', 'cl', 'cn', 'cx', 'cc', 'co', 'km', 'cg', 'cd', 'ck', 'cr', 'ci', 'hr', 'cu', 'cw', 'cy', 'cz', 'dk', 'dj', 'dm', 'do', 'ec', 'eg', 'sv', 'gq', 'er', 'ee', 'et', 'fk', 'fo', 'fj', 'fi', 'fr', 'gf', 'pf', 'tf', 'ga', 'gm', 'ge', 'de', 'gh', 'gi', 'gr', 'gl', 'gd', 'gp', 'gu', 'gt', 'gg', 'gn', 'gw', 'gy', 'ht', 'hm', 'va', 'hn', 'hk', 'hu', 'is', 'in', 'id', 'ir', 'iq', 'ie', 'im', 'il', 'it', 'jm', 'jp', 'je', 'jo', 'kz', 'ke', 'ki', 'kp', 'kr', 'kw', 'kg', 'la', 'lv', 'lb', 'ls', 'lr', 'ly', 'li', 'lt', 'lu', 'mo', 'mk', 'mg', 'mw', 'my', 'mv', 'ml', 'mt', 'mh', 'mq', 'mr', 'mu', 'yt', 'mx', 'fm', 'md', 'mc', 'mn', 'me', 'ms', 'ma', 'mz', 'mm', 'na', 'nr', 'np', 'nl', 'nc', 'nz', 'ni', 'ne', 'ng', 'nu', 'nf', 'mp', 'no', 'om', 'pk', 'pw', 'ps', 'pa', 'pg', 'py', 'pe', 'ph', 'pn', 'pl', 'pt', 'pr', 'qa', 're', 'ro', 'ru', 'rw', 'bl', 'sh', 'kn', 'lc', 'mf', 'pm', 'vc', 'ws', 'sm', 'st', 'sa', 'sn', 'rs', 'sc', 'sl', 'sg', 'sx', 'sk', 'si', 'sb', 'so', 'za', 'gs', 'ss', 'es', 'lk', 'sd', 'sr', 'sj', 'sz', 'se', 'ch', 'sy', 'tw', 'tj', 'tz', 'th', 'tl', 'tg', 'tk', 'to', 'tt', 'tn', 'tr', 'tm', 'tc', 'tv', 'ug', 'ua', 'ae', 'gb', 'us', 'um', 'uy', 'uz', 'vu', 've', 'vn', 'vg', 'vi', 'wf', 'eh', 'ye', 'zm']

idx = np.random.randint(0, len(country_ids))
print(idx)
starting_country = country_ids[idx]

world_map.add('First Country', {
    starting_country:1
})


world_map.render_to_file('static/world_map.svg') #Render SVG

@app.route('/')
def start():
    return render_template('about.html')

@app.route('/unearth')
def index():
    return render_template('index.html')

@app.route('/about')
def about_me():
    return render_template('about_me.html')

entered_us = 0
entered_ca = 0
#HANDLE MAP_CLICKS
@app.route('/map_click', methods=['POST'])
def map_click():
    # get the x and y coordinates of the click event
    x = int(request.form['x'])
    y = int(request.form['y'])
    
    # TODO: determine which part of the world map was clicked based on the coordinates
    # and return some information about the clicked location
    global entered_us
    global entered_ca
    us_food = ["burgers", "deep dish pizza", "hot dog"]
    us_artists = ["Drake", "Katy Perry", "Charlie Puth"]
    rand_idx = np.random.randint(0,4)
    if (194 <= y <= 227 and 552 <= x <= 622):
        flash('You clicked on The United States! Here are some of the most popular foods, music, and scenery in the US (Refresh to close this): The image above is Yosemite National Park, located in California and known for its stunning views. One of the USA\'s most well knwon dish is the '+  us_food[rand_idx] + ' and the country is known for artists like '+ us_artists[rand_idx])
        if (entered_us == 0):
            world_map.add('Been To: USA', [('us', 'marker', '#FF0000')])
            entered_us+=1
    elif (155 <= y <= 190 and 565 <= x <= 669):
        flash('You clicked on Canada! Here are some of the most popular foods, music, and scenery in Canada: (Refresh to close this): The image above is from Park Lake, Canada. It is one of the many lakes in Canada and houses stunning scenery and numerous hiking trails')
        if (entered_ca == 0):
            world_map.add('Been To: CA', [('ca')])
            entered_ca+=1

    world_map.render_to_file('static/world_map.svg') #Render SVG    
    print("Clicked at " , x , " ",  y)
    return f"Clicked at ({x}, {y})"

if __name__ == '__main__':
    app.run(debug=True)


