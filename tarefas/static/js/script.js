//função para confirmação excluir
document.querySelectorAll(".delete-btn").forEach(
    btn => {
        btn.addEventListener("click", function(e){
            e.preventDefault();

            const deLink = this.getAttribute("href");

            if(deLink && confirm ("Quer deletar esta Tarefa??"))
            {
                window.location.href = deLink;
            }
        });
    }

);

//Função de pequisa
document.getElementById("search-btn").addEventListener("click", function(){
    document.getElementById("search-form").onsubmit();
});

















