function hora_atual() {
    return new Date().toLocaleTimeString();
}

$(document).ready(function(){
    
    $("#tabelaListar").DataTable();

    $("button#btn-get").click(function(){
        $("ul.list-group").append("<li class='list-group-item'>" + hora_atual() + "</li>");
    })
})