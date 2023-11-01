            // if statement: "before running any other code, go to local storage, try to get 'counter' -> if there is NOT a value in local storage for 'counter' execute the following code"
            // if there is NOT a value in local storage for 'counter' then set a value for 'counter
            // ! exclamation point means "not"
            if (!localStorage.getItem('counter')) {
                localStorage.setItem('counter', 0);  //-> set the VALUE for KEY: 'counter' equal to 0 zero
            }
            //let counter = 0;

            function count() {
                let counter = localStorage.getItem('counter'); // set the VARIABLE: counter's value equal to the 'counter' KEY's value which is stored in local storage
                // counter = counter + 1;       // lines that begin with // are commented out in JavaScript
                // counter += 1;
                counter++;
                document.querySelector('h1').innerHTML = 'Current count: '+counter;
                localStorage.setItem('counter', counter); // set the KEY's value for 'counter' equal to the variable: counter's value after incrementing by 1

                if (counter % 10 === 0) {
                    //alert(`Count is now ${counter}`);
                    //displays an alert when the counter reaches a number that is a multiple of 10 [10, 20, 30, etc.]
                }
            }
            // wait until all of the page is loaded, until the DOM is fully loaded, before running the contained function
            document.addEventListener('DOMContentLoaded', function() {
                const currentcount = 'Current count: ';
                document.querySelector('h1').innerHTML = currentcount+localStorage.getItem('counter'); // updates starting value after refreshing page to the stored value, would start from 0 every time otherwise --> in counters5-.html starting value for h1 is set to text+0 --> CANNOT concatenate strings + variable within .getItem inputs
                document.querySelector('button').onclick = count;
                //document.querySelector('button').addEventListener('click', count); //works same as above line -> "when the click event happens, run the count function"
            
                //setInterval(count, 1000);
            });
            
            // Above: event listener --> listens for button click event/activates code when specified event happens "onclick"
            // find the button on page, access its onclick property, set the value of the onclick property to count
            // not actually calling the count function --> count() function ONLY runs when the button click event happens
            // would need to be more specific than just 'button' when selecting if there is more than one button on the page
            