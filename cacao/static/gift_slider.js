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

  // Auto-scroll slides every 3 seconds
  setInterval(scrollSlides, 2000);

  // Enable mouse scroll on .scroll_it element
  scrollIt.addEventListener('wheel', function(e) {
    e.preventDefault();
    if (e.deltaY < 0) {
      this.scrollLeft -= 100;
    } else {
      this.scrollLeft += 100;
    }
  });
});