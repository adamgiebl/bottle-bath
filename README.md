<img src="https://adamgiebl.github.io/adamgiebl/bottle-bath.svg" width="300"/>

# Bottle Bath

Single page app in python Bottle.
This repo is an example of the usage of the `spa.js` library. The example includes routing for normal pages, modal pages with a closing functionality, caching, and a 404 error page.

This fork is a bit simplified/modified version of the forked repository.

# How to use

Import `spa.js` at the end of your body element. Don’t forget to serve it with Bottle.

```html
<script src="/spa.js"></script>
```

Modify your routes so that they include this code. You can pass any variables to the template as usual but you have to include `is_fetch`.

```python
@get("/one")
@view("one")
def _():
  is_fetch = True if request.headers.get('From-Fetch') else False
  return dict(title="One is One", is_fetch=is_fetch)
```

Include a `<div>` element with the class `spa-wrapper` at the end of your header template and the closing `</div>` tag at the start of your footer template (example in repo).

Modify your navigation links so that they have this onclick listener:

```html
<nav>
  <a href="/" onclick="spa(this); return false">Home</a>
  <a href="/one" onclick="spa(this); return false">One</a>
  <a href="/two" onclick="spa(this); return false">Two</a>
</nav>
```

In your page templates, you need to optionally include the header and the footer depending on the `is_fetch` variable. Page template also has to be wrapped in the `<main>` element with the following data attributes:

- `data-spa_url` - URL of the page, should match the one in your Bottle route
- `data-spa_title` - The title of the page, it will be used as `document.title`

Pages should generally look like this:

```html
% if not is_fetch:
  % include("header")
% end

<main
  data-spa_url="/one"
  data-spa_title="{{title}}"
>
  <h1>One</h1>
</main>

% if not is_fetch:
  % include("footer")
% end
```

For an example of modal pages look at `views/item.html`

## Caching

The library is caching pages by default. This means that when you visit a page for the first time, it will fetch the HTML from the server and add that page to the cache so that when you visit it for the second time it doesn’t need to contact the server for it. There is a limit to how long pages will be cached and that’s because when you have a page that has dynamic content the user should get the new version from the server again after some time.

You can change this limit with the `STALE_TIME` variable at the top of `spa.js` file. By default, it caches pages for 10 seconds (10000ms). If you have pages that never change content you might want to set the `STALE_TIME` to `Infinity`.
