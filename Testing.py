from flask import Flask, render_template, request, send_from_directory, send_file
import pygal
import os

#PYGAL STATIC MAP STUFF
world_map =  pygal.maps.world.SupranationalWorld()

world_map.title = 'UnEarth'
  
world_map.add('Africa', [('africa')])
world_map.add('North america', [('north_america')])
world_map.add('Oceania', [('oceania')])
world_map.add('South america', [('south_america')])
world_map.add('Asia', [('asia')])
world_map.add('Europe', [('europe')])
world_map.add('Antartica', [('antartica')])
world_map.render_to_file('Map.svg')

#FLASK STUFF

svg_code = None

app = Flask(__name__)

country_clicked = None

def on_country_click_handler(country_code):
        global selected_country
        selected_country = country_code
        print("You clicked on {}".format(country_code))

@app.route('/unearth')
def index():
    filename = 'Map.svg'
    world_map.render_to_file(filename)
    world_map.on_country_click = on_country_click_handler
    return send_from_directory(os.getcwd(), filename)

@app.route('/')
def about():
    return render_template("about.html")

@app.route('/about')
def about_me():
    return render_template("about_me.html")

@app.route('/click')
def handle_click():
    x = request.args.get('x')
    y = request.args.get('y')
    # Do something with x and y, e.g. look up the country at those coordinates
    # and return a response
    return "You clicked at x={}, y={}".format(x, y)


@app.route('/send_map')
def send_map():
    return send_file('Map.svg', mimetype='image/svg+xml')



if __name__ == '__main__':
    app.run(debug=True)

