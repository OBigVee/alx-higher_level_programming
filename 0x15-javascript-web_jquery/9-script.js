'use strict';
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$(()=>{
    $.get(url, (body)=>{
        $('div#hello').html(body.hello);
    });
});
