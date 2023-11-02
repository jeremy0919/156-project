
window.onload=function(){//should work needs to bw fixed
var httpRequest = new XMLHttpRequest();
httpRequest.onreadystatechange = function(){
    if(httpRequest.readyState === XMLHttpRequest.DONE){
        alert(httpRequest.status);
        if(httpRequest.status === 200){
            var data = JSON.parse(httpRequest.responseText); // object
            i = 1;
          //pass in location of username
            alert(data.user[i].name);
            document.getElementsByClassName("table2").innerHTML = data.user[i].name;
            document.getElementById("gamesPlayed").innerHTML = data.user[i].gamesPlayed;
            document.getElementById("wins").innerHTML = data.user[i].wins;
            document.getElementById("losses").innerHTML = data.user[i].losses;
            document.getElementById("winRate").innerHTML = data.user[i].winRate;
        }
    }
};
httpRequest.open('GET',"database.json",true) // path = local path
httpRequest.send();
}



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
    tablebody.style.paddingLeft = "50%"; // learn how to align in center
    tablebody.style.padding = "50%";
    tablebody.style.marginLeft = "50%";
    tablebody.style.margin = "50%";
    document.getElementsByClassName("table")[0].appendChild(table);
}

function makeTurn(x,y){
    let td = document.getElementById(x+","+y);
    let temp = 0;
    if(turn ==0 && resultMatrix[x][y] !=1&&gameOver ==0&&resultMatrix[x][y]!=2){
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
    count+=1;
    if(checkWin()==true){
        return;
    }
    while(turn ==1&&gameOver==0){
        x = Math.random()*3; // computer algorithm :)
        y=Math.random()*3;
        x=Math.floor(x);
        y=Math.floor(y);
        td = document.getElementById(x+','+y);
    if( resultMatrix[x][y] !=1 &&gameOver==0&&resultMatrix[x][y]!=2){
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
    if(checkWin()==true){
        return;
    }
}

    count+=1;

};

function checkWin(){
    for(let i =0; i<width;++i){
        if(resultMatrix[i][0] ==resultMatrix[i][1] && resultMatrix[i][0] == resultMatrix[i][2]  ){
            winCond(resultMatrix[i][0]);
            return true;
        }
        if(resultMatrix[0][i] ==resultMatrix[1][i] && resultMatrix[0][i] == resultMatrix[2][i]  ){
            winCond(resultMatrix[0][i]);
            return true;
        }

    }
    if(resultMatrix[1][1] ==resultMatrix[0][0] && resultMatrix[1][1] == resultMatrix[2][2]  ){
        winCond(resultMatrix[1][1]);
        return true;
    }
    if(resultMatrix[1][1] ==resultMatrix[0][2] && resultMatrix[1][1] == resultMatrix[2][0]  ){
        winCond(resultMatrix[1][1]);
        return true;
    }

    if(count>=9){
       alert("tie");
       gameOver=1;
       turn =0;
       let b = document.createElement('button');
       b.innerHTML = "Click for new game";
       b.addEventListener('click', function() { // function for piece movement
           newGame();
         });
       b.setAttribute("id","NewButton");
       document.getElementsByClassName("new")[0].appendChild(b);
       return true;
    }
    

};

function winCond(x){
    alert("player "+x+" won");
    gameOver=1;
    count =0;
    turn =0;
    let temp = "score"+x;
    let score = document.getElementById(temp);
    score.innerHTML = parseInt(score.innerHTML) + 1;

   // score.item+=1;
   let b = document.createElement('button');
   b.innerHTML = "Click for new game"; // set the button text
   b.addEventListener('click', function() { // function for piece movement
       newGame();
   });
   b.setAttribute("id","NewButton");
    document.getElementsByClassName("new")[0].appendChild(b);
    
}
