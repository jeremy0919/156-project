var turn =0;



function createTable(){
  
    table = document.createElement('table');

    
    table.style.borderCollapse = "collapse";
    table.style.width = "auto";
  //  table.style.border = "2px black solid";
    let n = 3;
    let tablebody = document.createElement("tbody");
    table.appendChild(tablebody);

    for(let i =0; i<n;++i){ // table row
        let tr = document.createElement("trow");
        tr.style.borderCollapse = "collapse";
     //   tr.style.border = "2px black solid";
        for(let j =0; j<n; ++j){ // talbe data
            let td = document.createElement("td");
      
        td.addEventListener('click', function() { // function for piece movement
            makeTurn(i,j);
          });
            td.setAttribute("id",i+","+j);
            td.style.backgroundColor ="white";
          //  td.appendChild(input);
            td.style.height = "40px";
            td.style.width = "40px";
            td.style.border = "2px black solid";
         
            tr.appendChild(td); 
  
        }
        tablebody.appendChild(tr);
    
        
    }
  
    document.getElementsByClassName("table")[0].appendChild(table);
}

function makeTurn(x,y){
    let td = document.getElementById(x+","+y);
    if(turn ==0 && td.nodeValue != "black" && td.nodeValue!="blue"){
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
        td.setAttribute("nodevalue","black");
    }
    else if(turn ==1 && td.nodeValue != "black" && td.nodeValue!="blue"){
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
        td.setAttribute("nodevalue","black");
    }
}