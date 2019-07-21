
$(function(){
    var canvas = document.getElementById("myCanvas");
    var ctx = canvas.getContext("2d");
    ctx.fillStyle = "#FF0000";
    ctx.fillRect(0, 0, 75, 75);
    var snakex = 100,
        snakey = 100;
    var x = 10,
        y = 0;
    var cord_array = [[100,100],];
    var eatx = 200;
    var eaty = 200;
    var snakelength = 1;
    
    function snakedraw(){

        for(let i = 0 ;i<snakelength;i++){

            ctx.beginPath();
            let a = cord_array[i][0];
            let b = cord_array[i][1];
            ctx.rect(a,b,10,10);
            ctx.strokeStyle = "black";
            ctx.fillStyle="#0095DD";
            ctx.fill();
            ctx.stroke();
            ctx.closePath();

        }
    }
    // 1 for downw 2 for up 3 for left 4 for right
    function food(){

        ctx.beginPath();
        ctx.rect(eatx,eaty,10,10);

        ctx.fillStyle="red";
        ctx.fill();
        ctx.closePath();

    }


    function check(x,y){

        for(let i=0;i<snakelength;i++){
            if(cord_array[i]==[x,y]){
                return 1;
            }
        }

        return 0;
    }

    function snake(){
        console.log(eatx,eaty,snakex,snakey,snakelength);
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        val = check(snakex,snakey);

        snakex+=x;
        snakey+=y;

        cord_array.unshift([snakex,snakey]);
        cord_array.pop();
        food();
        snakedraw();


        if( Math.abs(snakex - eatx)<10 && Math.abs(snakey-eaty)<10)
        {
            eatx = Math.floor(Math.random()*(canvas.width) + 1);
            eaty = Math.floor(Math.random()*(canvas.height) + 1);
            snakelength++;
            cord_array.unshift([snakex+x,snakey+y]);
            snakex+=x;
            snakey+=y;

            snakedraw();
        }

    }
    function move()
    {
        setInterval(snake(),10);
        clearInterval();
    }

    window.addEventListener("keydown", function(){
        console.log(" ASDF "+event.keyCode);
        if(event.keyCode == 38)
        {
            //snakey-=10;
            if(y==0)
            y=-10;x = 0;
        }
            // up
        if(event.keyCode == 40)
        {
            if(y==0)
            y=10;x = 0;
            //snakey+=10;
        }
            // down
        if(event.keyCode == 39)
        {
            if(x==0)
            x=10;y = 0;
           // snakex+=10;
        }
        // right
        if(event.keyCode == 37)
        {
           // snakex-=10;
           if(x==0)
            x=-10;y = 0;
        }
            // left

        move();
        })

});
