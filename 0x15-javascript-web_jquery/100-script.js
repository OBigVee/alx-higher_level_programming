/**
 * 
 * a JavaScript script that updates the text color of the <header> element to red (#FF0000):
 * -> You must use document.querySelector to select the HTML tag
 * -> You can’t use the jQuery API
 * -> Note: Your script must be imported from the <head> tag, not at the end of the HTML
 */
'use strict'
window.addEventListener('load', () => {
    document.querySelector('header').style.color = '#FF0000'
});