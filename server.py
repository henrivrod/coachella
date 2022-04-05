#!/usr/bin/env python

"""
Columbia's COMS W4111.003 Introduction to Databases
Example Webserver

To run locally:

    python server.py

Go to http://localhost:8111 in your browser.

A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""

import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)


#
# The following is a dummy URI that does not connect to a valid database. You will need to modify it to connect to your Part 2 database in order to use the data.
#
# XXX: The URI should be in the format of: 
#
#     postgresql://USER:PASSWORD@104.196.152.219/proj1part2
#
# For example, if you had username biliris and password foobar, then the following line would be:
#
#     DATABASEURI = "postgresql://biliris:foobar@104.196.152.219/proj1part2"
#
DATABASEURI = "postgresql://eh2889:coachella@35.211.155.104/proj1part2"


#
# This line creates a database engine that knows how to connect to the URI above.
#
engine = create_engine(DATABASEURI)

#
# Example of running queries in your database
# Note that this will probably not work if you already have a table named 'test' in your database, containing meaningful data. This is only an example showing you how to run queries in your database using SQLAlchemy.
#
engine.execute("""CREATE TABLE IF NOT EXISTS test (
  id serial,
  name text
);""")
engine.execute("""INSERT INTO test(name) VALUES ('grace hopper'), ('alan turing'), ('ada lovelace');""")


@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request 
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request.

  The variable g is globally accessible.
  """
  try:
    g.conn = engine.connect()
  except:
    print("uh oh, problem connecting to database")
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't, the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass


#
# @app.route is a decorator around index() that means:
#   run index() whenever the user tries to access the "/" path using a GET request
#
# If you wanted the user to go to, for example, localhost:8111/foobar/ with POST or GET then you could use:
#
#       @app.route("/foobar/", methods=["POST", "GET"])
#
# PROTIP: (the trailing / in the path is important)
# 
# see for routing: http://flask.pocoo.org/docs/0.10/quickstart/#routing
# see for decorators: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
#
@app.route('/')
def index():
  """
  request is a special object that Flask provides to access web request information:

  request.method:   "GET" or "POST"
  request.form:     if the browser submitted a form, this contains the data in the form
  request.args:     dictionary of URL arguments, e.g., {a:1, b:2} for http://localhost?a=1&b=2

  See its API: http://flask.pocoo.org/docs/0.10/api/#incoming-request-data
  """

  # DEBUG: this is debugging code to see what request looks like
  print(request.args)


  #
  # example of a database query
  #
  cursor = g.conn.execute("SELECT name FROM test")
  names = []
  for result in cursor:
    names.append(result['name'])  # can also be accessed using result[0]
  cursor.close()

  #
  # Flask uses Jinja templates, which is an extension to HTML where you can
  # pass data to a template and dynamically generate HTML based on the data
  # (you can think of it as simple PHP)
  # documentation: https://realpython.com/blog/python/primer-on-jinja-templating/
  #
  # You can see an example template in templates/index.html
  #
  # context are the variables that are passed to the template.
  # for example, "data" key in the context variable defined below will be 
  # accessible as a variable in index.html:
  #
  #     # will print: [u'grace hopper', u'alan turing', u'ada lovelace']
  #     <div>{{data}}</div>
  #     
  #     # creates a <div> tag for each element in data
  #     # will print: 
  #     #
  #     #   <div>grace hopper</div>
  #     #   <div>alan turing</div>
  #     #   <div>ada lovelace</div>
  #     #
  #     {% for n in data %}
  #     <div>{{n}}</div>
  #     {% endfor %}
  #
  context = dict(data = names)

  
  


  #
  # render_template looks in the templates/ folder for files.
  # for example, the below file reads template/index.html
  #
  return render_template("index.html", **context)

#
# This is an example of a different path.  You can see it at:
# 
#     localhost:8111/another
#
# Notice that the function name is another() rather than index()
# The functions for each app.route need to have different names
#
@app.route('/another')
def another():
  return render_template("another.html")

@app.route('/tickets')
def tickets():
  # DEBUG: this is debugging code to see what request looks like
  print(request.args)

  cursor = g.conn.execute("SELECT ticket_type, purchaser_name, purchaser_age FROM ticket ORDER BY ticket_type")
  tickets = []
  for result in cursor:
    tickets.append(result)  # can also be accessed using result[0]
  cursor.close()

  context = dict(data = tickets)

  return render_template("tickets.html", **context)

@app.route('/stages')
def stages():
  # DEBUG: this is debugging code to see what request looks like
  print(request.args)

  cursor = g.conn.execute("SELECT stage_id, stage_name FROM stage")
  stages = []
  for result in cursor:
    stages.append(result)  # can also be accessed using result[0]
  cursor.close()

  cursor = g.conn.execute("SELECT COUNT(DISTINCT artist_id) FROM artist")
  for result in cursor:
    length = result
  cursor = g.conn.execute("SELECT song_name, artist_id FROM song")
  songs = []
  for i in range(length):
    songs.append([])
  for result in cursor:
    songs[result.artist_id].append(result)  # can also be accessed using result[0]
  cursor.close()

  cursor = g.conn.execute("SELECT artist_id,artist_name, set_start_time, set_end_time, stage_id, set_day FROM artist ORDER BY set_start_time")
  friday = [[],[],[],[],[],[],[]];
  saturday = [[],[],[],[],[],[],[]];
  sunday = [[],[],[],[],[],[],[]];
  for result in cursor:
    if (result.set_day=="Friday"):
      friday[result.stage_id-1].append(result)
    if (result.set_day=="Saturday"):
      saturday[result.stage_id-1].append(result)
    if (result.set_day=="Sunday"):
      sunday[result.stage_id-1].append(result)
  cursor.close()

  context = dict(stages = stages, friday=friday, saturday=saturday, sunday=sunday, songs=songs)

  return render_template("stages.html", **context)


