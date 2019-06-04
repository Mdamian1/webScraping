var randomColorGenerator = function () { 
    return '#' + (Math.random().toString(16) + '0000000').slice(2, 8); 
};


$(document).ready(function(){
    
    $.getJSON('meu_arquivo.json', function(data){
        var series = Array();
        var datas = Array();
        var nome = '';
        $.each(data, function(key, pontoPraia){ 
                
            //console.log(pontoPraia)
            var coletas = pontoPraia.coletas;
            var descricao = pontoPraia.descricao;
            nome = descricao[2].Ponto_de_Coleta;
            var ecolis = Array();
            datas = [];

            for(var i = 1; i<coletas.length; i++){
                datas.push(coletas[i].data)
                ecolis.push(coletas[i].ecolis)
            }

            console.log(nome);
            console.log(ecolis);

            series.push(
                        {
                            label: nome,
                            data: ecolis.reverse(),
                            borderColor: randomColorGenerator(),
                            backgroundColor: "transparent"
                        }
            )

            //console.log(nome)
        });
        
        
        console.log(series)
        var grafico = document.getElementById('grafico').getContext('2d');
        var chart = new Chart(grafico, {
            type: 'line',
            data: {
                labels: datas.reverse(),
                datasets: series
            }
        })

    })
    
})