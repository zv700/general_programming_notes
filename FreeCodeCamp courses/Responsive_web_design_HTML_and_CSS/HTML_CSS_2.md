<h2>ORDERED LIST</h2>
<ol></ol> element makes an ordered/numbered list

-each list item needs to be surrounded by <li></li> list item tags

-list items are numbered in the order they are listed

<h3>Top three colors:</h3>
<ol>
<li>blue</li>
<li>green</li>
<li>red</li>
</ol>

=====================
<html>
  <body>
    <main>
    <section>
      <h3>Things that are blue:</h3>
      <ul>
        <li>water</li>
        <li>the sky</li>
        <li>blueberries</li>
      </ul>
      </section>
      <section>
      <h3>The best fruits:</h3>
      <ol>
        <li>strawberries</li>
        <li>cherries</li>
        <li>bananas</li>
      </ol>
      <figure>
        <img src="https://fruitphotos.org/gallery/fruits.jpg" alt="strawberries, cherries, and bananas are sitting on a plate">
        <figcaption>Images of the best fruits</figcaption>
      </figure>
      </section>
    </main>
  </body>
</html>
=====================

<h2>STRONG</h2>
strong=bold
<strong></strong>


<figure>
  <figcaption>Cats <strong>hate</strong> baths.</figcaption>
</figure>


<h2>FORMS(element), ACTION(attribute)</h2>
<form></form>
-Form elements are sections of pages that take user input.

-action attribute <form action=""> indicates where the data from the form will be sent

SEND FORM INFO TO SPECIFIC DIRECTORY OF WEBSITE FILE STRUCTURE:
<form action="/submit-url"></form>
[sends form input info to the 
"/submit-url" directory of your website]

SEND FORM INFO TO SPECIFIC URL:
<form action="https://cookiecutter.com/submit-form"></form>


<h2>INPUT</h2>
<input>
-Inputs allow you to collect data from a web form. <input> defaults to placing a basic text input box on page. Can specify type of input with "type" attribute.

-Inputs <input> are SELF CLOSING, do not need closing tag

-Inputs <input> are nested within forms <form></form>

<form action="https://foodpics.na/acceptfoodpic">
  <input>
</form>

<h2>INPUT(element), TYPE(attribute)</h2>
<input type="text">
[places a text box for inputs]

<h2>INPUT(element), NAME(attribute)</h2>
Input needs to have a NAME attribute to be able to access the data collected. NAME attribute adds an accessable directory within site's file structure. 

For example to access this directory:
"/site/formdata/email"

-use NAME to group data from choices for one question into one directory

-NAME makes it easier for server to process web forms with more than one CHECKBOX

-NAMEs do not show up in front end(on web page), only for back end

name would need to have directory:
<input type="text" name="email">

<h2>INPUT(element), PLACEHOLDER(attribute)</h2>
PLACEHOLDER text gives user an idea of what kind of info to input into the form/text box. <input placeholder="enter email address">

<input type="text" name="email" placeholder="enter email address">

-PLACEHOLDER is grayed out text within text input box that is only displayed when no text is input

<h2>INPUT(element), REQUIRED(attribute)</h2>
REQUIRED prevents user from submitting a form when they have not entered the required info

-REQUIRED does not need to be followed by a value [="value"]

<input required type="text" name="catphotourl" placeholder="cat photo URL">

<input type="text" name="catphotourl" placeholder="cat photo URL" required>

-positioning does not matter as long as there is a space between required and other attributes

<h2>BUTTON (element)</h2>
BUTTON creates a clickable button
<button></button>

<button>Click Here</button>

<input required type="text" name="catphotourl" placeholder="cat photo URL">
<button>Submit</button>

-BUTTON behavior defaults to submitting form to designated location/url in <form action="">

<h2>BUTTON ATTRIBUTES, BEHAVIOR</h2>
-don't rely on default behavior of BUTTON to prevent confusion, use TYPE attribute

<button type="submit">Submit</button>

<input required type="text" name="catphotourl" placeholder="cat photo URL">
<button type="submit">Submit</button>

