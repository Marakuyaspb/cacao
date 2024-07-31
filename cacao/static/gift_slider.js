document.addEventListener('DOMContentLoaded', function() {
  // Set initial position for animation
  let position = 0;
  const scrollIt = document.querySelector('.scroll_it');

  // Function to animate the scrolling of slides
  function scrollSlides() {
    scrollIt.scrollTo({
      left: position,
      behavior: 'smooth'
    });
    position += 400; // Increment position for next animation
    if (position > scrollIt.scrollWidth - scrollIt.clientWidth) {
      position = 0; // Reset position to start over
    }
  }

  setInterval(scrollSlides, 2000);

  scrollIt.addEventListener('wheel', function(e) {
    e.preventDefault();
    if (e.deltaY < 0) {
      this.scrollLeft -= 100;
    } else {
      this.scrollLeft += 100;
    }
  });
});




document.addEventListener('DOMContentLoaded', function() {
  // Set initial position for animation
  let positionR = 0;
  const scrollItR = document.querySelector('.scroll_res');

  // Function to animate the scrolling of slides
  function scrollSlidesR() {
    scrollItR.scrollTo({
      left: positionR,
      behavior: 'smooth'
    });
    positionR += 400; // Increment position for next animation
    if (positionR > scrollItR.scrollWidth - scrollItR.clientWidth) {
      positionR = 0; // Reset position to start over
    }
  }

  setInterval(scrollSlidesR, 2000);

  scrollItR.addEventListener('wheel', function(e) {
    e.preventDefault();
    if (e.deltaY < 0) {
      this.scrollLeft -= 100;
    } else {
      this.scrollLeft += 100;
    }
  });
});



document.addEventListener('DOMContentLoaded', function() {
  // Set initial position for animation
  let positionP = 0;
  const scrollP = document.querySelector('.scroll_popular');

  // Function to animate the scrolling of slides
  function scrollSlidesP() {
    scrollP.scrollTo({
      left: positionP,
      behavior: 'smooth'
    });
    positionP += 400; // Increment position for next animation
    if (positionP > scrollP.scrollWidth - scrollP.clientWidth) {
      positionP = 0; // Reset position to start over
    }
  }

  setInterval(scrollSlidesP, 2000);

  scrollP.addEventListener('wheel', function(ev) {
    ev.preventDefault();
    if (ev.deltaY < 0) {
      this.scrollLeft -= 100;
    } else {
      this.scrollLeft += 100;
    }
  });
});