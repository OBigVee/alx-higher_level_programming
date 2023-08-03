$(()=>{
    $('div#add_item').click(()=>{
        $('ul.my_list').append('<li>item</li>');
    });
    $('div#remove_item').click(()=>{
        $('ul.my_list li:last-child').remove();
    });
    $('div#clear_list').click(()=>{
        $('ul.my_list').empty();
    })
})