<h2>RADIO BUTTONS/INPUT</h2>
-RADIO BUTTONS are used when you only want one answer out of multiple choices, multiple choice questions

-RADIO BUTTONS count as an INPUT element, not a BUTTON element

<input type="radio"> Indoor
[displays a circular radio butoon followed by the word Indoor]

<input type="radio">Indoor 
<input required type="text" placeholder="enter your email address">
<button type="submit">Submit</button>
[will display:1. radio button with "Indoor" to the right of it, 2. input text box with placeholder text, 3. Submit button]
[all three elements will be horizontally next to each other in the same line because they are currently inline elements, needs to be specified to change which line each are on]

<h2>LABEL</h2>
-LABEL associates text for an INPUT element with the INPUT element itself
-helps to flag/LABEL an INPUT as an INPUT to allow a screen reader to be able to find INPUTs on a page, screen readers and assistive tech might not be able to find INPUTs without LABELs
-nest INPUTs inside of LABEL element
-each individual INPUT needs to be nested within its own LABEL element

<label></label>

<label><input type="radio">Indoor</label>

<h2>INPUT(element), ID(attribute)</h2>
-ID attribute is used to specify HTML elements

-each ID attribute's value must be unique from other ID values within a page

<label><input id="indoor">Indoor</label>
[the ID:"indoor" specifies this radio button is the "indoor" button, no other radio button or input can also be the "indoor" button]
[if other radio buttons with the word "indoor" exist on the page, they would need different ID values, like <input id="indoor2"> or <input id="indoor3">to specify they are different buttons in different places on the page]

<label><input id="indoor" type="radio">Indoor</label>
<label><input id="outdoor" type="radio">Outdoor</label>
[creates two radio buttons: Indoor to the left, Outdoor to the right]
[both buttons can be selected at the same time]

<h2>MAKE ONLY ONE RADIO BUTTON SELECTABLE AT A TIME</h2>
-to make only one RADIO INPUT selectable at one time, all radio inputs for one question need to have THE SAME NAME ATTRIBUTE

MORE THAN ONE SELECTABLE:
<label><input id="indoor" type="radio">Indoor</label>
<label><input id="outdoor" type="radio">Outdoor</label>

ONLY ONE SELECTABLE:
<label><input id="indoor" type="radio" name="indoor-outdoor">Indoor</label>
<label><input id="outdoor" type="radio" name="indoor-outdoor">Outdoor</label>

-NAME attribute is being used to specify/group together choices for one multiple-choice question

<h2>INPUT(element), VALUE(attribute)</h2>
-without VALUE attribute, submitted form data from each RADIO INPUTS will default to include "indoor-outdoor=on" [from NAME]

Example without VALUE specified: 
1. select "RADIO indoor" and hit submit BUTTON: form data will submit as "indoor-outdoor=on"
2. select "RADIO outdoor" and hit submit BUTTON: form data will ALSO submit as "indoor-outdoor=on"

-VALUE specifies what data will be submited if a specific RADIO button is selected

-even though RADIO buttons may have be named differently, their name will not affect what data is submitted, by default all choices lead to the same outcome

Diagram (pathway with VALUEs unspecified, default pathway):
1--------\
2------------------->
3--------/
[all RADIO choices converge/lead to same outcome, default to the same value]

Diagram (pathway with VALUEs specified):
1----------------->
2----------------->
3----------------->
[each RADIO choice leads to different outcome]

<label><input id="indoor" type="radio" name="indoor-outdoor" valut="indoor"> Indoor</label>
          <label><input id="outdoor" type="radio" name="indoor-outdoor" value="outdoor"> Outdoor</label>
[VALUEs specified, indoor RADIO will now submit "indoor" and outdoor RADIO will now submit "outdoor"]

<h2>FIELDSET(element)</h2>
-FIELDSET element groups related inputs and labels together in a web form

-FIELDSET elements are BLOCK-LEVEL ELEMENTS which means they appear on a new line

-nest INPUT elements and corresponding LABELs within FIELDSET element

<fieldset>
  <label><input id="indoor" type="radio" name="indoor-outdoor" value="indoor">Indoor</label>
  <label><input id="outdoor" type="radio" name="indoor-outdoor" value="outdoor">Outdoor</label>
