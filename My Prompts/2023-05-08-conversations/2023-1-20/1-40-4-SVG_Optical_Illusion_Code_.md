## USER
Write an optical illusion in SVG code please.

## ASSISTANT
Here is an example of an optical illusion in SVG code that creates the illusion of a spinning spiral:
```html
<svg width="200" height="200">
  <rect width="100%" height="100%" fill="#fff"/>
  <path d="M100,100 L150,25 A25,25 0 0,1 145,75 Z" fill="none" stroke="#000" stroke-width="5"/>
  <path d="M100,100 L50,175 A25,25 0 0,1 55,125 Z" fill="none" stroke="#000" stroke-width="5"/>
  <animateTransform attributeName="transform" type="rotate" from="0 100 100" to="360 100 100" dur="5s" repeatCount="indefinite"/>
</svg>
```
This code creates a white rectangle that serves as the background, two black spiral shapes that overlap in the center, and an animation that rotates the entire image 360 degrees every 5 seconds. This creates the illusion of a spinning spiral.
