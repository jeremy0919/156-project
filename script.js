function newGame(){
    let turn =0;
let width =3;
gameOver=0;
count = 0;
for (let i = 0; i < width; i++) {
    }
    for(let i =0; i<width;++i){

        for(let j =0; j<width;++j){
            resultMatrix[i][j]=Math.random();
     //       alert(resultMatrix[i][j]);
        }
    }
    var removeTab1 = document.getElementById("NewButton");
    if(removeTab1!=null){
        var parentEl1 = removeTab1.parentElement;
            parentEl1.removeChild(removeTab1);
        }
    var removetab = document.getElementById("tab1");
    if(removetab!=null){
        var parentEl1 = removetab.parentElement;
            parentEl1.removeChild(removetab);
        }
    createTable();
}

let gameOver =0;
var turn =0;
let width =3;
let count = 0;
let resultMatrix = new Array(width);
for (let i = 0; i < width; i++) {
    resultMatrix[i] = new Array(length);
}
for(let i =0; i<width;++i){

    for(let j =0; j<width;++j){
        resultMatrix[i][j]=Math.random();
    }
}


function createTable(){
  
    table = document.createElement('table');

    
    table.style.borderCollapse = "collapse";
    table.style.width = "160px";
    table.style.height= "160px";
    table.style.border="solid";
    //table.style.border = "2px black solid";
    let n = 3;
table.setAttribute("id","tab1");
    let tablebody = document.createElement("tbody");
    table.appendChild(tablebody);

    for(let i =0; i<n;++i){ // table row
        let tr = document.createElement("trow");
        //   tr.style.borderCollapse = "collapse";
     //  tr.style.border = "2px black solid";
        for(let j =0; j<n; ++j){ // talbe data
            let td = document.createElement("td");
      
        td.addEventListener('click', function() { // function for piece movement
            makeTurn(i,j);
          });
            td.setAttribute("id",i+","+j);
            td.style.backgroundColor ="white";
          td.style.height = "50px";
            td.style.width = "50px";
            td.style.border = "solid";
         td.style.borderCollapse = "collapse";
            tr.appendChild(td); 
  
        }
        tablebody.appendChild(tr);
    
        
    }
  
    document.getElementsByClassName("table")[0].appendChild(table);
}

function makeTurn(x,y){
    let td = document.getElementById(x+","+y);
    
    if(turn ==0 && resultMatrix[x][y] !=1&&gameOver ==0){
        var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "40");
        svg.setAttribute("height", "40");

        var circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        circle.setAttribute("cx", "20");
        circle.setAttribute("cy", "20");
        circle.setAttribute("r", "15");
        circle.setAttribute("stroke", "black");
        circle.setAttribute("stroke-width", "3");
        circle.setAttribute("fill", "white");

        svg.appendChild(circle);
        td.appendChild(svg);
        turn =1;
        
        resultMatrix[x][y] =1;
    }
    else if(turn ==1&& resultMatrix[x][y] !=1 &&gameOver==0){
        var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "40");
        svg.setAttribute("height", "40");

        var circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        circle.setAttribute("cx", "20");
        circle.setAttribute("cy", "20");
        circle.setAttribute("r", "15");
        circle.setAttribute("stroke", "blue");
        circle.setAttribute("stroke-width", "3");
        circle.setAttribute("fill", "white");

        svg.appendChild(circle);
        td.appendChild(svg);
        turn =0;
        
        resultMatrix[x][y] =2;
    }
    count+=1;
    checkWin();
};

function checkWin(){
    for(let i =0; i<width;++i){
        if(resultMatrix[i][0] ==resultMatrix[i][1] && resultMatrix[i][0] == resultMatrix[i][2]  ){
            winCond(resultMatrix[i][0]);
        }
        if(resultMatrix[0][i] ==resultMatrix[1][i] && resultMatrix[0][i] == resultMatrix[2][i]  ){
            winCond(resultMatrix[0][i]);
        }

    }
    if(resultMatrix[1][1] ==resultMatrix[0][0] && resultMatrix[1][1] == resultMatrix[2][2]  ){
        winCond(resultMatrix[1][1]);
    }
    if(resultMatrix[1][1] ==resultMatrix[0][2] && resultMatrix[1][1] == resultMatrix[2][0]  ){
        winCond(resultMatrix[1][1]);
    }

    if(count>=9){
       alert("tie");
       gameOver=1;
       let b = document.createElement('button');
       b.setAttribute("value","Click for new game");
       b.addEventListener('click', function() { // function for piece movement
           newGame();
         });
       b.setAttribute("id","NewButton");
       document.getElementsByClassName("new")[0].appendChild(b);
    }
    

};

function winCond(x){
    alert("player "+x+" won");
    gameOver=1;
    count =0;
    let temp = "score"+x;
    alert("temp is " + temp);
   // let score = document.getElementById(temp);
  // alert(score.innerHTML);

   // score.item+=1;
    let b = document.createElement('button');
    b.setAttribute("value","Click for new game");
    b.addEventListener('click', function() { // function for piece movement
        newGame();
      });
    b.setAttribute("id","NewButton");
    document.getElementsByClassName("new")[0].appendChild(b);
}
