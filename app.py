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
  is_fetch = True if request.headers.get('From-Fetch') else False
  return dict(title="Home page", is_fetch=is_fetch)

##############################
@get("/one")
@view("one")
def _():
  is_fetch = True if request.headers.get('From-Fetch') else False
  return dict(title="One is One", is_fetch=is_fetch)


##############################
@get("/two")
@view("two")
def _():
  is_fetch = True if request.headers.get('From-Fetch') else False
  return dict(title="Two is two", is_fetch=is_fetch)

##############################
@get("/items/<item_id>")
@view("item")
def _(item_id):
  is_fetch = True if request.headers.get('From-Fetch') else False
  page_title = f"Title Item {item_id}"

  return dict(title=page_title, is_fetch=is_fetch, item_id=item_id)

##############################
@error(404)
@view("404")
def _(error):
  return

##############################
run(host="127.0.0.1", port=80, debug=True, reloader=True)














