@app.route('/merch')
def merch():
  print(request.args)
  cursor = g.conn.execute("SELECT m.tent_id, m.number_of_workers, s.stage_name FROM merch_tent m, stage s where m.stage_id = s.stage_id")
  tents = []
  for result in cursor:
    tents.append(result)  # can also be accessed using result[0]
  cursor.close()

  print(request.args)
  cursor = g.conn.execute("SELECT item_id, tent_id, item_name, item_type, number_remaining, price FROM merch_item order by tent_id")
  items = []
  for result in cursor:
    items.append(result)  # can also be accessed using result[0]
  cursor.close()

  context = dict(tent_info = tents, item_info = items)

  return render_template("merch.html", **context)

@app.route('/stand/<id>')
def stand(id=0):
  print(request.args)
  cursor = g.conn.execute("SELECT s.stand_name, c.area_name FROM stand s, concession_area c where c.area_id = s.area_id AND s.stand_id="+str(id))
  stand = []
  for result in cursor:
    stand.append(result)  # can also be accessed using result[0]
  cursor.close()

  cursor = g.conn.execute("SELECT dish_name, price, item_type FROM dish where stand_id="+str(id))
  dish = []
  for result in cursor:
    dish.append(result)  # can also be accessed using result[0]
  cursor.close()

  context = dict(stand_info = stand, dishes = dish)

  return render_template("stand.html", **context)



@app.route('/food')
def food():
  print(request.args)
   

  cursor = g.conn.execute("SELECT area_name, area_id FROM concession_area")
  area_names = []
  for result in cursor:
    area_names.append(result)
    """
    if result['area_id'] in concessiondata:
      concessiondata[result['area_id']].append(result['area_name'])  # can also be accessed using result[0]
    else:
      concessiondata[result['area_id']] = [result['area_name']]
      """
  cursor.close()

  
  cursor = g.conn.execute("SELECT s.stage_name, c.area_id FROM stage s, concession_area c WHERE s.stage_id = c.stage_id")
  stage_names = []
  for result in cursor:
    stage_names.append(result)
    #concessiondata[result['area_id']].append(result['stage_name'])  # can also be accessed using result[0]
  cursor.close()

  cursor = g.conn.execute("SELECT s.stand_name, s.area_id, s.stand_id FROM stand s order by s.area_id")
  stand_names= []
  for result in cursor:
    stand_names.append(result)  # can also be accessed using result[0]
  cursor.close()
  
  context = dict(area_name = area_names, stage_name = stage_names, stand_name=stand_names)

  return render_template("food.html", **context)

# Example of adding new data to the database
@app.route('/add_data')
def add_data():
  return render_template("add_data.html")

@app.route("/add_merch")
def add_merch():
  return render_template("add_merch.html")

@app.route("/add_food")
def add_food():
  return render_template("add_food.html")

@app.route("/add_tent", methods=['POST'])
def add_tent():
  
  tentid = request.form['tent_identry']
  stageid = request.form['stage_identry']
  numworkers = request.form['num_workersentry']
  g.conn.execute('INSERT INTO merch_tent (tent_id, stage_id, number_of_workers) VALUES (%s, %s, %s)', tentid, stageid, numworkers)
  return redirect('/')

@app.route("/add_item", methods=['POST'])
def add_item():
  itemid = request.form['item_identry']
  tentid = request.form['item_tentidentry']
  itemname = request.form['item_nameentry']
  itemtype = request.form['merchitemtype']
  numrem = request.form['num_remainingentry']
  price = request.form['price_entry']
  print(itemtype)
  g.conn.execute('INSERT INTO merch_item (item_id, tent_id, item_name, item_type, number_remaining, price) VALUES (%s, %s, %s, %s, %s, %s)', itemid, tentid, itemname, itemtype, numrem, price)
  return redirect('/')

@app.route("/add_concession", methods=['POST'])
def add_concession():
  
  areaid = request.form['area_identry']
  stageid = request.form['con_stage_identry']
  areaname = request.form['area_nameentry']
  numstand = request.form['num_standsentry']
  g.conn.execute('INSERT INTO concession_area (area_id, stage_id, area_name, number_of_stands) VALUES (%s, %s, %s, %s)', areaid, stageid, areaname, numstand)
  return redirect('/')

@app.route("/add_dish", methods=['POST'])
def add_dish():
  
  dishid = request.form['dish_identry']
  standid = request.form['dish_stand_identry']
  dishname = request.form['dish_nameentry']
  dishprice = request.form['dish_priceentry']
  dishitemtype = request.form['dish_item_typeentry']
  g.conn.execute('INSERT INTO merch_item (dish_id, stand_id, dish_name, price, item_type) VALUES (%s, %s, %s, %s, %s)', dishid, standid, dishname, dishprice, dishitemtype)
  return redirect('/')

@app.route("/add_stand", methods=['POST'])
def add_stand():
  
  standid = request.form['stand_identry']
  areaid = request.form['stand_areaidentry']
  standname = request.form['stand_nameentry']
  g.conn.execute('INSERT INTO stand (stand_id, area_id, stand_name) VALUES (%s, %s, %s)', standid, areaid, standname)
  return redirect('/')

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()


if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using:

        python server.py

    Show the help text using:

        python server.py --help

    """

    HOST, PORT = host, port
    print("running on %s:%d" % (HOST, PORT))
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)


  run()
