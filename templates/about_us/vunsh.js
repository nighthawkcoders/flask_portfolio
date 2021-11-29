const button = document.getElementById("music-button");
  const frame = document.getElementById("songFrame");
  const choices = [ "<iframe src="https://open.spotify.com/embed/track/3yk7PJnryiJ8mAPqsrujzf?utm_source=generator&theme=0" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>",
                    "<iframe src="https://open.spotify.com/embed/track/1s9DTymg5UQrdorZf43JQm?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>",
                    "<iframe src="https://open.spotify.com/embed/track/3cWmqvMwVQKDigWLSZ3w9h?utm_source=generator&theme=0" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>",
                    "<iframe src="https://open.spotify.com/embed/track/5hVghJ4KaYES3BFUATCYn0?utm_source=generator&theme=0" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>",
                    "<iframe src="https://open.spotify.com/embed/track/5B0kgjHULYJhAQkK5XsMoC?utm_source=generator&theme=0" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>",
                    "<iframe src="https://open.spotify.com/embed/track/5TxRUOsGeWeRl3xOML59Ai?utm_source=generator&theme=0" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>",
                    "<iframe src="https://open.spotify.com/embed/track/4EWBhKf1fOFnyMtUzACXEc?utm_source=generator" width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>"
                    ]

function updateSong(){
    alert('e')
    const songChoice = choices[Math.floor(Math.random() * choices.length)]
    frame.innerHtml(songChoice)
    alert('lol')

}
button.addEventListener("click", alert('e'));

