'use strict';
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$(()=>{
    const view = $('div#hello');
    $.ajax({
        url:url,
        method:'GET',
        success: (data)=>{
            view.text(data.hello);
        }
    });
});
