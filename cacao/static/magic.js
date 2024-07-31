const numStars = 150; // Number of stars
    const stars = document.getElementById('magics');

    for (let gli = 0; gli < numStars; gli++) {
        const magic = document.createElement('div');
        magic.className = 'magic';
        magic.style.top = Math.floor(Math.random() * 100) + '%';
        magic.style.left = Math.floor(Math.random() * 100) + '%';
        magic.style.animationDelay = Math.random() + 's';
        magics.appendChild(magic);
    }
