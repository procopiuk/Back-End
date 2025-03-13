const cliente = {
    nome: "carlos",
    idade: "40",
    email: "carlos.@gmail.com",
    telefone: "40028922",
    saldo: 2000,


    efetuaPagamento: function (valor){
        if(valor > this.saldo){
            console.log("saldo insuficiente");
        }else{
            this.saldo -= valor;
            console.log(`novo saldo ${this.saldo}`)
        }
    },

}