// Custom CSS
import '../scss/styles.scss';

// jQuery
import $ from 'jquery';
window.jQuery = $;
window.$ = $;

// Functions
import * as myFunctions from './functions';

Object.keys(myFunctions).forEach(key => {
    window[key] = myFunctions[key];
});
