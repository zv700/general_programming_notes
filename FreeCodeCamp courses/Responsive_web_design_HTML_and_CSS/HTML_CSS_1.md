<h2>HEADINGS</h2>
1. h1 through h6
2. lower numbers have higher importance and size
3. only use h1 once per page
<h1>example heading 1</h1>
<h6>example heading 6</h6>

<h2>PARAGRAPH</h2>
-use to indicate non-title/non-heading text on page
<h3>Today's weather</h3>
<p>The air is cold today. The ground is dry. Visibility is clear with a light breeze.</p>

<h2>COMMENTING</h2>
1. use comments to make sections of code inactive (not visible on final page)
2. use comments to leave notes in code
<!-- example comment -->

<!-- TODO: buy socks -->
<p>paragraph</p>
--------------------------------

<h1>HTML5 ELEMENTS:</h1>
-used to identify content areas

<h2>MAIN</2>
<main></main>

<main>
<h1>example title</h2>
<h2>example heading</h2>
<!-- TODO: add another example -->
<p>example paragraph for the purpose of explaining</p>
</main>


<h2>NESTING</h2>
1. "nested elements should be placed two spaces further to the right of the element they are nested in"
2. example: if "MAIN" is the nest, then anything between <main> and </main> is a nested element
3. editing program may automatically indent nested elements, so manual spaces may not be needed

<main>
    <h1>nested h1</h2>
    <h2>nested h2</h2>
    <!-- TODO: add notes -->
	<p>yes yes yes</p>
</main>

<main>
	<h1>yes</h1>
</main>

<h1>IMAGES</h1>
1. <img> element HAS an opening tag BUT DOES NOT HAVE a closing tag
2. <img> element is a SELF CLOSING TAB 

<p>example paragraph</p>
<img>

<h1>HTML ATTRIBUTES</h1>
-words used inside of opening tag of an element to control the element's behavior

<h1>SRC attribute</h1>
"src" attribute is used to indicate an image's location URL [Source?]
<img src="">

<img src="https://www.example.com/the-image.jpg">

<h1>ALT attribute</h1>
<img src="" alt=""> attribute applies text for screen reader programs to read out loud, used for accesibility, will display text if an image fails to load

=============================
<html>
  <main>
    <body>
      <h1>CatPhotoApp</h1>
	  <h2>Cat Photos</h2>
<!-- TODO: add cat photos -->
      <p>Send us your cat photos. Submitted cat photos below:</p>
      <img src=https://www.example.com/the-image.jpg" alt="an image of a cat lying on its back">
    </main>
  </body>
</html>
==============================

<h1>ANCHOR element</h1>
anchor element: <a> is used to link another page. 
[href=""] indicates link to page [html/https/hyperlink reference]
<a> needs closing tag </a>

<a href=' '></a>
<a href=" "></a>
[can surround link in apostrophes ' ' or quotation marks " ", should work either way]

<a href='https://freecatphotoapp.com'></a>

<h1>ANCHOR TEXT</h1>
hyperlink text can be placed between opening tag <a> and closing tag </a> of an anchor element link
<a href="">link text</a>

<a href="https://freecatphotoapp.com">Your cat photos here</a>

<h1>ANCHOR LINKS WITHIN PARAGRAPHS</h1>
anchor element links/hyperlinks can be added to words within paragraphs by surrounding desired words with anchor tags

BEFORE:
<p>This is a link to cat photos.</p>
AFTER:
<p>This is a <a href=https://freecatphotoapp.com>link to cat photos.</a>

<h1>SET ANCHOR LINKS TO OPEN A NEW TAB</h1>
target attribute within anchor element opens a new tab when target is set to "_blank"

<a target="_blank">


<p>Take a look at our cat <a target="_blank" href="https://catphotobook.com">photo book.</a></p>

<h1>MAKING IMAGES INTO CLICKABLE LINKS WITH img AND anchor</h1>
surround the image src with anchor element tags

IMAGE:
<img src="https://catphoto.org/gallery/angrycat.jpg">

IMAGE AS A LINK:
<a href="catphotobook.com"><img src="https://catphoto.org/gallery/angrycat.jpg"></a>

IMAGE AS A LINK THAT OPENS IN NEW TAB:
<a target="_blank" href="catphotobook.com"><img src="https://catphoto.org/gallery/angrycat.jpg"></a>

<h1>SECTION</h1>
use <section></section> to seperate old content from new content on the same page

BEFORE:
<main>
<h1>Title</h1>
<h2>smaller title</h2>
<p>Example paragraph text goes here.</p>
<a href="https://catphotos.com"><img src="https://images.google.com/gallery/deeznutz.jpg" alt="an image of Deez Nutz holding a fluffy cat"></a>
</main>

AFTER:
<main>
<h1>Title</h1>
<section>
<h2>smaller title</h2>
<p>Example paragraph text goes here.</p>
<a href="https://catphotos.com"><img src="https://images.google.com/gallery/deeznutz.jpg" alt="an image of Deez Nutz holding a fluffy cat"></a>
</section>
<section>
<h2>New content title</h2>
<p>New content goes here</p>
</section>
</main>

<h1>LOWER RANKING HEADING ELEMENTS</h1>
-adding a lower rank heading to a page implies you're starting a new subsection

<main>
  <section>
    <h2>Higher rank heading 1rst subsection</h2>
  </section>
  <section>
    <h3>Lower rank heading 2nd subsection</h3>
  </section>
</main>

UNORDERED LIST
open and close unordered list <ul> and </ul>, each list item needs to be nested/surrounded by <li></li> [list item]
<ul></ul>

<ul> 
  <li>cats</li> 
  <li>dogs</li> 
  <li>rabbits</li>
</ul>


=====================
<html>
  <body>
    <main>
      <section>
      <h1>Cat page</h1>
      <h2>Things cats like:</h2>      
      <ul>
        <li>naps</li>
        <li>food</li>
        <li>laser pointers</li>
      </ul>
      </section>
    </main>
  </body>
</html>
====================

<h1>FIGURE</h1>
<figure></figure> element represents self-containted content and allows you to associate an image with a caption

<figure>
  <img src="http://twitch.tv/content/poopie.jpg" alt="A piece of poop sitting unflushed in a toilet">
</figure>

<h1>FIGCAPTION</h1>
<figcaption></figcaption> element adds a caption to describe the image within <figure></figure>

-<figcaption></figcaption> is nested within <figure></figure>

<figure>
  <img src="https://smallanimalsonheads.org/categories/kittenonwomanshead.jpg" alt="A small orange kitten is sitting on a woman's head">
  <figcaption>Kittens are lightweight and can balance easily on people's heads.  </figcaption>
</figure>

EMPHASIZE TEXT
Use <em></em> element to put words in italics

<figcaption>Kittens are <em>small</em> animals.</figcaption>

<h1>ORDERED LIST</h1>
