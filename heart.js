
function yourHeart(){
    let  i, j, k, l, m;
    let  c = 'a'; 
    
    for (i=1; i<=3; i++) { 
        let _tmp1 = "x"
        for (j=1; j<= 32-2*i; j++){
            _tmp1 +=_tmp1
        }  
        console.log(_tmp1); 
        for (k=1; k<= 4 *i+1; k++){
            console.log(c);
        }  
        for (l=1; l<= 13-4*i; l++){
            console.log("x");
        }   
        for (m=1; m<= 4*i+1; m++) {
            console.log(c);
        } 
        console.log("");  
    }
    for (i=1; i<=3; i++) {
        for (j=1; j<=24+1; j++){
            console("x"); 
        }
        for (k=1; k<=29; k++){
            console.log(c);
        }
        console.log("");  
    }
    for (i=7; i>=1; i--) { 
        for (j=1; j<=40-2*i; j++){
            console.log(" "); 
        }  
        for (k=1; k<=4*i-1; k++){
            console.log(c);
        } 
        console.log("");  
    }
    
    for (i=1; i<=39; i++){
        console.log("x");
    }
    console.log(c);
}