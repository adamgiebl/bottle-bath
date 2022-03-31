from bottle import error, get, post, request, response, run, static_file, view

##############################
@get("/app.css")
def _():
  return static_file("app.css", root=".")

##############################
@get("/spa.js")
def _():
  return static_file("spa.js", root=".")

##############################
@get("/")
@view("index")
def _():
  is_xhr = True if request.headers.get('spa') else False
  return dict(title="APP", is_xhr=is_xhr)

##############################
@get("/one")
@view("one")
def _():
  print(list(request.headers))
  is_xhr = True if request.headers.get('spa') else False
  return dict(title="One is One", is_xhr=is_xhr)


##############################
@get("/two")
@view("two")
def _():
  is_xhr = True if request.headers.get('spa') else False
  return dict(title="Two is two", is_xhr=is_xhr)

##############################
@get("/items/<item_id>")
@view("item")
def _(item_id):
  is_xhr = True if request.headers.get('spa') else False
  page_title = f"Itemxxx {item_id}"
  print(type(page_title))
  print(page_title)
  return dict(title=f"Itemxxx {item_id}", is_xhr=is_xhr, item_id=item_id)

##############################
@error(404)
def _(error):
  return "error"

##############################
run(host="127.0.0.1", port=80, debug=True, reloader=True)














































