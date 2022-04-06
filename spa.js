const cachedPages = [];
const STALE_TIME = 10000;

(function () {
  // Set the initial state in the history when the page loads
  const mainElement = document.querySelector("main");
  if (!mainElement) return console.error("Cannot find <main> element");
  spaURL = mainElement.dataset.spaURL;
  history.replaceState({ spaURL: spaURL }, "", spaURL);
  console.log("Inital state replace", spaURL);
})();

async function spa(spaURL, replace_state = true) {
  spaURL = typeof spaURL === "string" ? spaURL : spaURL.getAttribute("href");

  console.log("Loading SPA page:", spaURL);

  const cachedPage = cachedPages.find((item) => item.url === spaURL);

  let html;

  /* 
    if page is not found in cache or older than stale time, fetch it from the server and save in cache
    else load it from the cache
  */
  if (!cachedPage || Date.now() - cachedPage.cachedAt > STALE_TIME) {
    const response = await fetch(spaURL, { headers: { "From-Fetch": true } });
    html = await response.text();
    console.log("HTML from server", { html: html });

    const newPage = { cachedAt: Date.now(), html: html, url: spaURL };

    if (cachedPage) {
      // if page was previously cached, update it with new cachedAt time and html
      const index = cachedPages.findIndex((x) => x.url == spaURL);
      cachedPages[index] = newPage;
    } else {
      cachedPages.push(newPage);
    }
  } else {
    // using cached page
    html = cachedPage.html;
  }

  if (html.includes("data-spa_modal")) {
    document
      .querySelector(".spa-wrapper")
      .insertAdjacentHTML("afterbegin", html);
  } else {
    document.querySelector(".spa-wrapper").innerHTML = html;
  }

  // When the loaded <main> element is in DOM, replace the document title with the correct one
  mainElement = document.querySelector(`main[data-spa_url="${spaURL}"]`);

  if (replace_state) {
    history.pushState({ spaURL: spaURL }, "", spaURL);
  }

  if (!mainElement) return console.error("Cannot find <main> element");

  spaTitle = mainElement.dataset.spa_title;
  document.title = spaTitle;
}

// Listener for when user navigates the browser with the forward and back buttons
window.addEventListener("popstate", (event) => {
  spa(event.state.spaURL, false);
  return false;
});
