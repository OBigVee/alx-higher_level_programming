const url ='https://www.fourtonfish.com/hellosalut/hello/';
$(()=>{
    $('#btn_translate').click(()=>{
        const languageCode = $('#language_code').val();
    });

    $.get(url,(data)=>{
        $('#hello').text(data.hello);
    });
});