</fieldset>

-elements within one FIELDSET are grouped into a boxed space on the page

<h2>LEGEND(element)</h2>
LEGEND is the caption for the FIELDSET element

-gives users context for what info needs to be entered within the FIELDSET form

<fieldset>
  <legend>What color are your eyes?</legend>
  <label><input type="radio"> brown</label>
  <label><input type="radio"> blue</label>
</fieldset>

<h2>INPUT(element), CHECKBOX(attribute)</h2>

<fieldset>
  <legend>What type of bags do you prefer?</legend>
  <input type="checkbox"> paper
  <input type="checkbox"> plastic
</fieldset>
[THERE SHOULD BE A SPACE BETWEEN ">" AND THE OPTION/WORD TO ITS RIGHT, even though it will display correctly without the space.]

<fieldset>
  <legend>What type of bags do you prefer?</legend>
  <label><input id="paper" type="checkbox"> paper</label>
  <label><input id="plastic" type="checkbox"> plastic</label>
</fieldset>

<h2>LABEL(element), FOR(attribute)</h2>
-FOR is used to associate an element's text with the element itself from within a LABEL ELEMENT

-ID attibute within INPUT should be the same as FOR attribute within LABEL, ID=FOR

-for this method, nest text associated with CHECKBOX INPUT within LABEL ELEMENT

WITHOUT "FOR":
<input id="paper"  type="checkbox"> Paper

WITH "FOR":
<input id="paper"  type="checkbox"> <label for="paper">Paper</label>

^^^works the same as:
<label><input id="paper"  type="checkbox"> Paper</label>

=======================
<html>
  <body>
    <main>
      <h4>Cat personalities questionaire</h4>
      <fieldset>
        <legend>What personalities do you prefer in cats?</legend>
        <input checked id="loving" type="checkbox" name="personality"  value="loving"> <label for="loving">Loving</label>
        <input id="lazy" type="checkbox" name="personality"  value="lazy"> <label for="lazy">Lazy</label>
        <input id="energetic" type="checkbox" name="personality" value="energetic"> <label for="energetic">Energetic</label>
      </fieldset>
    </main>
  </body>
</html>
====================

<h2>INPUT(element), CHECKED(attribute)</h2>
CHECKED attribute makes an INPUT choice checked by default

<input checked type="checkbox">

<input checked type="radio">


<h2>FOOTER(element)</h2>
FOOTER element comes after/below MAIN element's closing tag

<html>
  <body>
    <main>
    </main>
    <footer>
      <p>Copyright - <a href="https://poopybutthead.org">Poopybutthead.org</a>, all rights reserved</p>
    </footer>
  </body>
</html>

<h2>BODY(element)</h2>
-most page content, ELEMENTs, should be within BODY
<body>
</body>

<h2>HEAD(element), TITLE(element)</h2>
-page TITLE goes within HEAD

<html>
  <head>
    <title>CatPhotoApp</title>
  </head>
    <body>
    </body>
  <footer>
  </footer>
</html>


<h2>HTML(element), LANG(attribute)</h2>

-HTML is top-most element, all other elements must be DECENDANTS[lower in priority] of HTML element

-LANG attribute goes within HTML element

<html lang="en">
</html>

en=English

<h2>DECLARATION(special string), HTML(element)</h2>
-all pages should begin with DECLARATION string to ensure the browser tries to meet industry-wide specifications when loading the web page

<!DOCTYPE html>
<html lang="en">
</html>

"<!DOCTYPE html>" IS THE ENTIRE DECLARATION AND SHOULD APPEAR ON ITS OWN LINE ABOVE <html>

<h2>HEAD(element), META(element)</h2>
-META element nested within HEAD

-META elements are SELF-CLOSING

<head>
  <meta charset="UTF-8">
  <title>CatPhotoApp</title>
</head>

-^^^META CHARSET tells browser to use the UTF-8 character set so the web page's data/markup can be parsed/processed into multiple languages. 

-markup=the process of using tags/elements to alter text in specific ways [example: <strong> makes text bold]

