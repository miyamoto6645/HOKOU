$(() => {
    $('#div').on('dbiclick',() =>{

        $('#div').text('ダブルクリックされました')
    })

})
$(() =>{
    $('#div').on('click',() => {
        
        $('#div').text('シングルクリックされました')
    })
})
